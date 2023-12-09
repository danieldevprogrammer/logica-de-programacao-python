# Ex. 004 - Faça um programa que leia algo pelo teclado e mostra na tela o seu tipo primitivo e todas as informações possiveis sobre ela.
a = print('Digite algo: ')

print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços?', a.isspace())
print('É número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumérico?', a.alphanum())
print('Está em maiúsculas?', a.isupper())
print('Está em minúscula?', a.islower())
print('está capitalizada?', a.istitle())
