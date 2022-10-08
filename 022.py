'''Crie um programa que leia o nome completo de uma pessoa e mostre:
1º O nome com todas as letras maiúsculas 
2º O nome de todas minúsculas.
3º Quantas letras ao todo (sem considerar espaços).'''



nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em letras maiusculas:', nome.upper())
print('Seu nome em letras minúsculas:', nome.lower())
print('seu nome tem {} letas'.format(len(nome) - nome.count(' ')))
print('seu primeoro nome tem {} letras'.format(nome.find(' ')))

