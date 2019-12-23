#Definição de uma lista
lista = [10,48,30]

tupla = (10,48,30)

#Objetivo é atribuir o valor a = 10 , b = 30, c = 48
def sequencia(a,b,c):
    print('A', a)
    print('B', b)
    print('C', c)

#Ordena do menor para o maior
#lista.sort()
#sequencia(*lista)

#Como a tupla é um elemento imutavel atribuimos esse elemento a uma lista
#t = [*tupla]
#Na Sequencia utilizamos o metodo sort para ordenar do menor para o maior
#t.sort()
#Agora efetuamos a exibição do nosso resultado
#sequencia(*t)

#3° Forma atraves de desempacotamento atraves de um dicionario
sequencia(**dict(zip(('a', 'c', 'b'), lista)))
