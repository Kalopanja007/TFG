import json

class ObjRepr:

    @staticmethod
    def pretty_print(obj: object) -> str | object:
        """
            Name: pretty_print

            Description: 
                Given an object, obtains all its attributes
                and filters the punlic ones. By convention, 
                public elements of a class do not start by '_'.

                Gets the dict representation of an object
                with a string format. For printing purposes.

            Args:
                -> obj: An object of any type.

            Returns:
                ->  [str]: A string with a dict representation
                    of the class.
                or
                ->  [object]: if it is not possible to create 
                    a dict it just retuns "obj"   
        """

        dictionary = ObjRepr.dict_repr(obj)

        if not isinstance(dictionary, dict):
            return dictionary

        return json.dumps(dictionary, indent=4)
    
    
    @staticmethod
    def dict_repr(obj: object) -> dict | object:
        """
            Name: dict_repr

            Description: 
                Given an object, obtains all its attributes
                and filters the punlic ones. By convention, 
                public elements of a class do not start by '_'.
                
                Calls the recursive "_dict_repr_rec" function
                and returns the dict representation of its
                public attributes.

            Args:
                -> obj: An object of any type.

            Returns:
                ->  [dict]: A dict representation
                    of the class. 
                or
                ->  [object]: if it is not possible to create 
                    a dict it just retuns "obj" 
        """

        try:
            return ObjRepr._dict_repr_rec(obj)
        except TypeError as e:
            pass
            # print(e)
            return obj
        
    def _dict_repr_rec(obj: object) -> dict:
        """
            Name: _dict_repr_rec

            Description: 
                Given an object, obtains all its attributes
                and filters the punlic ones. By convention, 
                public elements of a class do not start by '_'.

                Performs a deep dict representation of its 
                public attributes.

            Args:
                -> obj: An object of any type.

            Returns:
                ->  [dict]: A dict representation
                    of the class. 
        """
        
        d = vars(obj)

        keys = list(d.keys())

        for k in keys:
            if k.startswith('_'):
                d.pop(k)
            else:
                try:
                    d[k] = ObjRepr._dict_repr_rec(d[k])
                except TypeError as e:
                    pass

        return d


    

class Patata:

    def __init__(self, x, y):
        pass
        self.x = x
        self.y = y

def main1():
    pass
    p = Patata(3,4)

    ic(json.dumps(vars(p), indent=4))

def main2():
    pass

    # p = Patata(3,4)
    # p = 5
    p = 'a'

    str_rep = ObjRepr.pretty_print(p)

    ic(str_rep, type(str_rep))
    
    d = json.loads(str_rep)


    ic(d, type(d))

    # ic(d['x'], type(d['x']))

def main3():
    pass
    p = Patata(3,4)
    # p = 5
    # p = "Buenah tardee"
    # p = [*range(10)]

    # d = ObjRepr.dict_repr(p)
    # d = ObjRepr.pretty_print(p)
    d = ObjRepr.dict_repr(p)

    ic(d)
    ic(type(d))


if __name__ == '__main__':
    from icecream import ic, install
    install()
    # main1()
    # main2()
    main3()