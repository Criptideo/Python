#J9KENPO
from time import sleep
from random import randint

print('Que tal jogarmos um jogo de JOKENPO?')
sleep(1)
itens = ["PEDRA", "PAPEL", "TESOURA"]
maquina = randint(0,2)
print('''
Escolha uma opção:
[0] PEDRA
[1] PAPEL 
[2] TESOURA''')
jogador = int(input("Escreva sua opção aqui: "))
sleep(1)
print('''
A máquina escolheu {}
O jogador eacolheu {}'''.format(itens[maquina],itens[jogador]))

if maquina == jogador:
    print("Há um EMPATE")
elif maquina==0: #pedra
    if jogador==1:
        print('Voce VENCEU')
    elif jogador==2:
        print('Voce PERDEU')
    else:
        print("Inválido, tente novamente")
elif maquina==1: #papel
    if jogador==0:
        print("Voce PERDEU")
    elif jogador==2:
        print('Voce GANHOU')
    else:
        print('Inválido, tente novamente')
elif maquina==2: #tesoura
    if jogador==0:
        print("Voce GANHOU")
    elif jogador==1:
        print("Voce PERDEU")
    else:
        print("Inválido, tente novamente")
else:
    print("marca uma opção que exista caralho")

