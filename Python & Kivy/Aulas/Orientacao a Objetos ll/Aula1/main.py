#Codigo sucetivel a falha
class Retangulo():
   
    def __init__(self, largura, altura):
        self.l = largura
        self.a = altura
  
    def area(self):
        return self.l * self.a

r1 = Retangulo(10,10)
r1.l = 'teste'
print(r1.area())
