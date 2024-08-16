# DESAFIO 11
# Faça um programa que leia a largura e a altura de uma parede em metros 
# depois, calcule a seu área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2m².

#em float
largura = float(input('Qual a largura da parede (em metros)? '))
altura = float(input('Qual a altura da parede (em metros)? '))
area = largura*altura
qnt_tinta = area/2

print('Considerando que a parede tem {} de largura e {} de altura, terá {}m² de área.' .format(largura, altura, area))
print('Para preencher a área, será necessário {} litros de tinta.' .format(qnt_tinta))