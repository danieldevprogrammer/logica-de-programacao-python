# Ex. 032 -  Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
# year = int(input('Que ano quer analsar? '))

# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(f'O ano {year} é BISSEXTO')
# else:
#     print(f'O ano {year} NÃO É BISSEXTO')

from datetime import date

year = int(input('Que ano quer analsar? Ou coloque 0 para analizar o ano atual: '))

if year == 0:
    year = date.today().year

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'O ano {year} é BISSEXTO')
else:
    print(f'O ano {year} NÃO É BISSEXTO')
