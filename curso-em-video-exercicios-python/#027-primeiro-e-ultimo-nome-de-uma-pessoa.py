# Ex. 027 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
name = str(input('Digite seu nome completo: ')).strip()

splitName = name.split()
firstName = splitName[0]
lastName = 

print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {firstName}.')
print(f'Seu último nome é {lastName}.')
