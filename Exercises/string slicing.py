#sting slicing 
#       indexing[] or slice()
#       [start:stop:step] 

nome = 'Miles Lagnar'
primeiro_nome = nome[0:6]
sobrenome = nome[6:]
nome_funny = nome[::2]
reverso = nome[::-1]



print(primeiro_nome)
print(sobrenome)
print(nome_funny)
print(reverso)

#now, slice()

website = "http://google.com"
slice = slice(7,-4)

print(website[slice])

