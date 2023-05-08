from field_xtractor import get_eth_segment

import random
from icecream import ic
import binascii

BYTEORDER = "big"

def mac_to_str(mac_bytes: bytes) -> str:
    mac_string = ':'.join(binascii.hexlify(mac_bytes).decode('utf-8')[i:i+2] for i in range(0, 12, 2))

    return mac_string

def main():
    size = 14  # tamaño deseado de la cadena de bytes
    byte_string = b''.join([random.randint(0, 255).to_bytes(1, 'little') for i in range(size)])


    # ic(byte_string)
    # ic(type(byte_string))
    # ic(len(byte_string))


    dst_mac, orig_mac, ether_type  = get_eth_segment(byte_string)

    ic(dst_mac, orig_mac, ether_type)

    dst_mac_str, orig_mac_str = [*map(lambda x: mac_to_str(x), [dst_mac, orig_mac])]


    ic(dst_mac_str, orig_mac_str)

if __name__ == '__main__':
    # main()

    from networkAPI.na_importAPI import Eth
    from probeTemplates.pt_importAPI import NetworkProbe

    size = 14  # tamaño deseado de la cadena de bytes
    byte_string = b''.join([random.randint(0, 255).to_bytes(1, 'little') for i in range(size)])

    np = NetworkProbe(0, byte_string)
    ic(np.eth_dict)


    
