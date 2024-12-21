import random
from time import sleep

print('Nesse algoritmo ocorre uma interação aleatória de um número de 0 a 5. Vamos ver se você tá com sorte.')
num = int(input('Diga um número entre 0 e 5 para ver se condiz com o da máquina: '))
aleatorio = random.randrange(0,6)
print('PROCESSANDO...')
sleep(1)
if num == aleatorio:
    print('Parabéns, você acertou o número da máquina!')
else:
    print('Que azar, você perdeu o jogo.')
print(f'O número da máquina foi: {aleatorio}')