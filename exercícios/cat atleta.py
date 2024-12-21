from datetime import date
from time import sleep

print('A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade.')
sleep(1)
ano_atual = date.today().year
nascimento = int(input('Informe o seu ano de nascimento: '))
idade = ano_atual - nascimento

if idade <= 9:
    print(f'''
O atleta tem {idade} anos.
Classifição: MIRIM''')
elif 9 < idade < 15:
    print(f'''
O atleta tem {idade} anos.
Classifição: INFANTIL''')
elif 14 < idade <= 19:
    print(f'''
O atleta tem {idade} anos.
Classificação: JÚNIOR''')
elif 19 < idade <= 25:
    print(f'''
O atleta tem {idade} anos.
Classificação: SÊNIOR''')
elif idade > 25:
    print(f'''
O atleta tem {idade} anos.
Classificação: JÚNIOR''')