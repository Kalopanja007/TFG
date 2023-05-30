from icecream import ic
import random

import socket

def bytes_to_ip(ip_bytes):
    ip_string = socket.inet_ntoa(ip_bytes)
    return ip_string


def main4():
    pass
    size = 4

    byte_string = b''.join([random.randint(0, 255).to_bytes(1, 'big') for i in range(size)])

    ic(byte_string)

    ip_bytes = b'\x7f\x00\x00\x01'  # Dirección IP 127.0.0.1 en bytes
    ip_string = bytes_to_ip(ip_bytes)
    ip_string = bytes_to_ip(byte_string)
    ic(ip_string)  # Imprime: 127.0.0.1


def _str_bits_to_bool_list(*args: str) -> tuple[list[bool], ...]:
    """
        Name: str_bits_to_bool_list

        Description: 
            
            (For each of the *args):

            Evaluates each "binary" element of the bitstring. 
            It creates a list of booleans where each element 
            is True or False depending if there was a 0 or a 
            1 when iterating the previous string.

        Args:
            -> args: list[str]: A list of array representations made of 
                                an string of 0s and 1s.

        Returns:
            ->  tuple[list[bool], ...]:
                    (for each of the *args) A list of booleans. 
    """
    boolean_lists = []

    # Lambda function that evaluates the string value
    char_to_bool = lambda x: bool(eval(x))

    # Creating the list of booleans based on the arguments
    for bin_str in args:
        # bool_list  = list(map(lambda x: char_to_bool(x), bin_str))
        bool_list  = list(map(char_to_bool, bin_str))

        boolean_lists.append(bool_list)

    
    return boolean_lists

def _split_to_str_bits(input_bytes: bytes, n_left_bits: int) -> tuple[str, str]:
    """
        Name: split_to_str_bits

        Description: 
            Divides a "bytes" object into two different sub-strings 
            that represent the byte slice in binary format

        Args:
            -> input_bytes [bytes]: The byte number to be splitted.
            -> n_left_bits [int]:   Number of bits to be kept in the 
                                    left part.

        Returns:
            ->  tuple[str, str]:
                    (for both args) A string that represents the
                    byte slice in binary format.
    """
    EIGHT_BITS = 8

    # Total bits lenght of input_bytes
    total_bits = len(input_bytes) * EIGHT_BITS

    # Checking bounds
    if n_left_bits < 0 or n_left_bits > total_bits:
        raise ValueError("Invalid \"n_left_bits\" for the left side")

    # Getting a bit string from input_bytes
    bits = ''.join(format(byte, '08b') for byte in input_bytes)
    
    
    # Splitting the bit string
    left_frag  = bits[:n_left_bits]
    right_frag = bits[n_left_bits:]

    return left_frag, right_frag

def main5():
    pass

    size = 2

    byte_string = b''.join([random.randint(0, 255).to_bytes(1, 'big') for i in range(size)])

    ic(byte_string)

    hlen, resrvd_flags = _split_to_str_bits(byte_string, 4)

    ic(hlen, resrvd_flags)

    resvd, flags = resrvd_flags[:6], resrvd_flags[6:]
    
    ic(resvd, flags)

    resvd, flags, hlen = _str_bits_to_bool_list(resvd, flags, hlen)

    ic(resvd, flags, hlen)

def main6():
    pass

    size = 3

    byte_string = b''.join([random.randint(0, 255).to_bytes(1, 'big') for i in range(size)])
    # byte_string = b"\xb2"

    ic(byte_string)

    hlen, resrvd_flags = _split_to_str_bits(byte_string, 4)

    ic(hlen, resrvd_flags)
    
    hlen_int         = int(hlen, 2)
    resrvd_flags_int = int(resrvd_flags, 2)

    ic(hlen_int, resrvd_flags_int)
    


if __name__ == "__main__":
    pass
    # main()
    # main2()
    # main3()
    # main4()
    # main5()
    main6()



"""
    a,b, x3, c = func()

"""


