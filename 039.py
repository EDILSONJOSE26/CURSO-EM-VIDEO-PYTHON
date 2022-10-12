'''faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- se ele ainda vai se alistar ao serviço militar 
- se é a hora de se alistar .
- se já passou do tempo do alistamento'''

from datetime import date
atual = date.today().year
ano_ncs = int(input('Digite seu ano de nascimento: '))
idade = (atual - ano_ncs)
print('Quem nasceu em {} tem {} anos em {}'.format(ano_ncs, idade, atual))
if idade < 18:
    saldo = 18 -idade
    print('ainda faltam {} anos para o alistamento'.format(idade, saldo))
elif idade == 18:
    print('Voçê tem que se alistar IMEDIATAMENTE!')
elif idade > 18:
    saldo = idade - 18
    print('Voçê ja deveria ter se alistado há {} anos'.format(saldo))
