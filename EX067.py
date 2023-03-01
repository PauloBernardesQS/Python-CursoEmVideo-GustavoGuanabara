m = 0
maior = 0
mvinte = 0
while True:
    print("-" * 20)
    idade = int(input("Qual sua idade: "))
    sexo = (input("Qual seu sexo (F/M): "))
    if sexo.upper() == "M":
        m += 1
    elif sexo.upper() == "F" and idade < 20:
        mvinte += 1
    else:
        continue
    if idade >= 18:
        maior += 1
    print("-"* 20)
    while True:
        continuar = input("Voce deseja continuar (S/N): ")
        if continuar.upper() == "N":
            print(f'''
        VOCE CADASTROU POR HOJE:
    
        {m} Homem(s)
        {maior} Pessoa(s) maiores de idade
        {mvinte} Mulher(s) com menos de vinte anos''')
            exit()
        elif continuar.upper() == "S":
            break
        else:
            continue
