from random import randint
numeros = (randint(1, 50),
randint(1, 50),
randint(1, 50),
randint(1, 50),
randint(1, 50))
print(f"Numeros sorteados: {numeros}")
print(f"O maior numero sorteado foi: {max(numeros)}")
print(f"O menor numero sorteado foi: {min(numeros)}")
