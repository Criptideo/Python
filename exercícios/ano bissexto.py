

ano = int(input('Me diga o ano que quer analisar: '))
bissexto = ano %4==0 and ano%100 != 0
bissexto = bissexto or ano %400==0
if bissexto:
    print('O ano {} escolhido é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
