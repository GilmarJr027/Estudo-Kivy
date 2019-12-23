#FUNÇÕES ANINHADAS 

#Definição de uma função 
def func():
    print('func')
    
    #Declaração de uma função dentro de outra função 
    def func_interna():
        print('func_interna')

    #Retornando a função interna
    func_interna()    



func()
