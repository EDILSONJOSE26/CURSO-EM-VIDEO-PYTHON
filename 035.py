'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuario se elas podem ou não formar um triangulo.'''

r1 = float(input("Digite o primeiro segmento: "))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 < r2 + r3 and r2 > r1 + r3 and r3 < r1 + r3:
    print('Os segmentos acima PODEM formar um triangulo')
else:
    print('Os segmentos acima NÃO PODEM formar um triangulo')