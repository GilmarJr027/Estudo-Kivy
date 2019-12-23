#getters e setters 

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = 0
        self.altura = 0
        self.set_altura = (altura)
        self.set_largura = (largura)
    
    def set_altura(self, val1):
        if(not(isinstance(val1, float) and (val1 > 0))):
            raise ValueError('Altura invalida {}'.format(val1))
        self.altura = val1
    
    def set_largura(self, val2):
        if(not(isinstance(va2, float) and (val2 > 0))):
            raise ValueError('Largura invalida {}'.format(val2))
        self.largura = val2
    def get_area(self):
        return (self.altura * self.largura)
        

r = Retangulo(altura=10.5, largura=15.5)
