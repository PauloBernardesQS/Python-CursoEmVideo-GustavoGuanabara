n1 = int (input("Digite o valor de um numero inteiro -> "))
m = 0
fatorial = n1
print("Fatorial do numero...")
while True:
    fatorial -= 1
    if fatorial > 0:
        n1 = n1 * fatorial
    else:
        break
print(n1)