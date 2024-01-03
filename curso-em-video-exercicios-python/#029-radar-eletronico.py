# Ex. 029 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

speed = float(input('Qual a velocidade atual do carro em Km/h? '))


if speed > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')

    trafficTicket = (speed - 80) * 7
    print(f'Você deve pagar uma multa de R${trafficTicket}')


print('Tenha um bom dia! Dirija com segurança!')
