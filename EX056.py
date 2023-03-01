while True:
    sexo = input("Digite qual sua sexualidade: (M/F) -> ")
    if sexo.upper() == "M" or sexo.upper() == "F":
        print("\033[32mCadastrado com sucesso!\033[m")
        break
    else:
        print("\033[31mSexo invalido, escreva novamente!\033[m")
        continue
