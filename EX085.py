pares = []
impar = []
for n in range(0,7):
    number = int(input("Digite um numero -> "))
    if number % 2 == 0:
        pares.append(number)
    else:
        impar.append(number)
pares.sort()
impar.sort()
print(f'''
NUMEROS PARES -> {pares}
NUMEROS IMPARES -> {impar}
''')