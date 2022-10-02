'''Escreva um programa que pergunte a quantidade de Km
percorridos por um carro alugado e a quantidade de dias pelos
quais foi alugado. calcule o preço a pagar, sabendo que o carro
custa R$60 por dia e R$0,15 por Km rodado'''

d = int(input('Digite a quantidade de dias que o veiculo foi alugado: '))
km = float(input('Digite a quantidade de Km percorridos: '))
s = (d * 60) + (km * 0.15)
print('O total  a pagar é de R${:.2f}'.format(s))
