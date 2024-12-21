a,b,c = int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')), int(input('Digite o terceiro número: '))
#verificando o menor valor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#o maior valor
maior = a
if a<b and b<c:
    maior = c
if a<c and c<b:
    maior = b
print(f'O menor valor atribuído foi: {menor}')
print(f'O maior valor atribuído foi: {maior}')


