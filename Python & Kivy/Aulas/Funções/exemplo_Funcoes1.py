#Retorno de multiplos valores

#Definição de função
#def func():
#    return 1 , 2

#Declaração de variaveis e empacotamento de valores da função func
#a , b  = func()

#Exibição dos valores
#print('\n',a,'\n',b)

def potencia(x):
    quadrado = x**2
    cubo = x**3
    return quadrado, cubo
q , c = potencia(10)
print('\n',q,'\n',c)