contador = 0
soma = 0
print("DIGITE QUANTOS NUMEROS INTEIROS QUISER, se digitar 999, o programa vai encerrar! ")
escolha = "S"
maior = menor = 0
while escolha.upper() == "S":
    num = int(input("numero -> "))
    contador = contador + 1
    if contador == -1:
        menor = maior = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma = soma + num
    escolha = input("Voce deseja continuar digitando (s/n)? ")
print(f"Voce digitou {contador} numeros")
print(f"A soma de todos os numero digitados é igual a -> {soma}")
print(f"O maior numero digitado foi {maior}")
print(f"O menor numero é {menor}")