'''Escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento
Para salários superiores a R$1.250,00, calcular um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15% '''

s = float(input('Digite o salário do funcionario: '))
if s <= 1250:
    n_salario = s + (s * 15 / 100)
else:
    n_salario = s + (s * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(s, n_salario))
