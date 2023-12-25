# Ex. 016 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte Inteira 6.

from math import trunc
number = float(input('Digite um número: '))
print(f'O número {number} tem a parte interia {trunc(number)}.')

# import math
# number = float(input('Digite um número: '))
# print(f'O número {number} tem a parte interia {math.trunc(number)}.')

# number = float(input('Digite um número: '))
# print(f'O número {number} tem a parte interia {int(number)}.')
