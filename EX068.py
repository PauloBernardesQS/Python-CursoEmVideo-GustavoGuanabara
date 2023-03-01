from random import randint
print("VAMOS JOGAR PAR OU IMPAR")
while True:
    pi = input("PAR OU IMPAR? ")
    num = int(input("Digite um numero -> "))
    pc = randint(1, 2)
    soma = num + pc
    if soma % 2 == 0 and pi.upper() == "PAR":
        print(f"PARABENS VOCE GANHOU!, {num} + {pc} = PAR ")
    elif soma % 2 == 1 and pi.upper() == "IMPAR":
        print(f"PARABENS VOCE GANHOU!, {num} + {pc} = IMPAR ")
    else:
        print(f"VOCE PERDEU... {soma} não é {pi}")

    while True:
        continuar = input("Deseja jogar novamente (s/n) ? ")
        if continuar.upper() == "N":
            exit()
        if continuar.upper() == "S":
            break
        else:
            continue