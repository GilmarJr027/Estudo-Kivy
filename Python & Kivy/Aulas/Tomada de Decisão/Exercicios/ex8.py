"""
8) Faça um algoritmo que peça dois números. 
Primeiro, imprima o maior e, em seguida, o menor.
"""


num1 = float(input('Digite um número:'))
num2 = float(input('Digite outro número:'))

if(num1 > num2):
    print('O número {} é maior que o número {}'.format(num1, num2))
else:
    if(num2 > num1): 
        print('O número {} é maior que o número {}'.format(num2, num1))

