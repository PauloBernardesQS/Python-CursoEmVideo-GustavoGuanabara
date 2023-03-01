num = int(input("Quantas vezes sera feita a repetição? "))
atual = 1
anterior = 0
c = 0
while c != num:
    proximo = anterior + atual
    print(f" -> {anterior} + {atual} = {proximo}", end=" ")
    anterior = atual
    atual = proximo
    c += 1
