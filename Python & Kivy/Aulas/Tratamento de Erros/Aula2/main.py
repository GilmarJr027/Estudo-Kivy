def input_float(msg):
    
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print('ERRO: Valor informado invalido')

def ini():
    
    n1 = input_float('Digite o 1° número:')
    n2 = input_float('Digite o 2° número:')
    
    if(n1 == 0 or n2 == 0):
        print('Não é possivel fazer uma divisão por zero, reiniciando a aplicação!')
        del(n1, n2)
        return ini()
        
    else:
        divisao = (n1 / n2) 
        print('A divisão entre {} e {} é igual a {}'.format(n1,n2, divisao))
    
    
ini()
