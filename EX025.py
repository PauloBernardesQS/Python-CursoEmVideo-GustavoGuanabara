frase = input("Digite uma frase:").strip()
print(f"Essa frase possui {frase.upper().count('A') } letras a")
print(f"A primeira letra a aparece na posição {frase.upper().find('A')+1}")
print(f"A ultima letra a aparece na pósição {frase.upper().rfind('A')+1}")
