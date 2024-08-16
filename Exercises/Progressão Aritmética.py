print("PROGRESSÃO ARITMÉTICA DE 20!")

prim_termo = int(input("Primeiro termo: "))
razão = int(input("Razão da proressão: "))
PA =  prim_termo + (20-1) * razão #FÓRMULA DE UMA PROGRESSÃO ARITMÉTICA
for ababa in range(prim_termo,PA+razão,razão):
    print(f"{ababa}", end=' -> ')
print("Programa finalizado")
