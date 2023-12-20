# Ex. 005 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
number1 = int(input('Digite um número: '))

predecessor = number1 - 1
successor = number1 + 1

print(
    f'Analisando o número {number1}, o seu antecessor é {predecessor} e o seu sucessor é {successor}')
