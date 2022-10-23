num = s = 0
v = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    s += num
    v += 1
print(f'A soma dos {v} foi {s}!')