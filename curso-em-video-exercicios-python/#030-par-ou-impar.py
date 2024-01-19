# Ex. 030 -Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

number = int(input('\033[35m''Me diga um número qualquer: ''\033[m'))

result = number % 2

if result == 0:
    print(f'O número {number} é PAR')
else:
    print(f'O número {number} é ÍMPAR')
