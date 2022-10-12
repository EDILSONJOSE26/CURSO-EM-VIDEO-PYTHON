'''faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- se ele ainda vai se alistar ao serviço militar 
- se é a hora de se alistar .
- se já passou do tempo do alistamento'''

ano_ncs = int(input('Digite seu ano de nascimento: '))

soma_a = (2022 - ano_ncs)

if soma_a < 18:
    print('idade {} ainda vai se alistar'.format(soma_a))
elif soma_a == 18:
    print('idade {} é a hora de se alistar'.format(soma_a))
elif soma_a > 18:
    print('idade {} já passou do tempo'.format(soma_a))
