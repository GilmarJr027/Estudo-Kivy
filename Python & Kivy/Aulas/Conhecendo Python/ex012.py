"""
13) Faça um algoritmo que solicite ao usuário
informar uma quantidade de dias,
horas, minutos e segundos. Em seguida,
converta tudo para segundos:

"""

dias = int(input('Informe os Dias:'))
horas = int(input('Informe as horas:'))
minutos = int(input('Informe os minutos:'))
segundos = int(input('Informe os segundos:'))

conv_dias = dias * 86400
conv_horas = horas * 3600
conv_min = minutos * 60
conv_seg = segundos * 1

total_segundos = (conv_dias + conv_horas + conv_min + conv_seg)

print('O total em segundos conforme as informações passadas são {} segundos'.format(total_segundos))
