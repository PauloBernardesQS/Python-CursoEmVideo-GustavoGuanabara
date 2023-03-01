numeros = ((int(input("Digite um numero -> ")),
    int(input("Digite um numero -> ")),
    int(input("Digite um numero -> ")),
    int(input("Digite um numero -> "))))
pares = 0
print(f"Numeros digitados: {numeros}")
print(f"Voce digitou {numeros.count(9)} vezes o numero 9")
if 3 in numeros:
    print(f"O valor 3 esta na {numeros.index(3) + 1}º posição")
else:
    print("O valor 3 não existe")
for num in numeros:
    if num % 2 == 0:
        pares += 1
print(f"Existem {pares} numeros pares")