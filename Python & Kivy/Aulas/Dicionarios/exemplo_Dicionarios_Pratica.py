#Definindo um dicionario
tel = {
    '991740025': 'Michael',
    '992476079': 'De Mattos',
    '33451395': 'AAP',
    '33436205': 'Informece'
    }

#Exibe a quantidade de chaves
print(len(tel))

#Retorna o valor contido na chave informada
print(tel.get(991740025))

#Lista as chaves contidas no dicionarios
for impri in enumerate(tel):
    print(impri)

#Verifica se determinado valor esta contido no dicionario
inf_tel = input('Informe o telefone: ')
inf_tel = str(inf_tel)

if(inf_tel in tel):
    print('Esta contido!')
else:
    print('NAO esta contido"')




