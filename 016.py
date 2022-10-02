'''crie um programa que leia um numero real qualquer pelo teclado e mostre na
tela a sua porção inteira.'''

import math
num = float(input("Digite um número: "))
s = math.trunc(num)
print('Resultado é {}'.format(s))
