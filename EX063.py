contador = 0
soma = 0
print("DIGITE QUANTOS NUMEROS INTEIROS QUISER, se digitar 999, o programa vai encerrar! ")
num = int(input("numero -> "))
while num != 999:
    contador = contador + 1
    soma = soma + num
    num = int(input("numero -> "))
print(f"Voce digitou {contador} numeros")
print(f"A soma de todos os numero digitados é igual a -> {soma }")