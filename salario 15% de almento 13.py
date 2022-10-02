'''Faça um algoritmo que leia o sálario de um funcionario e mostre seu
novo sálario, com 15% de almento.'''

salario = float(input('Digite seu salário: '))
aumento = salario + (salario*15/100)
print('seu salario com 15% de aumento é {:.2f}'.format(aumento))
