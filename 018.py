'''Faça um programa que leia um ângulo qualquer e mostre na tela
o valor do seno, cosseno e tangente desse ângulo.'''

import math
num = float(input('Digite o angulo: '))
seno = math.sin(math.radians(num))
cosseno = math.cos(math.radians(num))
tangente = math.tan(math.radians(num))
print('O seno é {:.2f}'.format(seno))
print('O cosseno é {:.2f}'.format(cosseno))
print('A tangente é {:.2f}'.format(tangente))
