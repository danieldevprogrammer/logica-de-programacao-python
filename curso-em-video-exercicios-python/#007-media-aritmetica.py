# Ex. 007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
grade1 = float(input('Digete a primeira nota: '))
grade2 = float(input('Digite a segunda nota: '))

average = (grade1 + grade2) / 2

print(
    f'A média aritmédica entre as notas {grade1:.1f} e {grade2:.1f} é {average:.1f}')
