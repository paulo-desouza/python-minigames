import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)


sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

text_color = (64, 64, 64)
box_color = '#c0e8ec'

score_surf = test_font.render('My Game', False, text_color)
score_rect = score_surf.get_rect(center = (400, 50))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600, 300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('JUMP')

        if event.type == pygame.KEYUP:
            print('key up')


        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print('collision')
    
    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, 300))
    pygame.draw.rect(screen, box_color, score_rect)
    screen.blit(score_surf, (score_rect))

    if snail_rect.x > -100:
        snail_rect.left -= 4
    else:
        snail_rect.x = 900
    screen.blit(snail_surf, snail_rect)
    player_rect.left += 1
    screen.blit(player_surf, player_rect)

    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_SPACE]:
    #    print('JUMP')

    # if player_rect.colliderect(snail_rect):
    #     print('collision')


    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)