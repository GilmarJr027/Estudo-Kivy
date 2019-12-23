def ini():
    n1 = int(input('Digite um número:'))
    n2 = int(input('Digite outro número:'))
    n3 = int(input('Digite mais um número:'))
    def fim(val1,val2,val3):
        minha_lista = [val1, val2, val3]
        minha_lista.sort()
        print('Maior número informado: {}'.format(minha_lista[-1]))
    fim(n1, n2, n3)
ini()
