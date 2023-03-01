numeros = []
for n in range(0,5):
    num = int(input("Digite o numero ->"))
    if n == 0 or num > numeros[-1]:
        numeros.append(num)
    else:
        p = 0
        while p <= len(numeros):
            numeros.insert(p, num)
            break

print(numeros)

