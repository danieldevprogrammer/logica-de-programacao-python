# Ex. 025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
name = str(input('Qual é seu nome completo? ')).strip()

checkingName = 'SILVA' in name.upper()

print(f'Seu nome tem Silva? {checkingName}')
