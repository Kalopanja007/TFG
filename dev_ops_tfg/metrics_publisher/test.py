from field_xtractor import get_eth_segment

import random
from icecream import ic
import binascii

from networkAPI.na_importAPI import Eth
from probeTemplates.pt_importAPI import NetworkProbe

BYTEORDER = "big"

def mac_to_str(mac_bytes: bytes) -> str:
    mac_string = ':'.join(binascii.hexlify(mac_bytes).decode('utf-8')[i:i+2] for i in range(0, 12, 2))

    return mac_string

def main1():
    pass
    size = 14  # tamaño deseado de la cadena de bytes
    byte_string = b''.join([random.randint(0, 255).to_bytes(1, 'little') for i in range(size)])


    # ic(byte_string)
    # ic(type(byte_string))
    # ic(len(byte_string))


    dst_mac, orig_mac, ether_type  = get_eth_segment(byte_string)

    ic(dst_mac, orig_mac, ether_type)

    dst_mac_str, orig_mac_str = [*map(lambda x: mac_to_str(x), [dst_mac, orig_mac])]


    ic(dst_mac_str, orig_mac_str)

def main2():
    pass
    size = 14  # tamaño deseado de la cadena de bytes
    byte_string = b''.join([random.randint(0, 255).to_bytes(1, 'big') for i in range(size)])

    np = NetworkProbe(0, byte_string)
    ic(np.eth_dict)

def int_to_bytes(int_num: int, n_bytes: int = None) -> bytes:
    pass
    SEVEN_BITS      = 7
    EIGHT_BITS_BYTE = 8
    BIG_ENDIAN      = "big"

    minimun_bytes = (int_num.bit_length() + SEVEN_BITS) // EIGHT_BITS_BYTE

    if not n_bytes or n_bytes < minimun_bytes:
        n_bytes = minimun_bytes
        print("aaa")

    ic(n_bytes)

    # bytes_num = int_num.to_bytes(n_bytes, BIG_ENDIAN)

    return int_num.to_bytes(n_bytes, BIG_ENDIAN)


def main3():
    pass

    n = 2000
    n_bytes = 2
    n_bytes = 1
    n_bytes = -1
    n_bytes = None


    out = int_to_bytes(n, n_bytes)

    ic(out,type(out))

if __name__ == '__main__':
    # main1()
    # main2()
    main3()





