matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = input(f"Digite um numero para a linha {l} coluna {c} -> ")
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]}] ", end="")
    print()