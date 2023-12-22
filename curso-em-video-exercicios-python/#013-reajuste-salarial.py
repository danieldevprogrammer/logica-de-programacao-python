# Ex. 013 -
wage = float(input('Qual o salário do funcionário? R$'))
increase = (wage * 15 / 100)
newWage = wage + increase


print(
    f'Um funcionário que ganhava R${wage}, com 15% de aumento, passa a receber R${newWage}')
