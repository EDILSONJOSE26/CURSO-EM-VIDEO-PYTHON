'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual sera a  base da conversao:'''
print('''  Digite 
1 conversão binaria
2 para conversão octal
3 para conversão hexadecimal
''')

num = int(input('Digite sua opção: '))

if num == 1:
    n1 = int(input('Digite um valor: '))
    print('O valaor foi convertido para {}'.format(bin(n1)[2:]))
elif num == 2:
    n2 = int(input('Digite um valor: '))
    print('O valor foi convertido para {}'.format(oct(n2)[2:]))
elif num == 3:
    n3 = int(input('Digite um valor: '))
    print('O valor foi convertido para {}'.format(hex(n3)[2:]))
else:
    print('Erro opçao invalida!')