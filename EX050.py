vlr1 = int(input("Digite o primeiro valor da PA: "))
razao = int(input("Digite a razao da PA: "))
print("Os 10 primeiros termos dessa pregressão vai ser: ")
for c in range(vlr1, vlr1 + razao * 10, razao ):
    print(f" -> {c}.", end=" ")