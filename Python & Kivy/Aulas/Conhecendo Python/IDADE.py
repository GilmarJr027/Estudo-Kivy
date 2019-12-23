idade = int(input('Informe a sua Idade:'))

def verifica(idade):
    if idade >=18:
        print('Você tem {} anos e portando é maior de idade'.format(idade))
    elif idade <18:
        print('Você tem {} anos e portanto é menor de idade'.format(idade))
print(verifica(idade))
