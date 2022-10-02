'''Faça um programa que leia o comprimento do cateto oposto e do catedo adjacente
de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.'''#s: FA


co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
