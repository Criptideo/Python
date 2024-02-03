# NÚMERO PAR OU ÍMPAR
from time import sleep

print('Vamos ver se o seu número é par ou ímpar')
sleep(1)
numero = int(input('Me diga um número qualquer para a análise: '))
resulução = numero % 2
sleep(1)
#todo número par vai dar resultado 0, agora todo número ímpar vai sobrar um
if resulução == 0:
    print(f'O número {numero} é par!')
else:
    print(f'O número {numero} é ímpar!')
