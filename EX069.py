total = mil = pbarato = nbarato = c = 0
continuar = ' '
while not continuar.upper()  == "S":
    produto = input("Digite o nome do produto -> ")
    preco = float(input("Digite o preço do produto -> "))
    c += 1
    total += preco
    if c == 1:
        pbarato = preco
        nbarato = produto
    else:
        if preco < pbarato:
            pbarato = preco
            nbarato = produto
    if preco > 1000:
        mil += 1
    continuar = input("Voce ja acabou sua lista ? (s/n) ")
print(f"Voce gastou R${total}, comprando {c} produtos, sendo o {nbarato} o produto mais barato por R${pbarato} ")