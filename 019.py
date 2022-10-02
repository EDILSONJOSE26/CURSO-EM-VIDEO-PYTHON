'''Um professor quer sortear um dos seus quatros alunos para apagar o quadro.
faça um programa que ajude ele, lendo o nome deles e escrevendo o nome dos escolhido.'''


import random
aluno_1 = input('Digite o nome do aluno: ')
aluno_2 = input('Digite o nome segundo aluno: ')
aluno_3 = input('Digite o nome terceiro aluno: ')
aluno_4 = input('Digite o nome quarto aluno: ')
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
sorteio = random.choice(lista)
print('Quem vai apagar o quadro será:',sorteio)

