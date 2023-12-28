# Ex. 023 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
number = int(input('Informe um número: '))

print(f'Analisando o número {number}')

unit = number // 1 % 10
tens = number // 10 % 10
hundreds = number // 100 % 10
thousands = number // 1000 % 10

print(f'Unidade: {unit}')
print(f'Dezena: {tens}')
print(f'Centena: {hundreds}')
print(f'Milhar: {thousands}')
