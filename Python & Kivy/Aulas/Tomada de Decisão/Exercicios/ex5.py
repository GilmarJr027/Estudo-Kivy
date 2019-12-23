"""
5) Faça um algoritmo que peça a idade do usuário
 e a idade da sua mãe. Em seguida, imprima na tela 
 com quantos anos sua mãe o teve.
"""

idade_usuario = int(input('Informe sua idade:'))

idade_mae_usuario = int(input('Informe a idade de sua mae:'))

if(idade_mae_usuario > idade_usuario):
    idade = (idade_mae_usuario - idade_usuario)
    print('Sua mãe teve você aos {} anos'.format(idade))
else:
    if(idade_usuario > idade_mae_usuario):
        print('Erro :( você não pode ser mais velho que sua mâe')