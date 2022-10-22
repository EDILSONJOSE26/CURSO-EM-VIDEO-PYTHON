num = int(input('Digite um numero: '))
cont = 0
tot = 0
for i in range(1, num + 1):
    if num%i == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\n\033[mO número {} foi divisivel {} vezes'.format(num, tot))
if tot == 0:
    print('É por isso que É PRIMO')
else:
    print('É por isso ele NÃO É PRIMO!')