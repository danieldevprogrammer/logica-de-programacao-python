# Ex. 022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

name = str(input('Digite o seu nome completo: ')).strip()
print('Analisando seu nome...')

upperName = name.upper()
lowerName = name.lower()
nameSize = len(name) - name.count(' ')
splitName = name.split()
firstName = splitName[0]
firstNameSize = len(firstName)

print(f'Seu nome em maiúsculas é {upperName}.')
print(f'Seu nome em minúsculas é {lowerName}.')
print(f'Seu nome tem ao todo {nameSize} letras.')
print(f'Seu primeiro nome é {firstName} e ele tem {firstNameSize} letras.')
