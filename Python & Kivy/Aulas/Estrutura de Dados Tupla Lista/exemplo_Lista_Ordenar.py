#Definindo uma lista 
lista = ['Michael', 'Julio Cesar', 'Luis', 'Marco Aurelio','Julia']
print('Minha lista original {}'.format(lista))

#Invertendo a ordem de exibição dos elementos 
lista.reverse()
print('A lista invertida {}'.format(lista))

#Ordenando listas com a função sort()
lista.sort()
print('Lista ordenada de forma crescente {}'.format(lista))

#Ordenando de maneira reversa
lista.sort(reverse=True)
print('Lista ordenada de forma inversa {}'.format(lista))
