# Ex. 031 - Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, colocando R$0,50 por Km para viagens até 200Km e R$0,45 para viagens mais longas.

tripDistance = float(input('Qual é a distância da sua viagem em Km? '))
print(f'Você está prestes a começar uma viagem de {tripDistance}km')

# triplPrice = tripDistance * 0.50 if tripDistance <= 200 else tripDistance * 0.45

if tripDistance <= 200:
    triplPrice = tripDistance * 0.50
else:
    triplPrice = tripDistance * 0.45

print(f'E o preço da passagem será de R${triplPrice:.2f}')
