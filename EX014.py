dias = int(input("Quantos dias voce alugou o carro? "))
km = float(input("Quantos km voce andou com o carro? "))
pagar = (dias * 60) + (km * 0.15)
print("O valor a ser pago vai ser de R${:.2f}".format(pagar))