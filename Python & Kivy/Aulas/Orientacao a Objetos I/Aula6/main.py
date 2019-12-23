class Retangulo():
    def __init__(self):
        self.a = 0
        self.l = 0

    def area(self):
        return self.l * self.a

#Instancia r1 recebe as propriedades contidas na classe Retangulo  
r1 = Retangulo()
#A partir da instancia é possivel acessar as variaveis declaradas no escopo da classe  
r1.l = float(input('Digite a largura:'))
r1.a = float(input('Digite a altura:'))
#Instancia r2 recebe as propriedades contidas na classe Retangulo
r2 = Retangulo()

print(r1.area())