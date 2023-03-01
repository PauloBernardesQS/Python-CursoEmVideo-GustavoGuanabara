numeros = []
while True:
    numeros.append(int(input("Digite um numero -> ")))
    cont = input("Você deseja continuar colocando numeros? (s/n) -> ")
    if cont.upper().strip() == "S":
        continue
    elif cont.upper().strip() =="N":
        break
    else:
        print("Opção não encontrada digite novamente")
        continue
numeros.sort()
print("Os numeros em ordem crescente digitados são:")
print(numeros)
