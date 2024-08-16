# faça um programa que pergunte a quantidade de km percorrido por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

dias_alugados = float(input('Por quantos dias o carro foi alugado? '))
km_percorridos = float(input('Quantos km foram percorridos? '))
por_dia = dias_alugados * 60
por_km = km_percorridos * 0.15
total = por_dia + por_km
print(f'O preço total a ser pago pelo aluguel do carro vai ser R${total:.2f}')