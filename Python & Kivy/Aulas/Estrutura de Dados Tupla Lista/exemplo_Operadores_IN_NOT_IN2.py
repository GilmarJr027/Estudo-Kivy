#Declaração de variaveis
a = 10
b = 25
c = 60
#embutindo valores na lista 
mylist = [a,b,c]

#Entrada de informaçãoes 
#x = input('Digite um número:')
#x = int(x)
##if(x == a or x ==b or x == c):
##    print('Esta Contido!')
##else:
##    print('Não está contido!')
#if x in mylist:
#    print('O valor {} está contido na lista {}'.format(x, mylist))
#else:
#    print('O valor {} não está contido em nossa lista {}'.format(x, mylist))
cores = ['Branco', 'branco', 'BRANCO', 'Preto', 'preto', 'PRETO', 'Azul', 'azul', 'AZUL']

while True:
    cor = input('Digite um nome de uma cor , ou digite 0 para sair:')
    if (cor == '0'):
        break
    elif cor in cores:
        print('A cor {} esta contido em nossa lista de cores'.format(cor))
    else:
        print('A cor {} não esta contida em nossa lista'.format(cor))
