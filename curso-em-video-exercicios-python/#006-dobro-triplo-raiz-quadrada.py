# Ex. 006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
number = int(input('Digite um número: '))

double = number * 2
triple = number * 3
sqr = number ** (1/2)
# squareRoot = pow(number, (1/2))

print(
    f'Analisando o número {number}, \no dobro é {double}, \no triplo é {triple} \ne a raiz quadrada é {sqr}')
