"""
7) Faça um algoritmo que solicite ao usuário
informar 2 números. Em seguida, some os valores
e envie para a saídapadrão a seguinte frase:
    "A soma entre <X> e <Y> é igual <total>".
"""

num_1 = float(input('Digite um número:'))
num_2 = float(input('Digite outro número:'))

soma = num_1 + num_2

print('A soma entre {} e {} vale: {}'.format(num_1, num_2, soma))
