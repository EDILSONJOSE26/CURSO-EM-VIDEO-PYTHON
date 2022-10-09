'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite. '''

velocidade_max = 80
multa = 7

vel = float(input('Digite a velocidade do veiculo: '))

velocidade_total = vel - velocidade_max
v_multa = velocidade_total * multa

if vel >= 81:
    print("Voçe foi multado!")
    print('O valor da multa é de R${:.2f}' .format(v_multa))
else:
    print(' ')