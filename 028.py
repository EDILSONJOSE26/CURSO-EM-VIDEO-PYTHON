'''Escreva um programa que faça o computador ''pensar'' em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
pelo computador.

o programa deverá escrever na tela se o usuário venceu ou perdeu.'''

import random

s = random.randint(0, 5)

num = int(input('Digite o seu numero da sorte: '))
if num == s:
    print('Parabens voçe assertou!')
else:
    print('Voçe errou!')