v1 = float(input("Digite o valor do primeiro lado do triangulo: "))
v2 = float(input("Digite o valor do segundo lado do triangulo: "))
v3 = float(input("Digite o valor do terceiro lado do triangulo: "))
if v1 + v2 > v3 and v2 + v3 > v1 and v1 + v3 > v2:
    print("É possivel formar um triangulo")
else:
    print("Não é possivel formar um triangulo")