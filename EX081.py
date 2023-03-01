lista = []
while True:
    lista.append(int(input("Digite um numero -> ")))
    cont = input("Você deseja continuar colocando numeros? (s/n) -> ")
    if cont.upper().strip() == "S":
        continue
    elif cont.upper().strip() =="N":
        break
    else:
        break
lista.sort(reverse=True)
print(f'''
VOCÊ DIGITOU {len(lista)} NUMEROS
ORDEM DECRESCENTE {lista}
''')
if 5 in lista:
    print("O VALOR 5 FOI ADICIONADO NA LISTA ")
else:
    print("NÃO EXISTE O VALOR 5 NA LISTA")
