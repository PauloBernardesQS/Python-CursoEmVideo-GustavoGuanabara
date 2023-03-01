nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0
print("-" * 20)
print("RETIRE SEU DINHEIRO")
print("-" * 20)
valor = int(input("Quanto voce quer sacar -> R$"))
while True:
    if valor > 0:
        if valor - 50 >= 50:
            valor = valor - 50
            nota50 += 1
        elif valor - 20 >= 20:
            valor = valor - 20
            nota20 += 1
        elif valor - 10 >= 10:
            valor = valor - 10
            nota10 += 1
        elif valor - 1 >= 1:
            valor = valor - 1
            nota10 += 1
    else:
        break
print(f"Você ira receber {nota50} notas de 50, {nota20} notas de 20, {nota10} notas de 10 e {nota1} notas de 1")
