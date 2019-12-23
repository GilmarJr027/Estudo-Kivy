"""
9) Faça um algoritmo que verifica se um determinado valor é um número inteiro.
"""

valor = input('Digite um número:')
valor = float(valor)


if(valor // 1 == valor):
    print('O número {} é inteiro'.format(valor))

else:
    print('O número {} é .flutuante'.format(valor))