# EX 091 : Make a program that will simulate 4 people rolling a d6, and then, show the position of each player,
# based on who rolled highest.
from random import randint
from time import sleep
from operator import itemgetter
players = {'Player 1': randint(1, 6),
           'Player 2': randint(1, 6),
           'Player 3': randint(1, 6),
           'Player 4': randint(1, 6)}
for gg, hf in players.items():
    print(f'{gg} rolled a {hf}')
    sleep(1)
rank = sorted(players.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(rank):
    print(f'{i + 1} Place: {v[0]} with a roll of {v[1]}')
"""
count = 0
for c in range(0, 4):
    count += 1
    print(f'In {count} place, we have:')
    for d in range(0, 2):
        print(f'{rank[c][d]}')
"""
