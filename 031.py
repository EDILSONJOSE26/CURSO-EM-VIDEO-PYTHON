'''Desenvolva um programa que pergunte a distãncia de uma viagem em Km.
calcule o preço da passagem, cobrando R$0,50 por km para viagens de até
200KM e R$0,45 para viagens mais longas'''

distancia = float(input('Digite a distancia da sua viagem em Km: '))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
    print('O preço de sa viagem é de R${:.2f}'.format(preco))