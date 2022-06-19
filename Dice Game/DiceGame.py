import pygame
import random
from sys import exit
from time import sleep

pygame.init()

WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dice Game')

clock = pygame.time.Clock()

dice_surfs = [
    pygame.image.load('Dice Game/Sprites/Dice-1.png').convert_alpha(),
    pygame.image.load('Dice Game/Sprites/Dice-2.png').convert_alpha(),
    pygame.image.load('Dice Game/Sprites/Dice-3.png').convert_alpha(),
    pygame.image.load('Dice Game/Sprites/Dice-4.png').convert_alpha(),
    pygame.image.load('Dice Game/Sprites/Dice-5.png').convert_alpha(),
    pygame.image.load('Dice Game/Sprites/Dice-6.png').convert_alpha()
]

dice_rects = [
    dice_surfs[1].get_rect(center = (250, 500)),
    dice_surfs[1].get_rect(center = (350, 500)),
    dice_surfs[1].get_rect(center = (500, 250)),
    dice_surfs[1].get_rect(center = (500, 350)),
    dice_surfs[1].get_rect(center = (100, 250)),
    dice_surfs[1].get_rect(center = (100, 350)),
    dice_surfs[1].get_rect(center = (250, 100)),
    dice_surfs[1].get_rect(center = (350, 100))
]

rand = []
for c, i in enumerate(dice_rects):
    rand.append(random.randint(0, 5))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()
        #if event.type == pygame.MOUSEBUTTONDOWN:
        #     print(event.pos)

    screen.fill('Pink')
    for id, dice in enumerate(dice_rects):
        screen.blit(dice_surfs[rand[id]], (dice_rects[id]))
        pygame.time.delay(1000)
        

    pygame.display.update()
    clock.tick(60)
