#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

# passei tempo quebrando a cabeça e não dei conta de fazer sozinha :(
# vou ver o raciocínio
minimo = 0
maximo = 0
for pessoas in range(1,6):
    peso = float(input(f'\tInforme o peso da {pessoas}° pessoa:'))
#faltou armazenar o valor
    if pessoas == 1:
        minimo = peso
        maximo = peso
    else:
        if peso > maximo:
            maximo = peso
        if peso < minimo:
            minimo = peso
print("\n\tO maior peso lido foi de {}kg".format(maximo))
print("\n\tO menor peso lido foi de {}kg".format(minimo))
