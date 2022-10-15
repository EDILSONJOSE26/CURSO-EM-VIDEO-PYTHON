peso = float(input('Digite seu peso Kg: '))
altura = float(input('Digite sua altura: '))

imc = (peso / altura) ** 2

if imc < 18.5:
    print('IMC {:.2f} BAIXO do peso!'.format(imc))
elif imc > 18.5 or imc <= 25:
    print('IMC {:.2f} PESO IDEAL'.format(imc))
elif imc > 25 or imc <= 30:
    print('IMC {:.2f} SOBREPESO!'.format(imc))
elif imc >30 or imc <= 40:
    print('IMC {:.2f} OBESIDADE'.format(imc))
else:
    print('OBESIDADE MÓRBIDA')