# Ex. 015 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

rentedDays = int(input('Quantos dias alugados? '))
kmDriven = float(input('Quantos km rodados? '))

costPerDay = rentedDays * 60
costPerKm = kmDriven * 0.15

totalPayable = costPerDay + costPerKm

print(f'O total a pagar é de R${totalPayable:.2f}')
