def ini():
    num = int(input('Informe um número inteiro não negativo:'))
    if(num >= 0):
        while(True):
            num -=1
            print(num)
            if(num == 0):
                break
    else:
        print('Foi informado um valor negativo invalido {}'.format(num))
ini()

        
        
        