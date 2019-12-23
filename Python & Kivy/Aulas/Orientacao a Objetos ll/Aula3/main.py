#getters e setters 

class Retangulo:
    def __init__(self, largura, altura):
        self._largura = 0
        self._altura = 0
        self.set_altura = (altura)
        self.set_largura = (largura)
    
    def set_altura(self, val1):
        if(not(isinstance(val1, float) and (val1 > 0))):
            raise ValueError('Altura invalida {}'.format(val1))
        self._altura = val1
    
    def set_largura(self, val2):
        if(not(isinstance(va2, float) and (val2 > 0))):
            raise ValueError('Largura invalida {}'.format(val2))
        self._largura = val2
    def get_area(self):
        return (self._altura * self._largura)
        
r = Retangulo(altura=10.5, largura=15.5)
        
r = Retangulo(altura=10.5, largura=15.5)

