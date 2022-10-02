'''O mesmo professor do desafio anterior quer sortear a ordem das apresentação
de trabalhos dos alunos.Faça um programa que leia o nome dos quato alunos e mostre
a ordem sorteada.'''


import random
aluno_1 = input('Digite o nome do aluno: ')
aluno_2 = input('Digite o nome segundo aluno: ')
aluno_3 = input('Digite o nome terceiro aluno: ')
aluno_4 = input('Digite o nome quarto aluno: ')
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
sorteio = random.sample(lista, k=4)
print('A ordem sorteada foi:',sorteio)
