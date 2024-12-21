#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
#depois optimize esse código

import datetime
ano_atual = datetime.date.today().year #importando o ano atual da biblioteca 
maior = 0 #vari de acumulação de quem é maior
menor = 0 #vari de acumulação de quem é menor
for pessoas in range (1, 7+1): #loop pessoas 7 vezes
    ano_nasc = int(input("Informe o ano de nascimento da {}° pessoa: ".format(pessoas)))
    idade = ano_atual - ano_nasc >= 18 #calcula a idade 
    if idade: #maior de idade
        maior += 1
    else:
        menor += 1 #menor de idade
print(f"\nVocê informou que {maior} pessoas são maiores de idade e que {menor} pessoas são menores de idade.")
