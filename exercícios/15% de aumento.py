# bota um aumento de 15% no salario do ploretário

S = float(input('Me diga seu salário: R$'))
C = float(S*15/100)
aumento = float(S+C)
print('Um funcionário que fatura R${}, com 15% de aumento passa a receber R${}' .format(S, aumento))