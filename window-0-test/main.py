import socket
import sys
import pcap

from sniffer import get_window_segment

from icecream import ic

ETH0 = "eth0"
LO = "lo"
WLO1 = "wlo1"


TCP_PROTO = "tcp"

# Configurar interfaces de red

iface = WLO1

# MODO PROMISCUO: Capturar tráfico que pasa por la máquina (no solo dirigido a ella)

# Inmediate: Le decimos a libpcap que entregue los paquetes inmediatamente después de capturarlos.  

pc = pcap.pcap(name=iface, promisc=True, immediate=True)

# Filtramos los paquetes TCP en este caso
pc.setfilter(TCP_PROTO)


# Captura de tráfico

try:
    for ts, pkg in pc:
        # Obtenemos el tamaño de la ventana + timestamp
        hora_rcv, window_size = get_window_segment(ts, pkg)

        if window_size is not None:
        # if window_size==0:
            print("################################################################################################")
            print(f"[{hora_rcv}]: window_size: {window_size}")
            ic(ts, pkg)

except KeyboardInterrupt:
        pass
        print("\n\nEND :)")








