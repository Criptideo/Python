# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.
from time import sleep
print('Vou pedir para me apresentar seis números inteiros, vou somar os pares e descartar os ímpares.')
sleep(1)
soma=0
cont=0
for valor in range(1,7):
    numero = int(input('Digite seu número: '))
    if numero % 2==0:
        soma =+numero
        cont =+1
print(f'Você informou {cont} números PARES e a soma foi {soma}')