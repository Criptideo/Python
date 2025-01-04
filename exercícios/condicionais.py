#FOR LAÇO
for loop in range(1, 5+1):
    print(loop)
print('separação interessante e necessária')
#WHILEE LAÇO
valor= int(input('Escreva algum número: '))
while valor<100:
    print(valor)
    valor += 1 
print('separação interessante e necessária')
#BREAK AND CONTINUE
for i in range(11):
    if i == 9:
        break
    print(i)
#o laço quebra quando i for igual a 9
print('separação interessante e necessária')
for i in range(11):
    if i == 9:
        continue
    print(i)
