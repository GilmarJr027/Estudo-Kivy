class Retangulo():
    #declaracao dos parametros no escopo da funcao 
    def __init__(self, largura, altura):
        self.l = largura
        self.a = altura
    #declaracao da funcao que pratica o calculo da area
    def area(self):
        return self.l * self.a
#atribui a instancia r a classe retangulo (em seguida é passado os parametros da função __init__)
r = Retangulo(10,20)
#Exibe o resultado na saida padrao (console)
print(r.area())
