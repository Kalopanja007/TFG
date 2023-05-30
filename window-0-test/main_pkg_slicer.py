import sys
import pcap

from sniffer import convert_timestamp

from probeTemplates.NetworkProbe import NetworkProbe
from networkAPI.utils.obj_repr import ObjRepr

from icecream import ic, install

install()

ETH0 = "eth0"
LO = "lo"
WLO1 = "wlo1"


TCP_PROTO = "tcp"

# Configurar interfaces de red

iface = WLO1

# MODO PROMISCUO: Capturar tráfico que pasa por la máquina (no solo dirigido a ella)

# Inmediate: Le decimos a libpcap que entregue los paquetes inmediatamente después de capturarlos.  

pc = pcap.pcap(name=iface, promisc=False, immediate=True)

# Filtramos los paquetes TCP en este caso
pc.setfilter(TCP_PROTO)


# # Captura de tráfico
# ancho_banda = ancho_banda_p = v_0 = 0

try:
    for ts, pkg in pc:
        #####################################

        # Se ejecuta el padre
            
            # Instancia la clase root con el (pkg y ts) como atributo
            # 


        # Comprueba los directorios
            
            # Lista scripts del dir
            # Filtra los que cumplen los requisitos
            # Los importa
            # Ejecuta su método estático
                
                # Este posteriormente puede publicar con el ts del padre


        #####################################


        # Obtenemos el tamaño de la ventana + timestamp

        hora_rcv = convert_timestamp(ts) 

        # if window_size == 0:
        #      v_0+=1

        # ancho_banda = sacar *Longitud total        -> 2 bytes * 8

        # ancho_banda_p +=1  

        # if window_size is not None:
        # # if window_size is not None:

        np = NetworkProbe(ts, pkg)

        if np.tcp_header:
            print("################################################################################################")
            print(f"[{hora_rcv}]:")
            ic(pkg)
            ic(np)

            # print(np)
            # print(type(np.__repr__()))

            d = ObjRepr.dict_repr(np)

            ic(d["tcp_header"]["window_size"])
            
            
            sys.exit()

        # # if hora_rcv .-> milisegundo = 0
            # # publicar ↓↓↓↓
            # ancho_banda = ancho_banda_p = v_0 = 0




except KeyboardInterrupt:
        pass
        print("\n\nEND :)")
        sys.exit()








