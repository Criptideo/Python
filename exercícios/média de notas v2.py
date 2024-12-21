n1 = float(input('Quanto você tirou na primeira nota? '))
n2 = float(input('Quanto você tirou na segunda nota? '))
media = float((n1 + n2) / 2)
print('A média das suas notas foi: {:.0f}'.format(media))

if media >= 6.0:
    print('Você foi aprovado.')
else:
    print('Você foi reprovado.')