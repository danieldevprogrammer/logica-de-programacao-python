# Ex. 035 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)

firstSegment = float(input('Primeiro segmento: '))
secondSegment = float(input('Segundo segmento: '))
thirdSegment = float(input('Terceiro segmento: '))

if firstSegment < secondSegment + thirdSegment and secondSegment < firstSegment + thirdSegment and thirdSegment < firstSegment + secondSegment:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
