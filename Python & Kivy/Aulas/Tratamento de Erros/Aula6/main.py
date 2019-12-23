def ini():
    while True:
        try:
            n1 = float(input('Digite o 1° número:'))
            n2 = float(input('Digite o 2° número:'))
        except ValueError as erro:
            print('Erro:', '\n', 'A Aplicação será reiniciada', '\n', type(erro), '\n', erro)
        else:
            soma = (n1 + n2)
            print('A soma entre n1 {} e n2 {} é igual: {}'.format(n1, n2, soma))
            print('Finalizando a execução')
            break
ini()