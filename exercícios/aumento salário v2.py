#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = int(input('Qual o seu salário?: '))

if salario > 1250:
    aumento = (salario * 10/100) + salario
    print(f'Seu salário passa a ser R${aumento} com o aumento de 10%')
if salario <= 1250:
    aumento = (salario * 15/100) + salario
    print(f'Seu salário passa a ser R${aumento} com aumento de 15%')
