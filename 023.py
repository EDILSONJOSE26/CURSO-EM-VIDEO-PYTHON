'''faça um programa que leia um número de 0 a 9999 e mostre na tela 
cada um dos digitos separados.'''

#S failed 90%

num = int(input("Digite um numero até 9999: ").strip())
uni = num % 10
dez = num % 10
s_centena = (num - dez) / 10
centena = s_centena
milhar = 


print(""" 
Unidade = {}
Dezena = {}
Centena = {}
Milhar = {}
""".format(uni,dez,centena,milhar))