# Ex. 034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salary = float(input('Qual é o salário do funcionário? R$'))

if salary <= 1250:
    Increase = salary * 0.15
    salaryIncrease = salary + Increase
    print(f'Quem ganhava R${salary:.2f} passa a ganhar R${salaryIncrease}')
else:
    Increase = salary * 0.10
    salaryIncrease = salary + Increase
    print(f'Quem ganhava R${salary:.2f} passa a ganhar R${salaryIncrease}')
