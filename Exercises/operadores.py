#OPERAÇÕES ARITMÉTICAS

# + ADIÇÃO
# - SUBTRAÇÃO
# * MULTIPLICAÇÃO
# / DIVISÃO
# ** POTÊNCIA
# // DIVISÃO INTEIRA (O que seria isso?)
# % RESTO DA DIVISÃO (O que seria isso?)

# 5+2 == 7
# 5-2 == 3
# 5*2 == 10
# 5/2 == 2.5
# 5**2 == 25
# 5//2 == 2 (não divide o resto)
# 5%2 == 1 (resto da divisão)

# ORDEM DE PRECEDÊNCIA

# 1 ()
# 2 **
# 3 * / // %
# 4 + -

#DESAFIO DA MATEMÁTICA FODA
#1. fazer um programa que leia um número inteiro e mostra na tela o seu sucessor e seu antecessor

N1 = int(input('Digite um número que te mostro uma mágica: '))
sucessor = N1 + 1
antecessor = N1 - 1

print('Seu sucessor é {} e seu antecessor é {}' .format(sucessor, antecessor))

