# Escreva um programa que converta uma temperatura digitada em ºC para ºF

#C = float(input('Me diga um valor em celcius para converter em fahrenheit: º'))
#F = float(C*1,8)+32

#print('Com {} ºC, teremos {} ºF' .format(C, F))

C = float(input('Me diga um valor em graus Celsius (ºC): '))
F = (C * (9 / 5)) + 32
K = C + 273.15

print(f'Com {C}ºC, teremos {F}ºF e {K}ºK')
