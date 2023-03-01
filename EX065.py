s = c = 0
while True:
    n1 = int(input("Digite um valor de um numero -> "))
    if n1 == 999:
        break
    s += n1
    c += 1
print(f"Você digitou {c} numeros e a soma deles é {s}")