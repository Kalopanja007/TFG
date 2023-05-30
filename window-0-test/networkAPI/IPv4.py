import struct

from networkAPI.utils.bitwise_utils import BitwiseUtils
from networkAPI.utils.obj_repr import ObjRepr


class IPv4:
    """
        H: unsigned short -> 2 bytes [0 to 65,535]
        s: char           -> 1 byte  [-128 to 127]
        B: unsigned char  -> 1 byte  [0  to   255]
        L: unsigned long  -> 4 bytes [0 to 4,294,967,295]
        !: network (big-endian)

    """
    
    HEADR_LEN = 20
    TCP_PROTO = 6
    XTRACT_FLAGS = "!BBHHHBBH4s4s"
    
    """
        network level => {
            Version                     -> 4 bits
            Header Length               -> 4 bits
            Service Type                -> 1 byte
            *Total Length               -> 2 bytes
            Identification              -> 2 bytes
            Flags                       -> 3 bits
            Fragmentation Offset        -> 13 bits
            Time To Live                -> 1 byte
            -> Protocol                 -> 1 byte
            Hecader Checksum            -> 2 bytes
            Source Ip Address           -> 4 bytes
            Destination Ip Address      -> 4 bytes
            Options                     -> (variable)
        }
    """
    
    def __init__(self, ip_pkg: bytes):
        self._ip_pkg = ip_pkg

        # Pkg_attributes
        self.version         = None # 4  bits
        self.h_len_bytes     = None # 4  bits
        self.service_type    = None # 1  byte
        self.t_len_bytes     = None # 2  bytes
        self.identification  = None # 2  bytes
        self.flags           = None # 3  bits
        self.frag_offset     = None # 13 bits
        self.ttl             = None # 1  byte
        self.protocol        = None # 1  byte
        self.header_checksum = None # 2  bytes
        self.src_ip          = None # 4  bytes
        self.dst_ip          = None # 4  bytes


        self.init_segment()
    
    def init_segment(self) -> None:
        """
            Name: init_segment

            Description: 
                Given the IPv4 segment, it will slice all 
                the corresponding fields making bitwise 
                opertions if neccesary and convert IP addresses 
                to string. 

            Args:
                -> None

            Returns:
                ->  None
        """

        # Extracting the fields of the ipernet segment
        v_and_hlen, serv_type, t_len_bytes, identification, flags_and_frag_offset, ttl, protocol, h_checksum, src_ip, dst_ip  = struct.unpack(
            IPv4.XTRACT_FLAGS, self._ip_pkg
        )

        # Bit size macros 
        THREE_BITS           = 3
        FOUR_BITS            = 4
        FOUR_BYTES_PER_WORD  = 4

        ONE_BYTE             = 1
        TWO_BYTES            = 2

        BASE_TWO             = 2

        # Pkg_attributes
        
        # -------------------------
        # Converting "v_and_hlen" to bytes
        if not isinstance(v_and_hlen, bytes): 
            v_and_hlen = BitwiseUtils.int_to_bytes(v_and_hlen, ONE_BYTE)

        # Bitwise operations for "v_and_hlen"

        # Slicing -> (version_b_str) | (hlen_bin_str)
        version_b_str, hlen_bin_str = BitwiseUtils.split_to_str_bits(
                input_bytes = v_and_hlen,
                n_left_bits = FOUR_BITS
        )

        # -------------------------
        
        # 4 bits, 4 bits
        self.version         = int(version_b_str, BASE_TWO)
        self.h_len_bytes     = int(hlen_bin_str,  BASE_TWO) * FOUR_BYTES_PER_WORD

        # 1 byte
        self.service_type    = serv_type

        # 2 bytes
        self.t_len_bytes     = t_len_bytes

        # 2 bytes
        self.identification  = identification

        # -------------------------
        # Converting "flags_and_frag_offset" to bytes
        if not isinstance(flags_and_frag_offset, bytes): 
            flags_and_frag_offset = BitwiseUtils.int_to_bytes(flags_and_frag_offset, TWO_BYTES)

        # Bitwise operations for "flags_and_frag_offset"

        # Slicing -> (flags_b_str) | (frag_offset_b_str)
        flags_b_str, frag_offset_b_str = BitwiseUtils.split_to_str_bits(
                input_bytes = flags_and_frag_offset,
                n_left_bits = THREE_BITS
        )

        # "version_b_str" binary string to a list of booleans
        flags, = BitwiseUtils.str_bits_to_bool_list(flags_b_str)

        # -------------------------

        # 3 bits, 13 bits
        self.flags           = flags
        self.frag_offset     = int(frag_offset_b_str, BASE_TWO)

        # 1 byte
        self.ttl             = ttl

        # 1 byte
        self.protocol        = protocol

        # 2 bytes
        self.header_checksum = h_checksum

        # converting IPs to string: 4 bytes, 4 bytes
        self.src_ip          = self._bytes_ip_to_str(src_ip)
        self.dst_ip          = self._bytes_ip_to_str(dst_ip)

    def _bytes_ip_to_str(self, ip_bytes: bytes) -> str | None:
        """
            Name: _bytes_ip_to_str

            Descriprion: 
                Converts the IP address expressed in bytes to
                string. So it is more human readable :D

            Args:
                -> ip_bytes [bytes]: The IP address in bytes format

            Returns:
                ->  [str]: The corresponding IP address into string
                    format; None if there is an error.
                        
        """
        from socket import inet_ntoa

        try:
            ip_string = inet_ntoa(ip_bytes)
        
        except OSError:
            return None
        
        return ip_string
    
    def __str__(self) -> str:
        return self.__repr__() 
    
    def __repr__(self) -> str:
        """
            Name: __repr__

            Description: 
                Returns the public elements of the class. 

            Args:
                -> None

            Returns:
                ->  [str]: A string with a dict representation
                    of the class. 
        """
        
        return ObjRepr.pretty_print(self)