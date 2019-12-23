#Propriedades Decorators

class A:
    def __init__(self):
        self._x = 0
    #Define o metodo getters com o decorator
    @property
    def x(self):
        print('O valor esta sendo lido!')
        return self._x 
    #Define o metodo setter com o decorator
    @x.setter
    def x(self, val1):
        print('O valor esta sendo escrito!')
        self._x = val1

capta = float(input('Informe um valor:'))
a = A()
a.x = capta
print(a.x)
#a.x = 10
#print(a.x)