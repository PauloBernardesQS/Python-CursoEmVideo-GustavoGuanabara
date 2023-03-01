matriz = [[0,0,0], [0,0,0], [0,0,0]]
par = soma = 0
slinha = []
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um numero para a linha {l} coluna {c} -> "))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if c == 2:
            soma += matriz[l][c]
        if l == 1:
            slinha.append(matriz[l][c])

for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]}] ", end="")
    print()

print(f"A soma de todos numeros pares é igual a {par}")
print(f"A soma dos numeros da terceira coluna é igual a {soma}")
print(f"O maior numero da 2 linha é {max(slinha)}" )