import pygame
import random
from sys import exit
from operator import itemgetter

# TASK: Display Winners and add "Play Again" Button
pygame.init()



# Getting clock info
current_time = 0
time_when_pressed = 0

# Defining the screen size
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dice Game')

clock = pygame.time.Clock()

# Loading the images for the die.
dice_surfs = [
    pygame.image.load('Dice Game/Sprites/Dice-1.png').convert_alpha(),
    pygame.image.load('Dice Game/Sprites/Dice-2.png').convert_alpha(),
    pygame.image.load('Dice Game/Sprites/Dice-3.png').convert_alpha(),
    pygame.image.load('Dice Game/Sprites/Dice-4.png').convert_alpha(),
    pygame.image.load('Dice Game/Sprites/Dice-5.png').convert_alpha(),
    pygame.image.load('Dice Game/Sprites/Dice-6.png').convert_alpha()
]

# Creating the "Play" Button and Results Display
button_font = pygame.font.Font('Dice Game/font/Pixeltype.ttf', 50)
button_color = (0, 0, 0)
play_button_surf = button_font.render('Roll Dice!', False, button_color)
play_button_rect = play_button_surf.get_rect(center = (300, 300))

first_surf = button_font.render('First Place!', False, 'Black')
second_surf = button_font.render('Second Place!', False, "Black")
third_surf = button_font.render('Third Place!', False, 'Black')
fourth_surf = button_font.render('Fourth Place', False, 'Black')

first_rect = first_surf.get_rect(center = (300, 500))

# Defining the coordinates for each dice in the list, appending each to the dice rectangles list through the loop.
dice_rects = []
dice_rects_coord = [
    (250, 500), (350, 500), (500, 250), (500, 350), (100, 250), (100, 350), (250, 100), (350, 100)
]
for i in range(len(dice_rects_coord)):
    dice_rects.append(dice_surfs[1].get_rect(center = dice_rects_coord[i]))

# Randomizing the sprite for the dice. 
rand = []
for c, i in enumerate(dice_rects):
    rand.append(random.randint(0, 5))


play = False

# Start running the game.
while True:
    # Here we get all the player input from mouse and keyboard.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                if play == False:
                    play = True
                    # Get time when pressed
                    time_when_pressed = pygame.time.get_ticks()

    # Keeping track of actual time
    current_time = pygame.time.get_ticks()

    screen.fill('Pink')
    screen.blit(play_button_surf, play_button_rect)
    positions = [first_surf, second_surf, third_surf, fourth_surf]
    players = {
            (300, 500) : rand[0] + rand[1] + 2,
            (500, 300) : rand[2] + rand[3] + 2,
            (100, 300) : rand[4] + rand[5] + 2,
            (300, 100) : rand[6] + rand[7] + 2,
        }

    # Bringing the surface (image) and rectangle (coordinate) to blit (display) the die once play_button has been pressed.
    if play == True:
        for id, dice in enumerate(dice_rects):
            # If first loop, reset background
            if id == 0:
                screen.fill('Pink')
            
            # Conditional Statements checking from the time that the button has pressed.
            if id < 2:
                screen.blit(dice_surfs[rand[id]], (dice_rects[id]))

            elif id < 4:
                if current_time - time_when_pressed >= 500:
                    screen.blit(dice_surfs[rand[id]], (dice_rects[id]))
                    
            elif id < 6:
                if current_time - time_when_pressed >= 1000:
                    screen.blit(dice_surfs[rand[id]], (dice_rects[id]))
                    
            elif id < 8:
                if current_time - time_when_pressed >= 1500:
                    screen.blit(dice_surfs[rand[id]], (dice_rects[id]))

        
        rank = sorted(players.items(), key=itemgetter(1), reverse=True)

        for i, v in enumerate(rank):
            if current_time - time_when_pressed >= 2000:
                screen.blit(positions[i], (v[0]))

    

    # Updating the screen and defining the framerate.
    pygame.display.update()
    clock.tick(60)
