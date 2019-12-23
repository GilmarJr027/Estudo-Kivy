#Definição de lista

def pessoa(nome, sobrenome, idade):
    print(nome)
    print(sobrenome)
    print(idade)

#1° opção    
tupla = ('Michael', 'De Mattos', 25)

#2° opção
lista = ['Michael', 'De Mattos', 25]

#3° opção
dicionario = {'nome': 'Michael', 'sobrenome': 'De mattos', 'idade': 25}

#Desempacotamento manual
#pessoa(tupla[0],tupla[1],tupla[2])

#Função para fazer o desempacotamento

#1° opção
pessoa(*tupla)

#2° opção
pessoa(*lista)

#3° opção
pessoa(**dicionario)