#Escopo Global 
num = 10
print(num)

#Definição de uma função
def func():
    #Acessando a variavel global
    global num
    #Alterando o valor da variavel global
    num = 100
    #Exibindo o valor contido na variavel 
    print(num)

#Invocando a função 
func()

#Exivindo o valor contido na variavel novamente
print(num)




