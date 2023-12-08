#Ex. 002 - Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
nome = input('Digite seu nume: ')
#print('É um prazer te conhecer',nome,'!')
print('É um prazer te conhecer {}!'.format(nome))