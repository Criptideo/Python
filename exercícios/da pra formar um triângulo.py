from time import sleep
sleep(1)
print('Olá, eu sou um analisador de segmentos para ver se eles podem formar um triângulo ou não')
sleep(1)
segm1 = float(input('Vamos ao primeiro segmento: '))
segm2 = float(input('Vamos ao segundo segmento: '))
segm3 = float(input('Vamos ao terceiro segmento: '))

if segm1+segm2>segm3 and segm3+segm1>segm2 and segm2+segm3>segm1:
    print('Esses valores são capazes de formar um triângulo')
    if segm1 == segm2 and segm2 == segm3:
        print('Pelos segmentos serem iguais, seu triângulo é EQUILÁTERO.')
    elif segm1 == segm2

else: 
    print('Esses valores não são capazes de formar um triâgulo')
