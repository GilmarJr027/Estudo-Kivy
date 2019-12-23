#Argumentos Posicionais e argumentos nomeados

#Definição da função
def dados_pessoais(nome, sobrenome, idade, sexo):
    print('Nome: {}\nSobrenome: {}\nIdade: {}\nSexo: {}'.format(nome, sobrenome, idade, sexo))
#chama a função e passa os parametros definidos no scopo da função

#Parametros posicionais

#dados_pessoais('Michael', 'De Mattos', 26, 'Masculino')

#Parametros Nomeados

dados_pessoais(sexo=True, 
                idade=26,
                sobrenome='De Mattos',
                nome='Michael')
