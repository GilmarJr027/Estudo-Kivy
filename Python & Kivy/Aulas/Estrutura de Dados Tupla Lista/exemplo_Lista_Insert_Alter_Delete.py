#Definição da lista
lista = [0,1,2,3,4,5]
print('Lista inicial {}'.format(lista))

#Inserindo um valor no indixe 0
lista.insert(0, 'a')
print('Lista após inserir dados com a função Insert {}'.format(lista))

#Alterando valores da nossa lista 
lista[0] = 'aaa'
print('Valor do indixe zero da nossa lista alterado {}'.format(lista))

#Limpando dados da nossa lista com a função clear
lista.clear()
print('Nossa lista limpa {}'.format(lista))

#Reatribuindo o valor a nossa lista
lista = [0,1,2,3,4,5]
print('Reatribuição dos valores a lista = {}'.format(lista))

#Deletando um elemento da nossa lista com a função POP 
lista.pop()
print('Lista com o ultimo elemento excluido pela função POP {}'.format(lista))

#Deletando um elemento especifico com a função POP 
lista.pop(0)
print('Excluindo o primeiro elemento da nossa lista {}'.format(lista))

#Deletando varios elementos da nossa lista 
del(lista[2:3])
print('Resultado excluindo a partir do 2° elemento {}'.format(lista))

#Reatribuindo o valor a nossa lista
lista = [0,1,2,3,4,5]
print('Reatribuição dos valores a lista = {}'.format(lista))

#Excluindo em um determinado passo
del(lista[::2])
print('Resultado excluindo num passo de 2 em 2 {}'.format(lista))
