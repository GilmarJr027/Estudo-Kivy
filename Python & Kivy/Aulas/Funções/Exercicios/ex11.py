def ini():
    lista = [1,2,3,4,5]
    def fim(v1,v2,v3,v4,v5):
        global lista
        soma = (v1 + v2 + v3 + v4 + v5)
        print('Soma entre [1,2,3,4,5] = {}'.format(soma))
    fim(lista[0], lista[1], lista[2], lista[3], lista[4])
ini()
