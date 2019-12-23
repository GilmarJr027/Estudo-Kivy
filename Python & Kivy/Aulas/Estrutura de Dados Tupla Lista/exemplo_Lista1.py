#Criando uma lista padrao
lista = ([1,5,8,15,10,21])

#imprimindo a lista
print(type(lista), lista,'\n')

#Mostra uma posição da lista
print('Mostrando a posição zero da lista:',lista[0])

#exemplo de soma em uma liusta 
soma = lista[1] + lista[2]

#exibe o resultado na tela
print('Soma a posição  1 = {} + a posição 2 =  {} resulta em: =  {} '.format(lista[1], lista[2], soma))

#Outra forma de trabalhar com lista
seg_forma =  list('Python')

print('Segunta forma de se trabalhar Resultado: {}'.format(seg_forma))

#Com a virgula no final da expressão declarada ele exibe uma unico conjunto de caracteres
ter_forma = list(('Python',))

print('Terceira forma de se trabalhar Resultado: {}'.format(ter_forma))


