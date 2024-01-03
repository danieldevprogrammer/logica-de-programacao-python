# Ex. 030 -Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

number = int(input('Me diga um número qualquer: '))

result = number % 2

if result == 0:
    print(f'O número {number} é PAR')
else:
    print(f'O número {number} é ÍMPAR')
