# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
price = float(input('Qual é o preço do produto? R$'))
discount = price - (price * 5 / 100)

print(
    f'O produto que custava R${price:.2f}, na promoção com desconto de 5% vai custar R${discount:.2f}.')
