from random import randint
numeros = []
def sorteio(lista):
    for n in range(0,5):
        lista.append(randint(0,100))
    print(f"Numeros sorteados {lista}")
def pares(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f"A soma dos numeros pares sorteados é {soma}")
sorteio(numeros)
pares(numeros)


