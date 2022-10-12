'''Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior, os dois são iguais '''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('o primeiro valor é maior')
elif n2 > n1:
    print('o segundo valor é maior')
elif n1 == n2:#ou else
    print('não existe valor maior, os dois são iguais')
