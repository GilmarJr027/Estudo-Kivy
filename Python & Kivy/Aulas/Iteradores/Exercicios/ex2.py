n_inicial = input('Digite o número inicial da sequencia:')
n_inicial = int(n_inicial)
n_final = input('Digite o número Final da sequencia:')
n_final = int(n_final)
intervalo = input('Informe o intervalo entre as sequencias:')
intervalo = int(intervalo)

for minha_lista in range(n_inicial, n_final, intervalo):
    print(minha_lista)