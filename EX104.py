def LeiaInt(text = "Digite um numero inteiro -> "):
    while True:
        n = input(f"{text}")
        if n.isnumeric():
            int(n)
            break
        else:
            continue
    return n
h = LeiaInt()
print(f"Voce digitou o numero {h}")

