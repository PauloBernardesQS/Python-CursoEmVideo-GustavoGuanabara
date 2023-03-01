from time import sleep
n1 = float(input("Digite o valor do primeiro numero -> "))
n2 = float(input("Digite o valor do segundo numero -> "))
while True :
    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] QUEM É O MAIOR?
    [4] MUDAR OS NUMEROS
    [5] SAIR 
    ''')
    escolha = int(input("Digite o numero da opção exigida -> "))
    if escolha == 1:
        print(f"{n1} + {n2} = {n1 + n2}")
        continue
    elif escolha == 2:
        print(f"{n1} X {n2} = {n1 * n2}")
        continue
    elif escolha == 3:
        if n1 > n2:
            print(f"{n1} é maior que {n2}")
            continue
        elif n2 < n1:
            print(f"{n2} é maior que {n1}")
            continue
        else:
            print(f"{n1} e {n2} possuem o mesmo valor")
            continue
    elif escolha == 4:
        novon1 = int(input("Digite o novo valor para o primeiro numero -> "))
        n1 = novon1
        novon2 = int(input("Digite o novo valor para o segundo numero -> "))
        n2 = novon2
        continue
    elif escolha == 5:
        print("Saindo...")
        sleep(1)
        break
    else:
        print("Escolha não disponivel")
        continue