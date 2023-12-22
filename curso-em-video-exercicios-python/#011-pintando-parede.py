# Ex. 011 - Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pinta-lá, sabendo que cada litro de tinta,
# pinta uma área de 2m².

width = float(input('Largura da parede em metros: '))
heigth = float(input('Altura da parede em metros: '))
area = width * heigth

litersOfPaint = area / 2

print(
    f'Sua parede tem dimensão de {width}mx{heigth}m e sua área é de {area}m².')
print(f'Para pintar essa parede, você precisará de {litersOfPaint}l de tinda.')
