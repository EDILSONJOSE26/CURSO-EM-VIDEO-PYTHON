from datetime import date
atual = date.today().year
s_ano = int(input('Digite seu ano de nascimento: '))
idade = (atual - s_ano)

if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('{} Infantil '.format(idade))
elif idade <= 19:
    print('{} Junior'.format(idade))
elif idade <= 25:
    print('{} Senior'.format(idade))
elif idade > 25:
    print('{} Master'.format(idade))