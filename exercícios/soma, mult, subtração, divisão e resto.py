n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
soma = n1 + n2
sub = n1 - n2
div = n1 / n2
div_int = n1 // n2
rest_div = n1 % n2
mult = n1 * n2
e = n1 ** n2
print('A soma vale {}, o produto é {} e a divisão é {}' .format(soma, mult, div))

print('Divisão inteira é {} e potência {}' .format(div_int, e))

print('Agora o resto da divisão é {}' .format(rest_div), end='')

