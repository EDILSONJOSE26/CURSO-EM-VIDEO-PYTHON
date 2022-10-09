'''Faça um programa que leia trê números e mostre qual é o maior e qual é o menor.'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    print('o primeiro numero é maior')
if n2 > n1 and n2 > n3:
    print('O segundo numero é maior')
if n3 > n1 and n3 > n2:
    print('O terceiro numero é maior!')
else:
    print('')