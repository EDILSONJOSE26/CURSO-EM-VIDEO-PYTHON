from datetime import date
atual = date.today().year
s_ano = int(input('Digite seu ano de nascimento: '))
idade = (atual - s_ano)

if idade <= 9:
    print('Mirim')
elif idade >= 10 and idade <= 14:
    print('{} Ifantil '.format(idade))
elif idade >= 15 and idade <= 19:
    print('{} Junior'.format(idade))
elif idade >= 20 and idade <= 20:
    print('{} Senior'.format(idade))
elif idade > 20:
    print('{} Mestre'.format(idade))