#converter um tipo de variável para outro tipo de variável

x = 1       #int
y = 2.0     #flaot 
z = "3"     #str
#não conseguimos fazer cálculos com strings
y = int(y) 
#mudou de float para int

print(x)
print(y) 
print(z*3)
print((float(z))*3)
#transformei a string z em float
print(float(x))