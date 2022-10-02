'''Faça um algoritimo que leia a preço de um produto e mostre seu novo preço com
5% de desconto.'''



produto = float(input('Digite o preço do produto: '))
novo_preco = produto - (produto * 5 / 100) 
print('O produto ficou por {}'.format(novo_preco))
