from icecream import ic

# from networkAPI.Eth import Eth
# from ..networkAPI.Eth import Eth

from networkAPI.na_importAPI import Eth


class NetworkProbe:
    pass

    # deberías pasarle un Publisher

    def __init__(self, ts: float, pkg: bytes):

        
        self._eth_pkg = pkg[0:Eth.HEADR_LEN]
        self.pkg_timestamp = ts
        # crea los dicts (serán atributos)
        
        # Ethernet dict:
        self.eth_dict = Eth(self._eth_pkg).get_dict()


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



if __name__ == '__main__':
    
    np = NetworkProbe(0, bytes(14))
    ic(np.eth_dict)

