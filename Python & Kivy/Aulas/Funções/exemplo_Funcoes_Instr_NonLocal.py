#Definição de uma função 
def func1():
    var_local = 10
    print('10 - 0 = ', var_local)

    #Definição de uma função aninhada
    def func2():
        #Dessa forma eu consigo acessar a variavel que esta definida no corpo da fimção func1
        nonlocal var_local
        var_local += 1
        print('10 + 1 = ', var_local)
    func2()

func1()

#Definição de uma variavel global 
x = 100

#Definição de uma função
def func_global():
    #Acesso a uma variavel global 
    global x 
    print(x)

func_global()

