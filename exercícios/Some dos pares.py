# Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
contagem = 0
for loop in range(1,7):
    seis_numeros = (int(input("Escreva seis números que descarto os ímpares e somo todos os pares: ")))
    if seis_numeros % 2 == 0:
        soma = soma + seis_numeros # ou soma += seis_numeros
        contagem = contagem + 1 # ou contagem += seis_numeros
print(f"Você nos passou {contagem} números e a soma deles foi {soma}")
