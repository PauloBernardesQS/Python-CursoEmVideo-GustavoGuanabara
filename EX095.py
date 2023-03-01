jogador = dict()
gols = list()
time = list()
while True:
    jogador.clear()
    jogador['Nome'] = input("Digite o nome do jogador -> ")
    partida = int(input(f"Digite quantas partidas {jogador['Nome']} jogou -> "))
    gols.clear()
    for g in range(0, partida):
        gols.append(int(input(f"Digite quantos gols {jogador['Nome']} fez na {g + 1}º partida -> ")))
    jogador['partidas'] = partida
    jogador['gols'] = gols[:]
    jogador['Total'] = sum(gols)
    time.append(jogador.copy())
    continuar = input("Deseja continuar(S/N): ")
    if continuar.upper() == "S":
        continue
    else:
        break
print(time)
for n , v in enumerate(time):
    print(f'''
    Cod: {n}
    Nome: {time[n]['Nome']}
    Gols: {time[n]['gols']}
    Total de gols: {time[n]['Total']}
    ''')
descrição = (int(input("Se desejar ver dados de um jogador digite seu cod (999 para sair) -> ")))
if descrição == 999:
    exit()
else:
   print(f'{time[descrição]["Nome"]} fez:')
   for p, g in enumerate(time[descrição]['gols']):
    print(f"No {p + 1}º jogo {g} gols ")