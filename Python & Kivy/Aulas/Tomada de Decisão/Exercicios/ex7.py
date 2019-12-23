"""
7) Faça um algoritmo que peça um número 
ao usuário e verifique se o mesmo é par ou então ímpar.
"""

num1 = float(input('Digite um número:'))

if(num1 % 2 ==0):
    print('O numero {} é par !!!'.format(num1))
else:
    print('O número {} é impar!'.format(num1))