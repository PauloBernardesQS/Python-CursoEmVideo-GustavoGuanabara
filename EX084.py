dados = []
pessoas = []
maior = 0
menor = 0

while True:
    dados.append(input("Digite o nome da pessoa -> "))
    dados.append(float(input("Digite o peso da pessoa -> ")))
    if len(pessoas) == 0:
        maior = dados[1]
        menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    cont = input('Voce deseja registrar mais alguem? (s/n) -> ')
    pessoas.append(dados[:])
    dados.clear()
    if cont == "s":
        continue
    else:
        break


print(f"O menor peso registrado foi de {menor}kg e o maior foi {maior}")