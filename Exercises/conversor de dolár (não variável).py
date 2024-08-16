# DESAFIO 010
# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# considere: US$1,00 = R$3,27

real = float(input('Quantos reais você tem? '))
dollar = float(real/3.27)

print('Então você tem:')
print(dollar)