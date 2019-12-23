from pprint import pprint
#Criação de classe 
class App:
    
    def __init__(self):
        self.a = 15
        print(self.a)

    @property
    def valor_init(self):
        print(self.a + 1)
        return self.a

#Instanciando a classe 
init_class = App()
#retornando valor contido no metodo inicializador
init_class.a
#retornando valor contido na propriedade decorator
init_class.valor_init
#Obtenco o valor contido em um objeto dentro da instancia da nossa classe
#print(type(init_class.a), init_class.a)
#pprint(init_class.valor_init)
