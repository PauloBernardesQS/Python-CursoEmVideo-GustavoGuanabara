def LeiaInt(text):
    while True:
        try:
            n = int(input(text))
        except (ValueError, TypeError):
            print(f"Valor não é inteiro ")
            continue
        else:
            return n

def linha(tam = 30):
    print("-=" * tam)

def cabecalho(txt = "MENU"):
    linha()
    print(txt.center(60))
    linha()

def menu(lista):
    cabecalho()
    c = 1
    for p in lista:
        print(f"{c}- {p}")
        c += 1
    opc = LeiaInt("Opção -> ")
    return opc