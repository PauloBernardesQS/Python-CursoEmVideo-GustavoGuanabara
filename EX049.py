s = 0
for c in range(0,6):
    n1 = int(input("Digite um numero inteiro:"))
    if n1%2 == 0:
        s += n1
print(f"A soma dos valores pares citados é igual a: {s}")