from icecream import ic

# from networkAPI.Eth import Eth
# from ..networkAPI.Eth import Eth

from networkAPI.na_importAPI import Eth, IPv4, TCP
from networkAPI.na_importAPI import ObjRepr


class NetworkProbe:
    pass

    # deberías pasarle un Publisher

    TWENTY_BYTES = 20

    def __init__(self, ts: float, pkg: bytes):

        # Declaring segment headers
        self.eth_header = None
        self.ip_header  = None
        self.tcp_header = None
        
        # Timestamp
        self.pkg_timestamp = ts

        # -------------------------------------
        
        # Extracting Eth segment
        self._eth_pkg = pkg[:Eth.HEADR_LEN]
        
        # Creating header objects (they will be atributes)
        
        # Ethernet dict:
        self.eth_header = Eth(self._eth_pkg)

        # Si no es Ipv4
        if self.eth_header.ethertype != Eth.ET_IPV4:
            return

        # Ipv4 threshold idx (Without considering options)
        ip_h_begin = Eth.HEADR_LEN
        ip_h_end   = ip_h_begin + IPv4.HEADR_LEN 

        # Getting IPv4 header
        self._ip_pkg = pkg[ip_h_begin:ip_h_end]

        # Ip header:
        self.ip_header = IPv4(self._ip_pkg)

        # Si no es TCP
        if self.ip_header.protocol != IPv4.TCP_PROTO:
            return
        
        # Getting TCP header size
        tcp_h_start = Eth.HEADR_LEN + self.ip_header.h_len_bytes
        tcp_h_end   = tcp_h_start   + TCP.HEADR_LEN

        # Getting TCP header (Without considering options)
        self._tcp_pkg = pkg[tcp_h_start:tcp_h_end]

        # TCP header:
        self.tcp_header = TCP(self._tcp_pkg)




    def get_metric():
        pass
        # usa los dicts     
        # retorna la métrica

    def _get_files():
        pass
        # Lista scripts del dir
        # Filtra los que cumplen los requisitos
        # Los importa

    def _exec_scripts():
        pass
        # Ejecuta su método estático

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



if __name__ == '__main__':
    
    np = NetworkProbe(0, bytes(14))
    ic(np.eth_dict)

