num1 = float(input("Digite o valor do numero 1: "))
num2 = float(input("Digite o valor do numero 2: "))
if num1 > num2:
    print(f"{num1} é maior que {num2}")
elif num2 > num1:
    print(f"{num2} é maior que {num1}")
else:
    print("Os dois numeros são iguais!")