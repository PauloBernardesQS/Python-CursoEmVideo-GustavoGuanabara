frase = input("Digite sua frase: ").strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = junto[::-1]
if junto == inverso:
    print(f"{frase} é um palindrome!")
else:
    print("Não temos um palindrome!")