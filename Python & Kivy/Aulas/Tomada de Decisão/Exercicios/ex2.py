"""
2) Faça um algoritmo que leia um número e mostre se o mesmo é par ou ímpar.

"""

num1 = float(input('Digite um número:'))

if(num1 % 2 ==0):
    print('O numero {} é par !!!'.format(num1))
else:
    print('O número {} é impar!'.format(num1))