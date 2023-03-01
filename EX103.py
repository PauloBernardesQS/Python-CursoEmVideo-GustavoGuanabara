def Ficha(n="desconhecido",g=0):
    print(f"O jogador {n} marcou {g} gol(s)")
n = input("Nome do jogador: ")
g = input("Digite numero de gols do jogador: ")
if g.isnumeric():
    int(g)
else:
    g = 0
if n == '' or  n.isnumeric():
    Ficha(g = g)
else:
    Ficha(n=n, g=g)

