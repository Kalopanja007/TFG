import sys
import pcap
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

install()

ETH0 = "eth0"
LO = "lo"
WLO1 = "wlo1"

def show_details(np: NetworkProbe):
    pass

    os.system("clear")
    print('\n'*5)

    ic(get_microservice_name())
    ic(get_pkg_direction(np))
    ic(get_pkg_size(np))
    ic(get_protocol(np))
    ic(get_time_to_live(np))
    ic(get_window_size(np))

def show_details_influx(np: NetworkProbe):
    pass

    os.system("clear")
    print('\n'*5)

    get_microservice_name()
    get_pkg_direction(np)
    get_pkg_size(np)
    get_protocol(np)
    get_time_to_live(np)
    get_window_size(np)

    data = {
        "INFLUX_DB_MEASUREMENT": INFLUX_DB_MEASUREMENT,
        "time"       : np.pkg_timestamp,
        "tags"       : {
            "microservice"  : get_microservice_name(),
            "pkg_direction" : get_pkg_direction(np),
            "protocol"      : get_protocol(np),
        },
        "fields"     : {
            "window_size"   : get_window_size(np),
            "time_to_live"  : get_time_to_live(np),
        }  
    }

    def remove_none(d: dict):
        aux = d.copy()
        items = aux.items()

        for k,v in items:
            if v is None:
                d.pop(k)
        return d
    
    data["tags"]   = remove_none(data["tags"])
    data["fields"] = remove_none(data["fields"])

    ic(ObjRepr.pretty_print(data))

    return [data]





TCP_PROTO = "tcp"

# Configurar interfaces de red

iface = WLO1

# MODO PROMISCUO: Capturar tráfico que pasa por la máquina (no solo dirigido a ella)

# Inmediate: Le decimos a libpcap que entregue los paquetes inmediatamente después de capturarlos.  

# pc = pcap.pcap(name=iface, promisc=False, immediate=True)
pc = pcap.pcap(promisc=False, immediate=True)
# pc = pcap.pcap(name="lo", promisc=False, immediate=True)

ic(pcap.findalldevs())
ic(pc.name)

# Filtramos los paquetes TCP en este caso
# pc.setfilter(TCP_PROTO)


# # Captura de tráfico
# ancho_banda = ancho_banda_p = v_0 = 0

INFLUX_DB_NAME     = os.environ.get("INFLUX_DB_NAME", "influx")
DB_HOST     = os.environ.get("INFLUX_CONTAINER", "influxdb")
INFLUX_DB_PORT     = int(os.environ.get("INFLUX_DB_PORT", 8086))
INFLUX_DB_MEASUREMENT = os.environ.get("INFLUX_DB_MEASUREMENT", "")


# publisher = InfluxDB(INFLUX_DB_NAME=INFLUX_DB_NAME, host=DB_HOST, port=INFLUX_DB_PORT)


ic(INFLUX_DB_NAME)
ic(DB_HOST)
ic(INFLUX_DB_PORT)
ic(INFLUX_DB_MEASUREMENT)

try:
    for ts, pkg in pc:
        pass
        np = NetworkProbe(ts, pkg)
        # show_details(np)
        
        data = show_details_influx(np)
        # publisher.publish(data)
        
            

except KeyboardInterrupt:
        pass
        print("\n\nEND :)")
        sys.exit()








