'''Crie um programa que leia quanto dinhero uma pessoa tem na carteira e mostara
quantos Dólar ela pode comprar.  Consider US$ 1,00 = R$3,27'''


carteira = float(input('Digite a quantidade de dinhero que tem na sua carteira: '))
considerar = carteira / 5.41
print('voçé pode comprar US${:.2f}!'.format(considerar))

