'''Faça um programa que leia trê números e mostre qual é o maior e qual é o menor.'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

maior = n1

if (n2 > maior):
    maior = n2

if (n3 > maior):
    maior = n3

print('o maior é {}'.format(maior))

menor = n1

if (n2 < menor):
    menor = n2

if (n3 < menor):
    menor = n3

print('O menor é {}'.format(menor))
