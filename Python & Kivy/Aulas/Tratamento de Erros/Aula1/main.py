try:
    a = float(input('Digite um valor para variavel A:'))
    b = float(input('Digite um valor para variavel B:'))

    divisao = (a / b)

    print('Deu Certo {:.3}'.format(divisao))
except ZeroDivisionError:
    print('Não é possivel dividir um valor por zero')

