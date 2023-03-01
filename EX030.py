viagem = float(input("Digite quantos km voce vai percorrer: "))
if viagem > 200:
    vlrPb=(viagem * 0.45)
    print(f"O valor da passagem vai ser de R${vlrPb:.2f}")
else:
    vlrPc=(viagem * 0.50)
    print(f"O valor da passagem vai ser de R${vlrPc:.2f}")