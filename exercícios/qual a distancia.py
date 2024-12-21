import time
distancia = float(input('Qual a distância da sua viagem em km?: '))
viagem1 = distancia * 0.5
viagem2 = distancia * 0.45
time.sleep(1)
if distancia <= 200:
    print(f'A viagem de {distancia}km vai ficar R${viagem1}.')
else:
    print(f'Passando dos 200 km você ganha uma promoção, sua viagem ficou a R${viagem2}.')
