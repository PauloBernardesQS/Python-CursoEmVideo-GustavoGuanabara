velocidade = float(input("Digite a velocidade em km/h que o carro percorria: "))
if velocidade > 80:
    multa = (velocidade-80)*7
    print(f"\033[31mO preco da multa vai ser de R${multa:.2f}")
else:
    print("\033[32mBom dia, dirija em segurança!\033[m")