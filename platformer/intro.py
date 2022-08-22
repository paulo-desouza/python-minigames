import pygame
from sys import exit

## Unfinished

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('platformer/font/Pixeltype.ttf', 50)
game_active = True


sky_surf = pygame.image.load('platformer/graphics/Sky.png').convert()
ground_surf = pygame.image.load('platformer/graphics/ground.png').convert()

text_color = (64, 64, 64)
box_color = '#c0e8ec'

score_surf = test_font.render('You lose', False, text_color)
score_rect = score_surf.get_rect(center = (400, 50))

snail_surf = pygame.image.load('platformer/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600, 300))

player_surf = pygame.image.load('platformer/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0
velocity = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    if player_rect.bottom == 300:
                        player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom == 300:
                        player_gravity = -20
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    velocity = 5
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    velocity = 0
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    velocity = -5
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    velocity = 0
                    
                    
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    snail_rect.left = 800

    if game_active:
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))
        

        if snail_rect.x > -100:
            snail_rect.left -= 4
        else:
            snail_rect.x = 900
        screen.blit(snail_surf, snail_rect)

        # Player
        player_gravity += 1
        player_rect.x += velocity
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('Yellow')
        screen.blit(score_surf, (score_rect))

    pygame.display.update()
    clock.tick(60)