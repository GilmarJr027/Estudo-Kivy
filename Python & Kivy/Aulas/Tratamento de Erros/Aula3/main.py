def ini():
    def erro(x):
        try:
            #Função que pode ser utilizada para printar valores
            eval(x)
        except NameError:
            print('NameError')
        except ValueError:
            print('ValueError')
        except ZeroDivisionError:
            print('ZeroDivisionError')
        except TypeError:
            print('TypeError')
    erro('a')
    erro("int('a')")
    erro('5/0')
    erro('int+int') 
    erro("print(10+10)")

ini()