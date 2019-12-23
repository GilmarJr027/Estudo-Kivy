a = 20
b = str(input('Informe um número ou letra ou simplesmente precione enter'))
def ex5(value1, value2):
    dic = {'valor_Obrigatorio':value1, 'valor_Opcional': value2}
    print('Valores informados {}'.format(dic))

ex5(a,b)