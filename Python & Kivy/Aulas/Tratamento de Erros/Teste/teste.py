def login():
    init = 0
    while(init == 0):
        init = int(input('Digite 0 para finalizar ou 1 para continuar:'))
        iniciar = init
        if(iniciar == 1):
             
             def ini():
                        try:
                            n1 = 0
                            n2 = 0
                            n1 = float(input('Digite um número:'))
                            n2 = float(input('Digite outro número:'))
                    
                        except (ValueError, TypeError):
                            print('Encontramos um problema ao somar os valores: Tipo de Valores Informados são invalidos :(')
                    
                        else:
                        
                            soma = (n1 + n2)
                            print('Soma entre {} e {} é igual a {}'.format(n1,n2, soma))
                    
                        finally:
                            pass               
        else:
            if(init == 0):
                print('Obrigado por utilizar o nosso programa :)')
                break

        ini()
login()                               