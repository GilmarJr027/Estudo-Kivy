class Retangulo():
    def area(self):
        return self.l * self.a

#Função externa a classe
def membros_retangulo(self):
        self.a = 0
        self.l = 0

#Instancia r1 recebe as propriedades contidas na classe Retangulo  
r1 = Retangulo()
#Ligando a função a instancia da classe
membros_retangulo(r1)
#A partir da instancia é possivel acessar as variaveis declaradas no escopo da classe  
r1.l = float(input('Digite a largura:'))
r1.a = float(input('Digite a altura:'))
#Instancia r2 recebe as propriedades contidas na classe Retangulo
r2 = Retangulo()
print(r1.area())