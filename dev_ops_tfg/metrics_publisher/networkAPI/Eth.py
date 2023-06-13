import binascii
import struct

from networkAPI.utils.obj_repr import ObjRepr


class Eth:
    """
        H: unsigned short -> 2 bytes [0 to 65,535]
        s: char           -> 1 byte  [-128 to 127]
        B: unsigned char  -> 1 byte  [0  to   255]
        L: unsigned long  -> 4 bytes [0 to 4,294,967,295]
        !: network (big-endian)

    """
    
    HEADR_LEN = 14
    ET_IPV4 = 0x0800
    XTRACT_FLAGS = '!6s6sH'
    
    """
        Data Link Layer => {
            destination MAC  -> 6 bytes
            origin MAC       -> 6 bytes
            -> EtherType     -> 2 bytes
        }
    """
    
    def __init__(self, eth_pkg: bytes):
        self._eth_pkg  = eth_pkg
        
        # Pkg_attributes
        self.dst_mac   = None # 6 bytes
        self.orig_mac  = None # 6 bytes
        self.ethertype = None # 2 bytes

        self.init_segment()

    def init_segment(self) -> None:
        """
            Name: init_segment

            Description: 
                Given the IPv4 segment, it will slice all 
                the corresponding fields and transform dest 
                and orig MAC addresses to string.

            Args:
                -> None

            Returns:
                ->  None
        """

        # Extracting the fields of the ethernet segment
        dst_mac, orig_mac, ethertype = struct.unpack(
            Eth.XTRACT_FLAGS, self._eth_pkg
        )

        """
        Data Link Layer => {
            destination MAC  -> 6 bytes
            origin MAC       -> 6 bytes
            -> EtherType     -> 2 bytes
        }
        """
        
        # Converting MAC addresses to strings
        self.dst_mac = self._mac_to_str(dst_mac)
        self.orig_mac = self._mac_to_str(orig_mac)

        # Ethertype attribute
        self.ethertype = ethertype


    def _mac_to_str(self, mac_bytes: bytes) -> str:
        """
            Name: _mac_to_str

            Descriprion: 
                Converts the MAC address expressed in bytes to
                string. So it is more human readable :D

            Args:
                -> mac_bytes [bytes]: The MAC address in bytes format.

            Returns:
                ->  [str]: The corresponding MAC address into string
                    format.
                        
        """
        mac_string = ':'.join(binascii.hexlify(mac_bytes).decode('utf-8')[i:i+2] for i in range(0, 12, 2))

        return mac_string
    
    
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


##############################################################################
##############################################################################
################################# DUMMY FUNC #################################
##############################################################################
##############################################################################


    def get_dict(self) -> dict:
        """
            Name: get_dict

            Description: 
                Given the ethernet segment by the parent class, it will
                slice all the corresponding fields and transform dest and
                orig MAC addresses to string.

            Args:
                -> None

            Returns:
                ->  self.eth_dict [dict]:
                        - keys: header field names
                        - values: header field values

        """