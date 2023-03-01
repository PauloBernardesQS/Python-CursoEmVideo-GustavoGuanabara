jogador = dict()
gols = list()
jogador['Nome'] = input("Digite o nome do jogador -> ")
partida = int(input(f"Digite quantas paridas {jogador['Nome']} jogou -> "))
for g in range(0, partida):
    gols.append(int(input(f"Digite quantos gols {jogador['Nome']} fez na {g + 1}º partida -> ")))
jogador['partidas'] = partida
jogador['gols'] = gols[:]
jogador['temporada'] = sum(gols)
jogador['media'] = jogador['temporada'] / jogador['partidas']
print(jogador.items())
for n, c in jogador.items():
    print(F"{n} -> {c}")


