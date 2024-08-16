#CONDIÇÕES

tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Seu carro é novo ainda!')
else: 
    print('Vish... teu carro já é meio velho.')
print('~~~~~~~FIM~~~~~~~')

#CONDIÇÃO SIMPLIFICADA

tempo2 = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo <=3 else 'carro velho')