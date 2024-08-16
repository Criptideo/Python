print('==========LOJINHA==========')
preço = float(int(input('Valor da compra: R$')))
print('''
FORMAS DE PAGAMENTO
[1] à vista com dinheiro ou pix
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual opção prefere? '))

if opção == 1:
    valor = preço - (preço * 10/100) 
    print(f'''
Sua compra à vista no dinheiro ou pix recebe 10% de desconto!
O valor cobrado será R${valor:.2f}.''')
elif opção == 2:
    valor = preço - (preço * 5/100)
    print(f'''
Sua compra à vista no cartão recebe um desconto de 5%!
O valor cobrado será R${valor:.2f}.''')
elif opção == 3:
    print(f'''
Sua compra será realizada, o valor cobrado é de R${preço:.2f}''')
elif opção == 4:
#achei 20% de juros dinheiro demais, então deixei os juros de 12% mesmo
    valor = preço + (preço * 12/100)
    print(f'''
Sua compra terá uma taxa de juros de 12%.
O valor cobrado será de R${valor:.2f}''')
else: 
    print('Inválido, tente novamente.')