from random import choice
from time import sleep
numero = int(input("Digite um numero inteiro de 0 a 5: "))
numeros = [0, 1, 2, 3, 4, 5]
sorteado = choice(numeros)
print("PROCESSANDO...")
sleep(2)
if numero == sorteado:
    print("Parabens voce acertou o numero")
else:
    print(f"Não foi dessa vez, pensei no numero {sorteado}")
