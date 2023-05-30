import struct

from networkAPI.utils.bitwise_utils import BitwiseUtils
from networkAPI.utils.obj_repr import ObjRepr


class TCP:
    """
        H: unsigned short -> 2 bytes [0 to 65,535]
        s: char           -> 1 byte  [-128 to 127]
        B: unsigned char  -> 1 byte  [0  to   255]
        L: unsigned long  -> 4 bytes [0 to 4,294,967,295]
        !: network (big-endian)

    """
    
    HEADR_LEN = 20
    # XTRACT_FLAGS = "!HHLLBBHHH"
    XTRACT_FLAGS = "!HHLLHHHH"
    
    """
        transport level => {
            Source Port             -> 2 bytes
            Destination Port        -> 2 bytes
            Sequence Number         -> 4 bytes
            Acknowledgement Number  -> 4 bytes
            Header Length           -> 4 bits
            Reserved                -> 6 bits
            Flags                   -> 6 bits
            -> Window Size             -> 2 bytes
            Checksum                -> 2 bytes
            Urgent Pointer          -> 2 bytes
            Options                 -> (variable)
            Data                    -> (variable)
        }
    """
    
    def __init__(self, tcp_pkg: bytes):
        self._tcp_pkg = tcp_pkg

        # Pkg_attributes
        self.scr_port       = None # 2  bytes
        self.dst_port       = None # 2  bytes
        self.seq_number     = None # 4  bytes
        self.ack_number     = None # 4  bytes
        self.h_len_bytes    = None # 4  bits
        self.reserved       = None # 6  bits
        self.flags          = None # 6  bits
        self.window_size    = None # 2  bytes
        self.checksum       = None # 2  bytes
        self.urgent_pointer = None # 2  bytes


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
        scr_port, dst_port, seq_number, ack_number, hl_resrvd_flags, window_size, checksum, urgent_pointer  = struct.unpack(
            TCP.XTRACT_FLAGS, self._tcp_pkg
        )

        # Bit size macros
        SIX_BITS  = 6
        FOUR_BITS = 4
        FOUR_BYTES_PER_WORD  = 4

        TWO_BYTES            = 2

        BASE_TWO             = 2

        # Pkg_attributes

        # 2  bytes
        self.scr_port       = scr_port
        
        # 2  bytes
        self.dst_port       = dst_port
        
        # 4  bytes
        self.seq_number     = seq_number
        
        # 4  bytes
        self.ack_number     = ack_number

        # -------------------------
        # Converting "hl_resrvd_flags" to bytes
        if not isinstance(hl_resrvd_flags, bytes): 
            hl_resrvd_flags = BitwiseUtils.int_to_bytes(hl_resrvd_flags, TWO_BYTES)

        # Bitwise operations for "hl_resrvd_flags"

        # Slicing -> (hlen_bin_str) | (resrvd_str + flags_str)
        hlen_bin_str, resrvd_flags = BitwiseUtils.split_to_str_bits(hl_resrvd_flags, FOUR_BITS)

        # Slicing "reserved" and "flag" fields
        resvd_str, flags_str = resrvd_flags[:SIX_BITS], resrvd_flags[SIX_BITS:]

        # Converting "reserved" and "flag" to a list of booleans
        resvd, flags = BitwiseUtils.str_bits_to_bool_list(resvd_str, flags_str)

        # -------------------------
        
        # 4  bits, 6  bits, 6  bits
        self.h_len_bytes    = int(hlen_bin_str, BASE_TWO) * FOUR_BYTES_PER_WORD
        self.reserved       = resvd
        self.flags          = flags
        
        # 2  bytes
        self.window_size    = window_size
        
        # 2  bytes
        self.checksum       = checksum
        
        # 2  bytes
        self.urgent_pointer = urgent_pointer


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