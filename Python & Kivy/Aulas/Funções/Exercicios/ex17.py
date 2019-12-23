def ini():
    #Definição de uma lista padrao com números repetidos
    lista = [1,2,3,4,5,6,2,2,1,8,5,8,7]
    #Faz a remoção dos valores repetidos e já ordena de forma acrescente
    remove_repetido = sorted(set(lista))
    #Exibe os valores no console
    print(remove_repetido)
ini()