def ini():
    def erro(x):
        try:
            #Função que pode ser utilizada para printar valores
            eval(x)
        except (NameError, TypeError):
            print('NameError ou TypeError ocorreu!')
        except ValueError:
            print('ValueError')
        except ZeroDivisionError:
            print('ZeroDivisionError')
    erro('a')
    erro("int('a')")
    erro('5/0')
    erro('int+int') 
    erro("print(10+10)")
ini()