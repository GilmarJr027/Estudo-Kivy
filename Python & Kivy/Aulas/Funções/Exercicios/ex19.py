def ini():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #SELECIONA SOMENTE OS PARAES DE UMA LISTA
    pares = list(filter(lambda x: x%2==0, lista))
    print(pares)
ini()