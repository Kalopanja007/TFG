
import struct
from icecream import ic

ET_IPV4 = 0x0800

TCP_PROTO = 6

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
        Data Link Layer => {
            MAC destino -> 6 bytes
            MAC oringen -> 6 bytes
            -> EtherType  -> 2 bytes
        }
    '''
    eth = struct.unpack('!6s6sH', pkg[0:14])
    if eth[2] != ET_IPV4: # no es IPv4
        return err_ret

def get_eth_segment(pkg: bytes) -> dict[str, str | bytes | int] | None:
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
    # eth = struct.unpack('!6s6sH', pkg[0:14])
    # eth[2]   
    # if eth[2] != ET_IPV4: # no es IPv4

    eth_keys = [
        "dst_mac",
        "orig_mac",
        "ether_type"             
    ]

    eth_values = struct.unpack('!6s6sH', pkg[0:14])


    # eth_dict = dict(zip(eth_keys, eth_values))

    # return eth_dict

    return eth_values
