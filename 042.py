r1 = float(input("Digite o primeiro segmento: "))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 == r2 or r1 == r3:
    print('Equilátero')
elif r1 == r2 or r1 == r3 or r3 == r2:
    print('isósceles')
else:
    print('Escaleno')
