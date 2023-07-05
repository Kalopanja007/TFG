import sys
import pcap
from waiting import wait

from probeTemplates.Publisher import InfluxDB

from sniffer import convert_timestamp

from probeTemplates.NetworkProbe import NetworkProbe
from networkAPI.utils.obj_repr import ObjRepr

from icecream import ic, install

import os

from customMetrics.network_metrics import get_microservice_name
from customMetrics.network_metrics import get_pkg_direction
from customMetrics.network_metrics import get_pkg_size
from customMetrics.network_metrics import get_protocol
from customMetrics.network_metrics import get_time_to_live
from customMetrics.network_metrics import get_window_size
from customMetrics.network_metrics import get_my_mac


def show_details(np: NetworkProbe):

    os.system("clear")
    print('\n'*5)

    ic(get_microservice_name())
    ic(get_pkg_direction(np))
    ic(get_pkg_size(np))
    ic(get_protocol(np))
    ic(get_time_to_live(np))
    ic(get_window_size(np))

def process_networkpackage(np: NetworkProbe):

    data = {
        "measurement" : "networkissues",
        "tags": {
            "microservice" : get_microservice_name(),
            "pkg_direction" : get_pkg_direction(np),
            "protocol" : get_protocol(np),
        },
        "fields" : {
        }
    }

    # Should it be published to DB?
    b_issues = False

    w_size = get_window_size(np)
    if not (w_size is None) and w_size < 1 :
        data["fields"]["wsize0"] = True
        b_issues = True

    ttlive = get_time_to_live(np)
    if not (ttlive is None) and ttlive==1:
        data["fields"]["TTL1"] = True
        b_issues = True

    if (not b_issues and not (data["tags"]["protocol"] is None) and data["tags"]["protocol"]=="ICMP"):
        data["fields"]["ICMP"] = True
        b_issues = True

    if b_issues:
        return data
    else:
        return None



def influxdb_server_ip():
    import socket
    return socket.gethostbyname(DB_HOST)



def publish_accum_data(num_bytes_in, num_bytes__out, num_packets_in, num_packets_out, num_secs):
    bitrate_in = num_bytes_in * 8 / num_secs
    bitrate_out = num_bytes_out * 8 / num_secs
    data_in = {
        "measurement": "bandwidth",
        "tags": {
            "microservice": get_microservice_name(),
            "pkg_direction": "in"
        },
        "fields": {
            "bitrate": bitrate_in,
            "numpaqs": num_packets_in
        }
    }
    data_out = {
        "measurement": "bandwidth",
        "tags": {
            "microservice": get_microservice_name(),
            "pkg_direction": "out"
        },
        "fields": {
            "bitrate": bitrate_out,
            "numpaqs": num_packets_out
        }
    }

    try:
        publisher.publish([data_in])
        publisher.publish([data_out])
    except Exception:
        print("Error writing Bandwidth data")


def process_all_data(np: NetworkProbe):
    data = {
        "measurement": "alldata",
        # "time"       : np.pkg_timestamp,
        "tags"       : {
            "orig_mac"      : np.eth_header.orig_mac,
            "dst_mac"       : np.eth_header.dst_mac,
            "my_mac"        : get_my_mac(),
            "microservice"  : get_microservice_name(),
            "pkg_direction" : get_pkg_direction(np),
            "protocol"      : get_protocol(np),
        },
        "fields"     : {
            "window_size"   : get_window_size(np),
            "pkg_size" : get_pkg_size(np),
            "time_to_live"  : get_time_to_live(np),
        }  
    }
    ok = False
    for k,v in data["fields"].items():
        if v is not None:
            ok = True
    if ok:
        return data
    else:
        return None

def show_data(data):

    os.system("clear")
    print('\n'*5)
    ic(ObjRepr.pretty_print(data))

def influxdb_ready(influxdb_host:str):
    try:
        publisher.query("show measurements")
        return True
    except:
        print(f"Cannot connect to InfluxDB server [{influxdb_host}]. Retrying...")
        return False


