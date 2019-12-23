def ini():

    def erro(x):

        try:
            eval(x)
        except ValueError as var:
                                #Classe     #msg Erro
            print('Erro: ', '\n',type(var), '\n',var)
        
    erro("int('a')")
   
ini()