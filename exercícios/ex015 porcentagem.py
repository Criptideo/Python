#Para calcular a porcentagem de um número e calcula em X
# R$10          100%
#  X             19%
# Portanto, o cálculo a se descobrir a porcentagem é fazer:
# (10*19/100) 

print(10*19/100)

# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preço = float(input('Digite o preço a ser calculado com desconto de 5%: R$'))
porcent = float(preço*5/100)
desconto = float(preço - porcent)
print('O produto com desconto de 5% sai a: R${}' .format(desconto))
