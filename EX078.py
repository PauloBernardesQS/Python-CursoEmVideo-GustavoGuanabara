numeros = []
for c in range(0,5):
    numeros.append(int(input("Digite um numero -> ")))
print(numeros)
print(f"{min(numeros)} é o menor numero e aparece na posição {min(numeros).__index__()}")
print(f"{max(numeros)} é o maior numero e aparece na posição {max(numeros).__index__()} ")
