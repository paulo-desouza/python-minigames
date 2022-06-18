# Write a game where you have to guess what number the computer is 'thinking' of until you get it right,
# and then showcase how many times you had to try before you got it right
from random import randint
PC = randint(0, 10)
PLAYER = 11
c = 0
print('SUPER GUESSING GAME! Guess the number the computer is thinking about, from 0 to 10.')
while PC != PLAYER:
    PLAYER = int(input('What is your input?'))
    while not 10 >= PLAYER >= 0:  # Validation
        PLAYER = int(input('Invalid entry! Try again:'))
    c += 1
if PC == PLAYER:
    print('Congratulations! And it only took {} tries.'.format(c))
else:
    print('You lose.')
