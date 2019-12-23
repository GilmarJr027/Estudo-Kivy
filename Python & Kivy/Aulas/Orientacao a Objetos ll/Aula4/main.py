#Propriedades

class A:
    
    def __init__(self):
        self._var = 0

    def _get_var(self):
        print('Valor esta sendo Lido!')
        return self._var
      
    
    def _set_var(self,val1):
        print('O valor esta sendo escrito!')
        self._var = val1
    
    #Criando as propriedades de acesso as informações
    var = property(fget=_get_var, fset=_set_var)

#Exige que o usuario passe o valor para ser computado
capta = float(input('Digite um valor:'))
#criamos uma nova instancia 
a = A()
#a.var = (250)
#print(a.var)
#Atribuimos o set de var ao input capta que criamos externamente
a.var = capta
#Por fim exibimos os resultados na saida padrao
print(a.var)
