"""
3) Faça um algoritmo que solicite o nome e a idade do
usuário e então, envie a seguinte frase para o Console:
"O seu nome é <nome> e a sua idade é <idade>".
"""

nome = input('Qual é seu nome:')
idade = input('Qual é sua idade:')

print('Olá {} você tem {} anos!'.format(nome, idade))
