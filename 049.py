from time import sleep
num = int(input('Digite um número de 1 a 10 para ver sua tabuada: '))
for c in range(1, 11):
    print( '{} x {:2} = {}'.format(num, c, num*c))
    sleep(0.5)
print('FIM')

