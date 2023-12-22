# Ex. 013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
wage = float(input('Qual o salário do funcionário? R$'))

increase = wage * 15 / 100

newWage = wage + increase


print(
    f'Um funcionário que ganhava R${wage:.2f}, com 15% de aumento, passa a receber R${newWage:.2f}')
