numDig = 45
while numDig < 0 or numDig > 20:
    numDig = int(input("Digite um numero de 0 a 20 -> "))
numeros = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
print(f"Voce digitou o numero {numeros[numDig]}")
