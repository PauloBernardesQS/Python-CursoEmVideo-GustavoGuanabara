def read_money():
    while True:
        v = input("Digite o valor -> ")
        if v.strip() == "":
            print("Valor Vazio")
            continue
        elif v.isnumeric() == False:
            print(f"{v} Valor Invalido")
            continue
        else:
            print("Correct")
            break