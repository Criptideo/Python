#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Qual o valor da casa que você vai financiar? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Qauntos anos vai durar esse financiamento? '))
empréstimo = valor_casa/ (anos*12)
print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos} anos, a prestação será de R${salario}')
if empréstimo < salario*(30/100):
    print('Seu empréstimo foi aprovado!')
else:
    print('Seu empréstimo NÃO foi aprovado!')
#algo deu erradokkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk


