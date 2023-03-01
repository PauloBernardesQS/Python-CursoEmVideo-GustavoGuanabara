altura = float(input("Digite sua altura: "))
peso = float(input("Digite sua altura: "))
IMC = peso / (altura*altura)
if IMC <= 18.5:
    print("Voce esta abaixo do peso")
elif IMC <= 25:
    print("Voce esta no peso ideal")
elif IMC <= 30:
    print("Voce esta acima do peso")
elif IMC <= 40:
    print("Voce esta obeso")
else:
    print("Obeso")
