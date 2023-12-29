# Ex. 028 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

player = int(input('Em que número eu pensei? '))  # Jogador tenta adivinhar

print('PROCESSANDO...')
sleep(3)

computerNumber = randint(0, 5)  # Faz o computador "PENSAR"

if computerNumber == player:
    print(
        f'PARABÉNS! Você conseguiu me vencer, eu pensei no número {computerNumber}!')
else:
    print(f'GANHEI! Eu pensei no número {computerNumber} e não no {player} !')
