''''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o valor do comprador e em quantos anos ele vai pagar.
calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo séra negado.'''

v_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu sálario: '))
q_anos = float(input('Quantos anos de financiamento: '))

prestacao = v_casa / (q_anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(v_casa, q_anos))
print('A prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
