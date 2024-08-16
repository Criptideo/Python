# Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
contagem = 0
for valor in range(1, 500 + 1, 2):
    if valor % 3 == 0:
        soma = soma + valor #acumulando os valores
        contagem = contagem +  1 #contando os valores
        print(valor," ", end="")
print('A soma dos {} valores solicitados é {}'.format(contagem,soma))
