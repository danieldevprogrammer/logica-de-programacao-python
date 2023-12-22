# Ex. 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos Dólares ela pode comprar.
# Considere US$1.00 = R$3.27
real = float(input('Quando dinheiro você tem na carteira? R$'))

dollar = real / 3.27

print(f'Com R${real:.2f} você pode comprar US${dollar:.2f}')
