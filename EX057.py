from random import randint
numeroEscolhido = randint(0,10)
contador = 0
print("O COMPUTADOR ESCOLHEU UM NUMERO DE 0 ATE 10, TENTE ACERTAR QUAL É!")
while True:
    tentativa = int(input("O numero escolhido é -> "))
    contador = contador + 1
    if tentativa == numeroEscolhido:
        print(f"VOCE ACERTOU EM {contador} TENTATIVAS")
        break
    elif tentativa < numeroEscolhido:
        print(f"É um pouco mais que {tentativa}, tente denovo: ")
        continue
    else:
        print(f"É um pouco menos que {tentativa}, tente denovo: ")
        from random import randint

    #tentativa = 100
    #numeroEscolhido = randint(0, 10)
    #print("O computador pensou em um numero de 0 a 10, tente advinhar qual é?")
    #while tentativa != numeroEscolhido:
    #    tentativa = int(input("Eu acho que o numero é -> "))
    #print("VOCE ACERTOU!")