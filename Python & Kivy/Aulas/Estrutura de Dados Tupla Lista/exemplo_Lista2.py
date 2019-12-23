#Listas e sublistas 
lista = [['a','b','c',],[1,2,3,],[],]
print(lista)

#Retornando a sublista desejada
print('Primeira sub lista {} Segunda sublista {} Terceira sublista {}'.format(lista[0], lista[1], lista[2]))

#Retornando um elemento de uma sublista

print('Primeira sublista {} retornando segundo elemento da mesma: {}'.format(lista[0], lista[0][1]))

#Retornando o ultimo elemento da nossa lista
print('Ultimo elemento da nossa lista {}'.format(lista[-1]))

#Retornando o ultimo primeiro elemento e o ultimo elemento de uma lista
print('Primeiro elemento: {} Ultimo elemento {} '.format(lista[0], lista[-1]))

#Contando os elementos da nossa lista com a função len
print('Total de elementos da nossa lista: {}'.format(len(lista)))

