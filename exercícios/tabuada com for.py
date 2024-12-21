from time import sleep
numero = int(input('Digite um número para saber sua tabuada: '))
for multiplicação in range(1,11):
    sleep(0.5)
    print(f'{numero} x {multiplicação:2} = {numero*multiplicação}')

