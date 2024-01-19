# Ex. 029 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

speed = float(input('Qual a velocidade atual do carro em Km/h? '))


if speed > 80:
    print(
        '\033[31m''MULTADO! Você excedeu o limite permitido que é de 80Km/h''\033[m')

    trafficTicket = (speed - 80) * 7
    print('\033[33m'f'Você deve pagar uma multa de R${trafficTicket}')


print('\033[32m''Tenha um bom dia! Dirija com segurança!''\033[m')
