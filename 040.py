'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a média atingida:
- média abaixo de 5.0: REPROVADO
- media entre 5.0 e 6.9: RECUPERAÇÃO
- média 7.0 ou superior : APROVADO  '''

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))

s = (nota_1 + nota_2) / 2

if s < 5:
    print('Sua media é {} voçê está REPROVADO!'.format(s))
elif s != 5 or s != 6.9:
    print('Sua media é {} voçê esta de RECUPERAÇÃO!'.format(s))
elif s < 7:
    print('PARABENS VOÇÊ ESTA APROVADO SUA MEDIA É {}'.format(s))