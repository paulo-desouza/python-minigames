playerList = []
playerStats = {}
while True:
    playerStats.clear()
    playerStats = {'name': str(input('Player name:')), 'goals': [], 'total': 0}
    matches = int(input('How many matches were played?'))
    for c in range(0, matches):
        playerStats['goals'].append(int(input(f'How many goals in match {c + 1}?')))
        playerStats['total'] += playerStats['goals'][c]
    playerList.append(playerStats.copy())
    while True:
        check = str(input('Would you like to add another player?(Yes or No)')).strip().lower()[0]
        if check in "yn":
            break
    if check == 'n':
        break
print('-'*40)
print('No. ', end='')
for k in playerStats.keys():
    print(f'{k:15}', end='')
print()
print('-'*40)
for c, p in enumerate(playerList):
    print(f'{c:3} {p["name"]:<10} {str(p["goals"]):>11} {str(p["total"]):>6}')
print('-'*40)
while True:
    playerPull = int(input('Which player`s data would you like to see? Search by number, 999 to quit.'))
    if playerPull == 999:
        break
    while playerPull >= len(playerList):
        playerPull = int(input('Player not found. Which player`s data would you like to see? Search by number, '
                               '999 to quit.'))
    print(f'{playerList[playerPull]["name"]} STATS:')
    for i, v in enumerate(playerList[playerPull]['goals']):
        print(f'In game {i}, player scored {v} goals.')
    print('-'*40)
print('See ya!')
