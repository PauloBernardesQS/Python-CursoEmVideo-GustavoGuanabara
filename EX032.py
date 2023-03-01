n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))
n3 = float(input("Digite outro numero: "))
menor = n1
maior = n2
if n1 > n2 and n1 > n3:
    maior = n1
if n3 > n1 and n3 > n2:
    maior= n3
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n2
print(f"O MENOR numero é: {menor}")
print(f"O MAIOR numero é: {maior}")