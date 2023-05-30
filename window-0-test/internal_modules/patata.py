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


class C:
    
    def __init__(self, x, _y):
        self.x = x
        self._y = _y

    def __repr__(self) -> str:
        pass
        return "patata"
        


def main1():
    pass
    MiClase.metodo_estatico_1()
    MiClase.metodo_estatico_2()
    Hijo()

    a = Testing.get_var()
    a = Testing().get_var()

    ic(a)

def main2():
    pass
    p = Padre()
    h = Hijo()

    p.crear_p_atr()
    ic(h.get_p_atr())


def main3():
    pass
    args = [1,2]

    c = C(*args)

    ic(vars(c))
    
    # print(vars(c))


def main4():
    pass
    # Python program to understand about locals
    # here no local variable is present

    def demo1():
        print("Here no local variable is present : ", locals())

    # here local variables are present
    def demo2():
        name = "Ankit"
        print("Here local variables are present : ", locals())
        print("Before updating name is : ", name)

        # trying to change name value
        locals()['name'] = "Sri Ram"

        print("after updating name is : ", name)
        print(f"Finally locals -> {globals()}")

    # driver code
    demo1()
    demo2()


def main5():
    pass
    # Python3 program to demonstrate global() function

    # global variable
    a = 5

    def func():
        c = 10
        d = c + a
        
        # Calling globals()
        globals()['a'] = d
        ic(a)
        ic(d)
        ic(globals())
        
    # Driver Code
    func()

    ic(a)
    ic(globals()['a'])

def main6():
    pass
    k = ['a', '_b', 'c', '_d']
    v = [*range(4)]
    
    d = dict(zip(k,v))

    ic(d)

    l = list(d.items())

    for k in [*d.keys()]:
        if k.startswith('_'):
            d.pop(k)

    ic(d)


if __name__ == "__main__":
    pass
    # main1()
    # main2()
    # main3()
    # main4()
    # main5()
    main6()


