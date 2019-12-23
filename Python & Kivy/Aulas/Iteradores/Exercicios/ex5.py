soma = 0
for myseq in (range(0,101,1)):
    if(myseq%2==0):
       lista = [myseq]
       soma = sum(lista)
       print(soma)