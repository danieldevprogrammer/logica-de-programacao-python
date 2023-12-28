# Ex. 026 - Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

phrase = str(input('Digite uma frase: ')).strip().upper()

countLetterA = phrase.count('A')
firstTimeLetterA = phrase.find('A') + 1
lastTimeLetterA = phrase.rfind('A') + 1

print(f'A letra A aparece {countLetterA} vezes na frase.')
print(f'A primeira letra A apareceu na posição {firstTimeLetterA}.')
print(f'A última letra A apareceu na posição {lastTimeLetterA}')
