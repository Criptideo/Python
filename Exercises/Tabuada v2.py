# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input('Digite um número que te mostrarei sua tabuada: '))
for multiplicador in range(1, 10+1):
    print(f'{numero} x {multiplicador:2} = {numero*multiplicador}')
