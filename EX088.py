from random import randint
jogos = int(input("Quantos jogos voce deseja jogar -> "))
for c in range(0,jogos):
    numeros = [randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60)]
    print(f"Jogo {c + 1}: {numeros}")