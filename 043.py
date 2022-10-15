'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''


peso = float(input('Digite seu peso Kg: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('IMC {:.1f} BAIXO do peso!'.format(imc))
elif 18.5 <= imc < 35:
    print('IMC {:.1f} PESO IDEAL'.format(imc))
elif 25 <= imc <30:
    print('IMC {:.1f} SOBREPESO!'.format(imc))
elif 30  <= imc < 40:
    print('IMC {:.1f} OBESIDADE'.format(imc))
elif imc >= 40:
    print('OBESIDADE MÓRBIDA')
    