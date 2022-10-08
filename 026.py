''' Faça um programa que leia uma frase pelo teclado e mostre:
1º Quantas vezes aparece a letra ''A''
2º Em que posição ela aparece pela primeira vez
3º Em que posiçao ela aparece a última vez. '''

frase = str(input("Digite sua frase: ")).upper().strip()
print('A letra a aparece {} vezes'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))