# Ex. 033 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

number1 = int(input('Primeiro valor: '))
number2 = int(input('Segundo valor: '))
number3 = int(input('Terceiro valor: '))

# Verificando quem é menor
smaller = number1
if number2 < number1 and number2 < number3:
    smaller = number2

if number3 < number1 and number3 < number2:
    smaller = number3

# Verificando quem é o maior
bigger = number1
if number2 > number1 and number2 > number3:
    bigger = number2

if number3 > number1 and number3 > number2:
    bigger = number3


print(f'O menor valor digitado foi {smaller}')
print(f'O maior valor digitado foi {bigger}')
