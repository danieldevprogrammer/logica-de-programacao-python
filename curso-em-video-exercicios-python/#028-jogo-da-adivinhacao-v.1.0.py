# Ex. 028 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

print('\033[33m''-=-''\033[m' * 20)
print('\033[36m''Vou pensar em um número entre 0 e 5. Tente adivinhar...''\033[m')
print('\033[33m''-=-''\033[m' * 20)

player = int(input('Em que número eu pensei? '))  # Jogador tenta adivinhar

print('\033[34m''PROCESSANDO...''\033[m')
sleep(3)

computerNumber = randint(0, 5)  # Faz o computador "PENSAR"

if computerNumber == player:
    print(
        '\033[32m'f'PARABÉNS! Você conseguiu me vencer, eu pensei no número {computerNumber}!''\033[m')
else:
    print(
        '\033[31m'f'GANHEI! Eu pensei no número {computerNumber} e não no {player} !''\033[m')
