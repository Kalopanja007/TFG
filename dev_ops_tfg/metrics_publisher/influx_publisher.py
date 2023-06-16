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
    if not (w_size is None) and w_size < 512 :
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


if __name__ == "__main__":

    INFLUX_DB_NAME     = os.environ.get("INFLUX_DB_NAME", "influx")
    DB_HOST     = os.environ.get("INFLUX_CONTAINER", "influxdb")
    INFLUX_DB_PORT     = int(os.environ.get("INFLUX_DB_PORT", 8086))


    ic(INFLUX_DB_NAME)
    ic(DB_HOST)
    ic(INFLUX_DB_PORT)

    publisher = InfluxDB(db_name=INFLUX_DB_NAME, host=DB_HOST, port=INFLUX_DB_PORT)

    # Wait until influxdb server is found

    wait(lambda: influxdb_ready(DB_HOST), sleep_seconds=5)



    # Publish services and microservice

    SERVICE_NAMES = os.environ.get("SERVICE_NAMES", "no_service")
    services = SERVICE_NAMES.split(',')
    mservice = os.environ.get("MICROSERVICE", "nonamed")

    try:
        publisher.query(f"delete from services where microservice='{mservice}'")
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




    try:
        for ts, pkg in pc:

            np = NetworkProbe(ts, pkg)
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

