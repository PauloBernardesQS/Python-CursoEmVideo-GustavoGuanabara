vlr1 = int(input("Digite o primeiro valor da P.A: "))
razao = int(input("Digite qual o valor da razão da P.A: "))
limite = vlr1 + razao * 9
while  vlr1 <= limite:
    print(f" -> {vlr1 }", end=" ")
    vlr1 = vlr1 + razao