"""

11) Faça um algoritmo que verifica se um determinado valor é do tipo decimal.

"""

valor = input('Digite um número:')
valor = float(valor)


if(valor // 1 == valor):
    print('O número {} é inteiro'.format(valor))

else:
    print('O número {} é .flutuante'.format(valor))