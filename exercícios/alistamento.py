from datetime import date
from time import sleep 

ano_atual = date.today().year
nasc = int(input('Informe o seu ano de nascimento: '))
idade = ano_atual - nasc
sleep(1)
print(f'Quem nasceu em {ano_atual} tem {idade} anos.')
sleep(1)
if idade == 18:
    print(f'Você que fez {idade} anos em {ano_atual} deve se alistar IMEDIATAMENTE.')
elif idade > 18:
    print(f'Você que tem {idade} anos com certeza ja se alistou né lindo')
else:
    print(f'Você ainda tem {idade} anos, sua hora de se alistar vai chegar em {nasc+18}, vamos estar te esperando.')