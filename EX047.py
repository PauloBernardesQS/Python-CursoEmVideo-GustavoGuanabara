s = 0
contador = 0
print("SOMA DOS NUMEROS ENTRE 1 E 500, IMPARES, MULTIPLOS DE 3: ")
for c in range (1, 501):
    if c%2 == 1 and c%3 == 0:
        contador = contador + 1
        s = s+c
print(s)
print(f"Numero de numeros contados: {contador}")
