v1 = float(input("Digite o valor do primeiro lado do quadrado: "))
v2 = float(input("Digite o valor do segundo lado do quadrado: "))
v3 = float(input("Digite o valor do terceiro lado do quadrado: "))
if v1 + v2 > v3 and v2 + v3 > v1 and v3 + v1 > v2:
    print("É possivel construir um triangulo!")
    if v1 == v2 == v3:
        print("Ele é um triangulo equilatero")
    if (v1 == v2 and v1 != v3) or (v3 == v2 and v3 != v1) or (v1 == v3 and v1 != v2):
        print("Ele é um triangulo Isoceles")
    if v1 != v3 and v1 != v2 and v3 != v2:
        print("Ele é um triangulo Escaleno")
else:
    print("Não é possivel criar um triangulo")