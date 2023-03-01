name = input("Digite o nome da sua cidade: ").strip()
nameA = name.split()
print(f"Existe o nome santos no primeiro nome da cidade: {'SANTO' in nameA[0].upper()}")