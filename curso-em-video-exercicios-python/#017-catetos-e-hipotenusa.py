# Ex. 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

# oppositeSide = float(input('Comprimento do cateto oposto: '))
# adjacentleg = float(input('Comprimento do cateto adjacente: '))

# hypotenuse = ((oppositeSide ** 2) + (adjacentleg ** 2)) ** (1 / 2)

# print(f'A hipotenusa vai medir {hypotenuse:.2f}')

# from math import sqrt, pow

# oppositeSide = float(input('Comprimento do cateto oposto: '))
# adjacentleg = float(input('Comprimento do cateto adjacente: '))

# hypotenuse = sqrt(pow(oppositeSide, 2) + pow(adjacentleg, 2))

# print(f'A hipotenusa vai medir {hypotenuse:.2f}')

from math import hypot

oppositeSide = float(input('Comprimento do cateto oposto: '))
adjacentleg = float(input('Comprimento do cateto adjacente: '))

hypotenuse = hypot(oppositeSide, adjacentleg)

print(f'A hipotenusa vai medir {hypotenuse:.2f}')
