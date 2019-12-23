#Definição de função

#O * significa para o python que iremos passar uma lista de argumentos
def lista_de_parametros(*lista): #utilizado como padrao (*args)
    print(lista)
#Envocamos a função e passamos os parametros a serem exibidos
lista_de_parametros(1,2,3,4,5,6)

def lista_de_parametros_associativos(**dicionarios): #utilizado como padrao (**kwargs)
    print(dicionarios)

lista_de_parametros_associativos(a=1, b=2,c='Michael',d='De Mattos')
