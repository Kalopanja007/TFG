import binascii
import struct

class Eth:
    '''
        H: unsigned short -> 2 bytes [0 to 65,535]
        s: char           -> 1 byte  [-128 to 127]
        B: unsigned char  -> 1 byte  [0  to   255]
        L: unsigned long  -> 4 bytes [0 to 4,294,967,295]
        !: network (big-endian)

    '''
    HEADR_LEN = 14
    
    '''
        Data Link Layer => {
            destination MAC  -> 6 bytes
            origin MAC       -> 6 bytes
            -> EtherType     -> 2 bytes
        }
    '''
    XTRACT_FLAGS = '!6s6sH'
    
    def __init__(self, eth_pkg: bytes):
        self._eth_pkg = eth_pkg


    def get_dict(self) -> dict:
        """
            Name: get_dict

            Descriprion: 
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
        # Initialising eth_dict field key names
        eth_keys = [
            "dst_mac",
            "orig_mac",
            "ethertype"             
        ]

        # Extracting the fields of the ethernet segment
        dst_mac, orig_mac, ethertype = struct.unpack(
            Eth.XTRACT_FLAGS, self._eth_pkg
        )

        # Converting MAC addresses to strings
        dst_mac = self._mac_to_str(dst_mac)
        orig_mac = self._mac_to_str(orig_mac)

        eth_vals = [dst_mac, orig_mac, ethertype]
        
        # Creating the dictionary
        self.eth_dict = dict(zip(eth_keys, eth_vals))
        
        # Converting MAC addresses to strings
        return self.eth_dict


    def _mac_to_str(self, mac_bytes: bytes) -> str:
        """
            Name: _mac_to_str

            Descriprion: 
                Converts the MAC address expressed in bytes to
                string. So it is more human readable :D

            Args:
                -> mac_bytes [bytes]: 

            Returns:
                ->  mac_string [str]: The corresponding MAC address into string
                    format.
                        
        """
        mac_string = ':'.join(binascii.hexlify(mac_bytes).decode('utf-8')[i:i+2] for i in range(0, 12, 2))

        return mac_string
