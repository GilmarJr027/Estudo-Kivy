def func1(a=10, b=15):

    print('Valor de A {}\nValor de B {}'.format(a,b))

    def func2(v1,v2):
       soma = (v1 + v2)
       print('Soma entre A + B = {}'.format(soma))
    func2(a ,b)
func1()