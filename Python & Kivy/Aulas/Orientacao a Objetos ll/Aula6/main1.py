#Propriedades III

class Retangulo:
    def __init__(self, largura, altura):
        self._largura = 0
        self._altura = 0
        self.set_altura = altura
        self.set_largura = largura
    @property
    def altura(self):
        return self._altura
    @altura.setter
    def altura(self, val1):
        if(not(isinstance(val1, float) and (val1 > 0))):
            raise ValueError('Altura invalida {}'.format(val1))
        self._altura = val1
    @property
    def largura(self):
        return self._largura
    @largura.setter
    def largura(self, val2):
        if(not(isinstance(val2, float) and (val2 > 0))):
            raise ValueError('Largura invalida {}'.format(val2))
        self._largura = val2
    @property
    def area(self):
        return (self._altura * self._largura)
    
    #altura = property(fset=_set_altura, fget=_get_altura)
    #largura = property(fset=_set_largura, fget=_get_largura)
    #area = property(fget=_get_area)
        
inf_altura = float(input('Informe a altura:'))
inf_largura = float(input('Informe a largura:'))

r = Retangulo(largura=None, altura=None)

r.altura = inf_altura
r.largura = inf_largura

#r.altura = 10.00
#r.largura = 15.00

print('Altura:',r.altura)
print('Largura:',r.largura)
#
print('Area:',r.area)