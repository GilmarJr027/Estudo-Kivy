"""
13 - Faça um algoritmo que leia um caractere e informe se o mesmo é uma vogal ou não.

"""

vogal = ['A', 'a', 'E', 'e ','I', 'i', 'O', 'o', 'U', 'u']

letra = str(input('Informe uma letra:'))

if(letra in vogal):
    print('È uma vogal')
else:
    print('não é vogal')