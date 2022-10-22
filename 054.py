from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for i in range(1, 8):
    ano_nacs = int(input('EM que ano a {}ª pessoa nasceu?: '.format(i)))
    idade = atual - ano_nacs
    if idade >= 20:
        totmaior += 1
    else:
       totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E tambem tivemos {} pessoas menores de idade'.format(totmenor))