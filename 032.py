'''Faça um programa que leia um ano qualquer e mostre se ele é BISSEXRO.'''

ano = int(input('Digite um  ano para saber se é BISSEXTO: '))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('O ano é BISSEXTO!')
else:
    print('Não é BISSEXTO!')