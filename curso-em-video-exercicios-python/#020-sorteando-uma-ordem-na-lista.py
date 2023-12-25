# Ex. 020 - O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
from random import shuffle

firstStudent = str(input('Primeiro aluno: '))
secondStudent = str(input('Segundo aluno: '))
thirdStudent = str(input('Terceiro aluno: '))
fourthStudent = str(input('Quarto aluno: '))

listStudents = [firstStudent, secondStudent, thirdStudent, fourthStudent]

# random.shuffle(listStudents)
shuffle(listStudents)

print(f'A ordem de apresentação será: \n{listStudents}')
