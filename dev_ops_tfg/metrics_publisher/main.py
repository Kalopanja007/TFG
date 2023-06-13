import sys
import pcap

from sniffer import get_window_segment, convert_timestamp

from icecream import ic

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
        window_size = get_window_segment(pkg)

        hora_rcv = convert_timestamp(ts) 

        # if window_size == 0:
        #      v_0+=1

        # ancho_banda = sacar *Longitud total        -> 2 bytes * 8

        # ancho_banda_p +=1  

        # if window_size is not None:
        # # if window_size is not None:
        if window_size==0:
            print("################################################################################################")
            print(f"[{hora_rcv}]: window_size: {window_size}")
            ic(ts, pkg)

        # # if hora_rcv .-> milisegundo = 0
            # # publicar ↓↓↓↓
            # ancho_banda = ancho_banda_p = v_0 = 0




except KeyboardInterrupt:
        pass
        print("\n\nEND :)")
        sys.exit()








