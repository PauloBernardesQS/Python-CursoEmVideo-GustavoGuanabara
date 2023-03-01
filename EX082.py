num = []
pares = []
impares = []

while True:
    num.append(int(input("Digite um numero -> ")))
    cont = input("Você deseja continuar colocando numeros? (s/n) -> ")
    if cont.upper().strip() == "S":
        continue
    elif cont.upper().strip() =="N":
        break
    else:
        break
for p in num:
    if p % 2 == 0:
        pares.append(p)
    else:
        impares.append(p)
print(f"NUMEROS DIGITADOS {num}")
print(f"NUMEROS PARES DIGITADOS {pares}")
print(f"NUMEROS IMPARES DIGITADOS {impares}")
