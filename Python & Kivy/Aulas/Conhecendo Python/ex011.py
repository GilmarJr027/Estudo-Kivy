"""
11) Faça um algoritmo que solicite ao usuário digitar 2 números. Em seguida,
imprima o total decimal da divisão e o total inteiro (sem casas decimais):
"""
import math

num_1 = float(input('Digite um número:'))
num_2 = float(input('Digite outro número:'))

total_dec_divi = (num_1 % num_2)
divisao = (num_1 / num_2)

print('Resto da divisão entre {} e {} é {} e a parte inteira dessa divisão é {}'.format(num_1,num_2,total_dec_divi, math.ceil(divisao)))

