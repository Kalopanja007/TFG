
import datetime
import struct
from icecream import ic

ET_IPV4 = 0x0800

TCP_PROTO = 6

def convert_timestamp(unix_ts: float):

    # Convertir Unix timestamp a objeto datetime
    fecha_hora = datetime.datetime.fromtimestamp(unix_ts)

    # Obtener la hora actual como una cadena de texto
    return fecha_hora.strftime("%H:%M:%S.%f")[:-3]

def get_window_segment(pkg: bytes) -> tuple[bytes | None]:
    '''
        H: unsigned short -> 2 bytes [0 to 65,535]
        s: char           -> 1 byte  [-128 to 127]
        B: unsigned char  -> 1 byte  [0  to   255]
        L: unsigned long  -> 4 bytes [0 to 4,294,967,295]
        !: network (big-endian)

    '''
    
    err_ret = None

    if pkg is None:
        return err_ret 
    
    '''
        nivel de enlace => {
            MAC destino -> 6 bytes
            MAC oringen -> 6 bytes
            -> EtherType  -> 2 bytes
        }
    '''
    eth = struct.unpack('!6s6sH', pkg[0:14])
    if eth[2] != ET_IPV4: # no es IPv4
        return err_ret

    # ic(eth)
    ########################################################################

    '''
        nivel de red => {
            Version                     -> 4 bits
            Longitud de la cabecera     -> 4 bits
            Tipo de servicio            -> 1 byte
            *Longitud total              -> 2 bytes
            Identificación              -> 2 bytes
            Bandera de fragmentación    -> 3 bits (Dejarlo en bits)
            Desplazamiento de fragmento -> 13 bits
            Tiempo de vida              -> 1 byte
            -> Protocolo                   -> 1 byte
            Checksum                    -> 2 bytes
            Dirección IP de origen      -> 4 bytes
            Dirección IP de destino     -> 4 bytes
            Opciones                    -> (variable)
        }
    '''

    iph = struct.unpack('!BBHHHBBH4s4s', pkg[14:34])
    if iph[6] != TCP_PROTO: # no es TCP
        return err_ret 
    
    '''
        nivel de transporte => {
            Puerto de origen         -> 2 bytes
            Puerto de destino        -> 2 bytes
            Número de secuencia      -> 4 bytes
            Número de confirmación   -> 4 bytes
            Longitud de la cabecera  -> 4 bits
            Reservado                -> 6 bits
            Flags                    -> 6 bits
            -> Tamaño de ventana        -> 2 bytes
            Checksum                 -> 2 bytes
            Puntero urgente          -> 2 bytes
            Opciones                 -> (variable)
            Datos                    -> (variable)
        }
    '''

    tcph = struct.unpack('!HHLLBBHHH', pkg[34:54])

    # ic(tcph)

    # Extraer la ventana de los paquetes TCP
    window_size = tcph[6]
    
    return window_size



# Ejecutar

# sudo $(pipenv --venv)/bin/python main.py
