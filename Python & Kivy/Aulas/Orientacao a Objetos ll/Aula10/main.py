#Metodo estatico
class MEstatico:
    @staticmethod
    def func1():
        print('Func1()')
    @staticmethod
    def func2(x,y):
        print('Func2() {} , {} '.format(x,y))
    @staticmethod
    def func3(a,b,c):
        info = """
        Nome da função: = {nome}
        Quantidade de args: = {quantidade}
        Args: {args}
        """
        info = info.format(
            nome = MEstatico.func3.__name__,
            quantidade = MEstatico.func3.__code__.co_argcount,
            args= MEstatico.func3.__code__.co_varnames
        )
        print(info)
    #func1 = staticmethod(func1)
    #func2 = staticmethod(func2)
    #func3 = staticmethod(func3)
#Instancia de metodo estatico
me = MEstatico()
me.func1()
me.func2(100,200)
me.func3(12,22,33)
print('-----------')
#MEstatico.func1()

