# Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input("Diga um número inteiro aqui: "))
tot = 0
for ababa in range(1,numero+1):
    if numero % ababa == 0:
        print("\033[34m", end="")
        tot = tot + 1
    else:
        print("\033[31m", end="")
    print(f'{ababa}', ababa, end='')
print(tot)