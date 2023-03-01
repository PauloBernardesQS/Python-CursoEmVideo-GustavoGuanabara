nome = str(input("Digite seu numero completo: ")).strip()
nomeDiv = nome.split()
print(f"Seu todo em maiusculo: {nome.upper()}")
print(f"Seu nome todo em minusculo: {nome.lower()}")
print(f"Seu nome tem ao todo {len(nome) - nome.count(' ')} letras")
print(f"Seu primeiro nome possui {len(nomeDiv[0])} letras")

