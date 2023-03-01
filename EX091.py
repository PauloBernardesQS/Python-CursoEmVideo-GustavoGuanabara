from random import randint
from time import sleep
from operator import  itemgetter
player = {
    "jogador 1" : randint(1,6),
    "jogador 2" : randint(1,6),
    "jogador 3" : randint(1,6),
    "jogador 4" : randint(1,6)}
for k, v in player.items():
    print(f"O {k} tirou {v}")
    sleep(1)
rank = list()
rank = sorted(player.items(), key=itemgetter(1), reverse=True)
for p, k in enumerate(rank):
    print(f"{p+1}º lugar: {k[0]}")
    sleep(1)


