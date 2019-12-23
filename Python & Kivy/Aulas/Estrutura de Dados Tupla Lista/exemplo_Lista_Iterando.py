#Iterando listas em Python [iterar = percorrer todos elementos]

#Criação da nossa lista
lista = [100,200,300,400,500,600,700]

#Criação de indice para acessar os valores da nossa lista
#Pode utilizar essa sintaxe
#lista_indice = [0,1,2,3]
lista_indice = range(4)

#Criação do nosso laço for, passando o 
#nome de item e passamos o parametro de lista_indece

#Pode utilizar essa sintaxe
#for item in lista_indice:
    #lista linha dizemos que cada elemento da nossa
    #lista recebe a instrução contida em item e soma 1000 a cada elemento
#ou essa sintaxe
#for item in range(4):
#
##Exista essa opção também (melhor opção)
#for item in range(len(lista)):
#    lista[item] += 1000
#

#Trabalhando com a função enumerate 
for idx, item in enumerate(lista):
    lista[idx] += 1000

print('Cada intem da nossa lista +1000 = {}'.format(lista))

