# Ex. 036 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado!

housevalue = float(input('Valor da casa: R$'))
salary = float(input('Sálario do comprador: R$'))
yearsOfFinancing = int(input('Quantos anos de financiamento? '))

installment = housevalue / (yearsOfFinancing * 12)

minimum = salary * 30 / 100

print(
    f'Para pagar uma casa de R${housevalue:.2f} em {yearsOfFinancing} anos a prestação será de R${installment:.2f}')

if installment <= minimum:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
