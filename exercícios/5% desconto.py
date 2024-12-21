# DESAFIO 12
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preço = float(input('Insira a quantia de dinheiro para calcular o desconto: R$'))
calculo = float((preço / 100) * 5)
desconto = float(preço - calculo)


print('O preço com desconto de 5% é: {}' .format(desconto))