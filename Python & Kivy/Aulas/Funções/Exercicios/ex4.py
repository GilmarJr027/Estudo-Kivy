a = 10 
b = 55 
c = 12

def ex4(val1, val2 ,val3):
    lista = [val1, val2 ,val3]
    lista.sort()
    media = (val1 +  val2 + val3) / 3

    print('Lista organizada {}'.format(lista))
    print('A media dos valores passados é {}'.format(media))

ex4(a,b,c)
