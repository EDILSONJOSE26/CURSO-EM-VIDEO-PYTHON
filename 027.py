'''Faça um programa que leia o nome completo de uma pessoa,mostrando em seguida o primeiro
e o nome separado.
ex: Ana Maria de Souza
primeiro = Ana
último = Souza'''

nome = str(input("Digite seu nome: ")).strip()
n = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))