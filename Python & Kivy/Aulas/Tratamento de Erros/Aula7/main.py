import importlib

def ini():
    while True:
        try:
            n1 = float(input('Digite o 1° número:'))
            n2 = float(input('Digite o 2° número:'))
        except ValueError as erro:
            print('Erro:', '\n', 'A Aplicação será reiniciada', '\n', type(erro), '\n', erro)
            #Caso a exeção do erro for levantada será reiniciada a função
            return ini()
            
        else:
            soma = (n1 + n2)
            print('A soma entre n1 {} e n2 {} é igual: {}'.format(n1, n2, soma))
        
        finally:
            #a = ('Finalizando a execução do programa!')
            #print(a)
            break
ini()