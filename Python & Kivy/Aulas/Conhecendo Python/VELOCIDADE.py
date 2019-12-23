
distancia = float(input('Informe a distancia percorrida:'))
tempo = float(input('Informe o tempo percorrido:'))

def funcao(tempo, distancia):
    funcao = distancia / tempo
    print('Sua velocidade é de {} metros por segundo'.format(funcao))

print(funcao(tempo,distancia))

