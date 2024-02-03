velocidade = float(input('A velocidade mínima é 80km/h, digite aqui a velocidade que seu carro estava: '))
valor_da_multa = (velocidade - 80)*7
if velocidade > 80:
    print(f'Você foi multado. O valor da multa é R${valor_da_multa}.')
else:
    print('Tudo nos conformes, você não ultrapasssou a velocidade.')

