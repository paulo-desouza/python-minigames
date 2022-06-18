# EX 068: PAR OU IMPAR (EVEN OR UNEVEN) - Create a program that will play EVEN or UNEVEN with you, a game where you and
# the computer both pick either even or uneven, and a number. If the sum of the two numbers is EVEN, the player that
# picked EVEN wins. Run the game until PLAYER loses.
from random import randint
v = 0
while True:
    PC = randint(0, 6)
    PLAYER = str(input('PAR OU IMPAR?')).strip().upper()[0]
    while PLAYER not in 'PI':
        print('Resposta Invalida!!')
        PLAYER = str(input('PAR OU IMPAR?')).strip().upper()[0]
    PLAY = int(input('Qual numero voce joga?'))
    TOT = PLAY + PC
    print(f'Computador jogou {PC}!\nJOGADOR jogou {PLAY}!\n{PC}+{PLAY}={TOT}!')
    if TOT % 2 == 0 and PLAYER == 'P':
        print('You Win!')
        v += 1
    elif TOT % 2 == 0 and PLAYER == 'I':
        print('You Lose! Good bye.')
        break
    elif TOT % 2 == 1 and PLAYER == 'P':
        print('You Lose! Good bye.')
        break
    elif TOT % 2 == 1 and PLAYER == 'I':
        print('You Win!')
        v += 1
    print('#'*15)
print(f'Voce venceu {v} vezes.')




