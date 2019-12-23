#criando uma classe 
class MinhaClasse:
    membro_inst = 10
    def __init__(self):
        #self.membro_inst = 10
        self.membro_cls = 0
    def func(self):
        #print('O metodo func foi invovado com sucesso!')
        print(self.membro_inst)

    def imprimi(self):
        print('-' *50)
#Criando uma instancia 
iniciar1 = MinhaClasse()

iniciar2 = MinhaClasse()
#Altera somente o valor contido na instancia da classe
iniciar2.membro_inst = 20

#1° Forma de retornar os valores
#iniciar1.func()
#iniciar2.func()

#2° Forma de exibir os valores já convertendo o resultado para string 
print('Classe pripriamente dita: ' + str(MinhaClasse.membro_inst))
print('1° Instancia: ' +str(iniciar1.membro_inst))
print('2° Instancia: ' +str(iniciar2.membro_inst))


MinhaClasse.imprimi(None)

#altera o valor dos membros em todas as instancias 
MinhaClasse.membro_inst = 500
print('Classe pripriamente dita: ' + str(MinhaClasse.membro_inst))
print('1° Instancia: ' +str(iniciar1.membro_inst))
print('2° Instancia: ' +str(iniciar2.membro_inst))


#imprimindo na saida padrao o resultado do metodo func
#iniciar.func()
