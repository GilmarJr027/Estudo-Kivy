#Criando uma lista e declarando os seus valores
lista = [1,2,3,4,5]
print('Lista bruta: {}'.format(lista))

#Atribui um elemento a lista
lista = lista + [6]
print('Lista  + 6 = {}'.format(lista))

#Adcionando mais um elemento a minha lista no inicio
lista = [0] + lista
print('Adiconando o elemento 0 ao inicio da nossa lista = {}'.format(lista))

#Adcionando mais de um elemento a minha lista 
lista = lista + [7,8,9,10]
print('Adicionando os elementos 7, 8 , 9 , 10 a nossa lista = {}'.format(lista))

#Adcionando um elemento com a função append
lista.append(11)
print('Minha lista mais o elemento append {}'.format(lista))

#Adicionando uma sublista a uma lista 
lista.append([12])
print('Minha lista agora com uma sub-lista {}'.format(lista))

#Excluindo algum elemento de nossa lista  (no caso passado o
#Metodo -1 para determinar excluir o ultimo elemento)
del(lista[-1])
print('Minha lista agora com o ultimo elemento excluido {}'.format(lista))

#Adicionando varios elementos a nossa lista
lista += 10*[0]
print('Nossa lista com mais 10 elementos iguais\nAdicionados com metodo de Multiplicação = {}'.format(lista))

#Excluindo os elementos do 12 pra frente
del(lista[12:])
print('Minha lista formatada = {}'.format(lista))
