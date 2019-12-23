núm = 100
núm = int(núm)

for lista in range(1, núm + 1):
    if(lista%2==0):
        pass
        print('\033[34m', end='')
    else:
        print('\033[33m', end='')
  
    print('{}'.format(lista), end='')
print('\nOs números listados em amarelo são primos')