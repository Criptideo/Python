from time import sleep

num = int(input('Diga-me um número: '))
sleep(0.5)
print('''Escolha uma das bases para conversão:
[ 1 ]   Converter para BINÁRIO
[ 2 ]   Converter para OCTAL
[ 3 ]   Converter para HEXADECIMAL''')
sleep(1)
escolha = int(input('Digite o escolhido: '))

if escolha == 1:
    print(f'Seu número {num} convertido para BINÁRIO é {bin(num)}')
elif escolha == 2:
    print(f'Seu número {num} convertido para OCTAL é {oct(num)}')
elif escolha == 3:
    print(f'Seu número {num} convertido para HEXADECIMAL é {hex(num)}')
else: 
    print('Inválido.')