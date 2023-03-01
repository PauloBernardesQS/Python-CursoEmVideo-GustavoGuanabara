def LeiaInt():
    while True:
        try:
            n = int(input("Digite um numero Inteiro -> "))
        except (ValueError, TypeError):
            print(f"Valor não é inteiro ")
            continue
        else:
            return n
            print("Correto")
            break
def LeiaFloat():
    while True:
        try:
            f = float(input("Digite um numero real -> "))
        except (ValueError, TypeError):
            print(f"Valor não é um numero real")
            continue
        else:
            return f
            print("Correto")
            break
print(f"O valor Int é {LeiaInt()}, o valor Float é {LeiaFloat()}")