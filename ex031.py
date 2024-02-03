x,y,z = int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')), int(input('Digite o terceiro número: '))
l = [x,z,y]
l.sort()
#o .sort() lista os números em ordem crescente
print(f'O maior número é {l[2]} e o menor é {l[0]}')