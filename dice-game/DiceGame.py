import pygame
import random
from sys import exit
from operator import itemgetter


pygame.init()

# Getting clock info
current_time = 0
time_when_pressed = 0

# Defining the screen size
WIDTH = 610
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('dice-game')

clock = pygame.time.Clock()

# Loading the images for the die.
dice_imgs = [
    pygame.image.load('dice-game/Sprites/Dice-1.png').convert_alpha(),
    pygame.image.load('dice-game/Sprites/Dice-2.png').convert_alpha(),
    pygame.image.load('dice-game/Sprites/Dice-3.png').convert_alpha(),
    pygame.image.load('dice-game/Sprites/Dice-4.png').convert_alpha(),
    pygame.image.load('dice-game/Sprites/Dice-5.png').convert_alpha(),
    pygame.image.load('dice-game/Sprites/Dice-6.png').convert_alpha()
]

dice_size = (64, 64)

dice_surfs = [
    pygame.transform.scale(dice_imgs[0], dice_size),
    pygame.transform.scale(dice_imgs[1], dice_size),
    pygame.transform.scale(dice_imgs[2], dice_size),
    pygame.transform.scale(dice_imgs[3], dice_size),
    pygame.transform.scale(dice_imgs[4], dice_size),
    pygame.transform.scale(dice_imgs[5], dice_size)
]

# Creating the "Play" Button and Results Display
button_img = pygame.image.load(
    'dice-game/Sprites/unnpressed.png').convert_alpha()
start_img = pygame.transform.scale(button_img, (130, 85))

button_font = pygame.font.Font('dice-game/font/Pixeltype.ttf', 50)

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def draw(self):
        global play
        # get mouse position
        pos = pygame.mouse.get_pos()
        action = False
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked == True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            action = False

        # draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action
    
        
    def reset(self):
        global rand
        rand = []
        for c, i in enumerate(dice_rects):
            rand.append(random.randint(0, 5))
        play = True 
        run = False




# create button instance
start_button = Button(300, 300, start_img)
again_button = Button(300, 300, start_img)

first_surf = button_font.render('First Place!', False, 'Black')
second_surf = button_font.render('Second Place', False, "Black")
third_surf = button_font.render('Third Place', False, 'Black')
fourth_surf = button_font.render('Fourth Place...', False, 'Black')
fifth_surf = button_font.render('         Tie!', False, 'Black')

# Defining the coordinates for each dice in the list, appending each to the dice rectangles list through the loop.
dice_rects = []
dice_rects_coord = [
    (250, 500), (350, 500), (500, 250), (500,
                                            350), (100, 250), (100, 350), (250, 100), (350, 100)
]
for i in range(len(dice_rects_coord)):
    dice_rects.append(dice_surfs[1].get_rect(
        center=dice_rects_coord[i]))

# Randomizing the sprite for the dice.
rand = []
for c, i in enumerate(dice_rects):
    rand.append(random.randint(0, 5))

play = False
run = True
# Start running the game.
while run:
    # Here we get all the player input from mouse and keyboard.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if start_button.rect.collidepoint(event.pos):
                # Keeping track of actual time
                if play == False:
                    play = True

    screen.fill((189, 255, 255))

    if start_button.draw():
        if play == False:
            play = True
            time_when_pressed = pygame.time.get_ticks()

    positions = [first_surf, second_surf,
                    third_surf, fourth_surf, fifth_surf]
    players = {
        (300, 560): rand[0] + rand[1] + 2,
        (500, 410): rand[2] + rand[3] + 2,
        (100, 410): rand[4] + rand[5] + 2,
        (300, 160): rand[6] + rand[7] + 2,
    }
    # Bringing the surface (image) and rectangle (coordinate) to blit (display) the die once play_button has been pressed.
    if play == True:

        for id, dice in enumerate(dice_rects):
            current_time = pygame.time.get_ticks()
            tie = False
            # If first loop, reset background
            if id == 0:
                screen.fill((189, 255, 255))

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

        if current_time - time_when_pressed >= 2000:
            if rank[0][1] == rank[1][1]:
                tie = True
                for i, v in enumerate(rank):
                    if i == 2:
                        break
                    screen.blit(
                        positions[4], positions[i].get_rect(center=v[0]))
                positions = positions[2:]
                rank = rank[2:]

            elif rank[0][1] == rank[2][1]:
                tie = True
                for i, v in enumerate(rank):
                    if i == 3:
                        break
                    screen.blit(
                        positions[4], positions[i].get_rect(center=v[0]))
                positions = positions[3:]
                rank = rank[3:]

            for i, v in enumerate(rank):
                screen.blit(
                    positions[i], positions[i].get_rect(center=v[0]))

            if again_button.draw():
                play = False
                again_button.reset()
    # Updating the screen and defining the framerate.
    
    pygame.display.update()
    clock.tick(60)
