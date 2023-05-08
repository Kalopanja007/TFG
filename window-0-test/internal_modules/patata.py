from icecream import ic

class MiClase:
    atributo = None
    
    @staticmethod
    def metodo_estatico_1():
        # MiClase.atributo = "Este es el valor del atributo"
        MiClase.atributo = "Este es el valor del atributo"
    
    @staticmethod
    def metodo_estatico_2():
        # print("El valor del atributo es:", MiClase.atributo)
        ic(MiClase.atributo)


class Padre:
    pass

    def __init__(self):
        self.atr = 5
    
    def crear_p_atr(self):
        pass
        self.p_atr = 9

class Hijo(Padre):
    pass
    def __init__(self):
        super().__init__()
        
        ic(self.atr)


    def get_p_atr(self):
        return self.p_atr
class Testing:
    
    def get_var(self):
        self.initialise_var()
        return self.var

    def initialise_var(self):
        self.var = 5

if __name__ == "__main__":
    pass

    # MiClase.metodo_estatico_1()
    # MiClase.metodo_estatico_2()
    # Hijo()

    # a = Testing.get_var()
    # a = Testing().get_var()

    # ic(a)

    p = Padre()
    h = Hijo()

    p.crear_p_atr()
    ic(h.get_p_atr())



