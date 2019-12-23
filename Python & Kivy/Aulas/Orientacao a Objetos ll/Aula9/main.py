class Bichos:
    qtd_bichos = 0

    def __init__(self):
        self.add_bicho()

    def __del__(self):
        self.del_bicho()
        if(self.qtd_bichos == 0):
            print('Todos os bichos foram mortos')
    #Estou dizendo que esse metodo de instancia deve ser nomeado para metodo de classe
    @classmethod
    def add_bicho(cls):
        cls.qtd_bichos += 1
    #Estou dizendo que esse metodo de instancia deve ser nomeado para metodo de classe
    @classmethod
    def del_bicho(cls):
        cls.qtd_bichos -= 1

    #add_bicho = classmethod(add_bicho)
    #del_bicho = classmethod(del_bicho)

b1 = Bichos()
print(Bichos.qtd_bichos)

b2 = Bichos()
print(Bichos.qtd_bichos)

b3 = Bichos()
print(Bichos.qtd_bichos)