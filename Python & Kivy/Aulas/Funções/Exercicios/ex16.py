def ini():
    texto = str(input('Entre com qualquer texto que não contenha números:'))
    if(texto != ''):
        conta_carac = len(texto)
        print('Quantidade de caracteres {}'.format(conta_carac))
ini()