def publish_services_devoted(publisher: InfluxDB):
    # Publish services and microservice

    SERVICE_NAMES = os.environ.get("SERVICE_NAMES", "no_service")
    services = SERVICE_NAMES.split(',')
    mservice = os.environ.get("MICROSERVICE", "nonamed")

    try:
        #publisher.query(f"delete from services where microservice='{mservice}'")
        for service in services:
            data = {
                "measurement": "services",
                "tags"     : {
                    "microservice" : mservice,
                },
                "fields"     : {
                    "service"   : service,
                }  
            }
            publisher.publish([data])
    except:
        print("Error updating list of services for this microservice. List outdated")


if __name__ == "__main__":

    INFLUX_DB_NAME     = os.environ.get("INFLUX_DB_NAME", "monitoring")
    DB_HOST     = os.environ.get("INFLUX_CONTAINER", "influxdb")
    INFLUX_DB_PORT     = int(os.environ.get("INFLUX_DB_PORT", 8086))


    ic(INFLUX_DB_NAME)
    ic(DB_HOST)
    ic(INFLUX_DB_PORT)

    publisher = InfluxDB(db_name=INFLUX_DB_NAME, host=DB_HOST, port=INFLUX_DB_PORT)


    install()

    # Configurar interfaces de red

    # MODO PROMISCUO: Capturar tráfico que pasa por la máquina (no solo dirigido a ella)

    # Inmediate: Le decimos a libpcap que entregue los paquetes inmediatamente después de capturarlos.  

    #iface = WLO1
    # pc = pcap.pcap(name=iface, promisc=False, immediate=True)
    pc = pcap.pcap(promisc=False, immediate=True)
    # pc = pcap.pcap(name="lo", promisc=False, immediate=True)

    ic(pcap.findalldevs())
    ic(pc.name)

    #TCP_PROTO = "tcp"
    # Filtramos los paquetes TCP en este caso
    # pc.setfilter(TCP_PROTO)

    # # Captura de tráfico
    # ancho_banda = ancho_banda_p = v_0 = 0


    # Wait until influxdb server is found

    wait(lambda: influxdb_ready(DB_HOST), sleep_seconds=5)


    t_inicper = 0   # Accounts for data (bits/sec and num. packets) in a period of 10 seconds
    num_bytes_in = 0
    num_bytes_out = 0
    num_packets_in = 0
    num_packets_out = 0

    t_pubservices_inicper = 0
    try:
        for ts, pkg in pc:

            # Periodic publishing of services devoted by this microservice, in 'services' measurement
            # Being periodic, instead of a one off when starting the microservice has two advantages:
            # - If InflixDB data is lost, 'services' measurement will be filled in again in a short period of time
            # - Publishing every few seconds informs that the microservide is alive
            if t_pubservices_inicper==0 or ts - t_pubservices_inicper > 30:
                publish_services_devoted(publisher)
                t_pubservices_inicper = ts


            np = NetworkProbe(ts, pkg)
            pkg_direction = get_pkg_direction(np)
            if (pkg_direction):
                pkg_size = get_pkg_size(np)
                if pkg_direction == 'in':
                    if pkg_size:
                        num_bytes_in += pkg_size
                    num_packets_in += 1
                else:
                    if pkg_size:
                        num_bytes_out += pkg_size
                    num_packets_out += 1

            if t_inicper==0:
                t_inicper = ts
            if ts - t_inicper > 10:
                t_period = ts - t_inicper
                t_inicper = ts
                publish_accum_data(num_bytes_in, num_bytes_out, num_packets_in, num_packets_out, t_period)
                num_bytes_in = 0
                num_bytes_out = 0
                num_packets_in = 0
                num_packets_out = 0




            #show_details(np)
            data = process_networkpackage(np)
            if data:
                show_data(data)
                try:
                    publisher.publish([data])
                except:
                    print("Error writing DB. Message discarded")
            
            # data = process_all_data(np)
            # if np.ip_header:
            #     dst_ip = np.ip_header.dst_ip
            #     src_ip = np.ip_header.src_ip
            #     if dst_ip == influxdb_ip or src_ip == influxdb_ip:
            #         data = None
            #         print(f"Filtrado {influxdb_ip}")
            # if data:
            #    show_data(data)
            #    publisher.publish([data])


    except KeyboardInterrupt:
            print("\n\nEND :)")
            sys.exit()

