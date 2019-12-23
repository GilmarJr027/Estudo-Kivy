
"""

10) Faça um algoritmo que calcule o cubo e o quadrado de um
determinado número:

"""

import math

num_1 = float(input('Digite um número: '))

#portencia (quadrado)
quadrado = math.pow(num_1, 2)


#cubo
cubo = num_1 ** (1 / 3)


print('Quadrado: {} Cubo: {}'.format(quadrado, math.ceil(cubo)))




