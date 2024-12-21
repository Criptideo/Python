# Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles

from time import sleep

for contagem in range(10, 0, -1): #-1 was really important, you can go backwards by doing this
    sleep(1)
    print(contagem)
sleep(1)
print('ATATAFIIIIILLLFIIIIILLLLFIIIIIIILLLPOOOWWWWWW🎇🎆🎇🎆🎇🎆🎇🎇🎆🎇🎆🎇🎆🎇🎆🎇PAPAPAPAPUPUPUPUPU🎉🎉🎉🎊🎊🎊🎉PAPAPUPU🎆🎇🎇🎆🎇🎆🎇🎆🎇🎇🎆🎇🎆🎇🎆🎇🎆🎇PAPAPAPAPUPUPUPUPU🎉🎉🎉🎊🎊🎊🎉PAPAPUPU🎆🎇PAPUL🎆🎇🎇🎆FIIILLLPUUUUUPOWPOWATATAFIIIIILLLFIIIIILLLLFIIIIIIILLLPOOOWWWWWW🎇🎆🎇🎆🎇🎆🎇🎇🎆🎇🎆🎇🎆🎇🎆🎇PAPAPAPAPUPUPUPUPU🎉🎉🎉🎊🎊🎊🎉PAPAPUPU🎆🎇🎇🎆🎇🎆🎇🎆🎇🎇🎆🎇🎆🎇🎆🎇🎆🎇PAPAPAPAPUPUPUPUPU🎉🎉🎉🎊🎊🎊🎉PAPAPUPU🎆🎇PAPUL🎆🎇🎇🎆FIIILLLPUUUUUPOWPOW')