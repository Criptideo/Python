from time import sleep

print('VAMOS COMPARAR NÚMEROS')

num1 = int(input('Me diga o primeiro número: '))
num2 = int(input('Agora me diga o segundo número: '))

sleep(1)
if num1 == num2:
    print(f'O número {num1} e {num2} são IGUAIS.')
elif num1 < num2:
    print(f'O número {num1}  é MENOR QUE o número {num2}.')
elif num1 > num2:
    print(f'O número {num1} é MAIOR QUE o número {num2}.')