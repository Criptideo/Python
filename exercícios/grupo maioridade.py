#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
data_atual = date.today().year
maioridade = 0
menoridade = 0 
for pessoas in range(1,7+1):
    nascimento = int(input(f"Informe o ano de nascimento da {pessoas}° pessoa: "))
    idade = data_atual - nascimento
    if idade >=18:
        maioridade = maioridade + 1
    else:
        menoridade = menoridade + 1
print(f"Você nos informou {maioridade} pessoas maiores de idade e {menoridade} pessoas menores de idade.")