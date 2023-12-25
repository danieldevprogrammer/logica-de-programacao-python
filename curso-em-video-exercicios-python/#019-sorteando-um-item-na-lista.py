# Ex. 019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice

firstStudent = str(input('Primeiro aluno: '))
secondStudent = str(input('Segundo aluno: '))
thirdStudent = str(input('Terceiro aluno: '))
fourthStudent = str(input('Quarto aluno: '))

listStudents = [firstStudent, secondStudent, thirdStudent, fourthStudent]

chosenStudent = choice(listStudents)

print(f'O aluno escolhido foi: {chosenStudent}')
