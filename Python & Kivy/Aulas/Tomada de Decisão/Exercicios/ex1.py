"""
1) Faça um algoritmo que leia um número e mostre se o mesmo é positivo, negativo ou zero.
"""
num1 = float(input('Digite um número:'))

if(num1 >= 1):
    print('O número é positivo')
if(num1 < 0):
    print('O número é negativo')
if(num1==0):
    print('O número é igual a zero')