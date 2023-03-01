contador = 0
n1 = int(input("Digite algum numero inteiro -> "))
for p in range (2, n1):
    if n1 % p == 0:
        contador = contador + 1
if contador == 0:
    print("Esse numero é primo")
else:
    print("Esse numero não é primo")

