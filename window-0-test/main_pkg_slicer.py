import sys
import pcap

from sniffer import convert_timestamp

from probeTemplates.NetworkProbe import NetworkProbe
from networkAPI.utils.obj_repr import ObjRepr

from icecream import ic, install

import os

install()

ETH0 = "eth0"
LO = "lo"
WLO1 = "wlo1"

def get_my_mac() -> str:
    pass
    
    import uuid
    
    return (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
    for ele in range(0,8*6,8)][::-1]))

MAC = get_my_mac()

def show_details():
    pass
    global n_w0
    global n_pkgs

    os.system("clear")
    print('\n'*5)

    ic(n_w0)
    ic(n_pkgs)


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

n_w0 = 0
n_pkgs = 0

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
        # ic(np)

        allow_all = False

        if np.eth_header.dst_mac == MAC or allow_all:
        
            n_pkgs += 1

            if np.tcp_header and np.tcp_header.window_size == 0:
                n_w0 += 1

        show_details()
            
            
        # if np.tcp_header and np.tcp_header.window_size == 0:
        # if np and not (np.ip_header or np.tcp_header):
        #     print("################################################################################################")
        #     print(f"[{hora_rcv}]:")
        #     ic(pkg)
        #     ic(np)


        if False:
        # if np.tcp_header:
            # print("################################################################################################")
            # print(f"[{hora_rcv}]:")
            # ic(pkg)
            # ic(np)

            tcp_hdr = np.tcp_header
            ip_hdr  = np.ip_header
            # eth_hdr = np.eth_header

            # ------------
            # src_ip = np.ip_header.src_ip
            # dst_ip = np.ip_header.dst_ip
            # ------------

            total_pkg_len = ip_hdr.t_len_bytes

            ip_h_len      = ip_hdr.h_len_bytes
            
            tcp_h_len     = tcp_hdr.h_len_bytes



            # own_ip = "192.168.1.81"
            # my_ip_appears = [ip == own_ip for ip in (src_ip, dst_ip)]
            
            # if (ip_h_len != 20 or tcp_h_len != 20) and not any(my_ip_appears):
            # if (ip_h_len != 20 or tcp_h_len != 20) or not any(my_ip_appears):
            # if (ip_h_len != 20 and tcp_h_len != 20):
            # if ip_h_len != 20:
            # if tcp_h_len != 32:
            print("################################################################################################")
            print(f"[{hora_rcv}]:")

            # ic(src_ip)
            # ic(dst_ip)

            ic(total_pkg_len)
            ic(ip_h_len)
            ic(tcp_h_len)
            if total_pkg_len == (ip_h_len + tcp_h_len):
                hasUsefulLoad = False 
                ic(hasUsefulLoad)



            # ic(np)


            # src_ip = np.ip_header.src_ip
            # dst_ip = np.ip_header.dst_ip
            
            # ttl = np.ip_header.ttl

            # own_ip = "192.168.1.81"
            # if src_ip == own_ip:
            #     print(f"SEND -> {ttl}")
            # elif dst_ip == own_ip:
            #     print(f"RCV  -> {ttl}")
            
            # ic(src_ip)
            # ic(dst_ip)

            # ic(np.ip_header, type(np.ip_header))
            # sys.exit()  

            # dst_ip = np.ip_header.dst_ip
            # src_ip = np.ip_header.src_ip

            # own_ip = "192.168.1.81"

            # my_ip_appears = [ip == own_ip for ip in (src_ip, dst_ip)]

            # if not any(my_ip_appears):
            #     ic(pkg)
            #     print("################################################################################################")
            #     print(f"[{hora_rcv}]:")
            #     ic(np)                             
            #     ic(src_ip, dst_ip)                             
            
                # sys.exit()  

        # # if hora_rcv .-> milisegundo = 0
            # # publicar ↓↓↓↓
            # ancho_banda = ancho_banda_p = v_0 = 0

        # if not np.ip_header and np.eth_header.ethertype != 34525:
        #     print("################################################################################################")
        #     print(f"[{hora_rcv}]:")
        #     ic(pkg)
        #     ic(np)
            



except KeyboardInterrupt:
        pass
        print("\n\nEND :)")
        try:
            ic(n_w0)
            ic(n_pkgs)
            
            ic( f"{n_w0*100 // n_pkgs}%" )
        except:
            pass
        sys.exit()








