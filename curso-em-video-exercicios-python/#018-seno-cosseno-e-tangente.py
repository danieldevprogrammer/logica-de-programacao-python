# Ex. 018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# import math

# angle = float(input('Digite o ângulo que você deseja: '))

# sin = math.sin(math.radians(angle))
# cos = math.cos(math.radians(angle))
# tan = math.tan(math.radians(angle))

# print(f'O ângulo de {angle} tem o SENO de {sin:.2f}')
# print(f'O ângulo de {angle} tem o COSSENO de {cos:.2f}')
# print(f'O ângulo de {angle} tem o TANGENTE de {tan:.2f}')

from math import sin, cos, tan, radians

angle = float(input('Digite o ângulo que você deseja: '))

sin = sin(radians(angle))
cos = cos(radians(angle))
tan = tan(radians(angle))

print(f'O ângulo de {angle} tem o SENO de {sin:.2f}')
print(f'O ângulo de {angle} tem o COSSENO de {cos:.2f}')
print(f'O ângulo de {angle} tem o TANGENTE de {tan:.2f}')
