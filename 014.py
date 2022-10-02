'''escreva um programa que converta uma temperarura digitada
em ºC e converta para ºF.'''


graus_c = float(input('Digete a temperatura em graus celsius: '))
conv_f = (graus_c * 9/5) + 32
print('A temperatura em Fahrenheit é {:.0f}ºF'.format(conv_f))
