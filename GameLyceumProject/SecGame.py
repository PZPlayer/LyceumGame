import pygame
import sys

pygame.init()

width = 800
height = 600

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Танчики")

white = (255, 255, 255)
black = (0, 0, 0)

tank_width = 50
tank_height = 50
tank_speed = 0.2
bullet_speed = 0.6
bullet_radius = 5

tank1_x = 50
tank1_y = height // 2
tank2_x = width - 50
tank2_y = height // 2

bullet1_x = 0
bullet1_y = 0
bullet2_x = 0
bullet2_y = 0

tank1_direction = 0
tank2_direction = 0

bullet_delay = 500
last_shot1 = 0
last_shot2 = 0

leftwon = -1
run = True
canDo = True
while run:
    win.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            import main

    if canDo: keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and tank1_y > 0:
        tank1_y -= tank_speed
    if keys[pygame.K_s] and tank1_y < height - tank_height:
        tank1_y += tank_speed
    if keys[pygame.K_UP] and tank2_y > 0:
        tank2_y -= tank_speed
    if keys[pygame.K_DOWN] and tank2_y < height - tank_height:
        tank2_y += tank_speed

    if keys[pygame.K_SPACE] and pygame.time.get_ticks() - last_shot1 > bullet_delay:
        bullet1_x = tank1_x + tank_width
        bullet1_y = tank1_y + tank_height // 2
        last_shot1 = pygame.time.get_ticks()

    if keys[pygame.K_RETURN] and pygame.time.get_ticks() - last_shot2 > bullet_delay:
        bullet2_x = tank2_x - bullet_radius
        bullet2_y = tank2_y + tank_height // 2
        last_shot2 = pygame.time.get_ticks()

    if bullet1_x > 0:
        bullet1_x += bullet_speed
        if bullet1_x > width:
            bullet1_x = 0

    if bullet2_x > 0:
        bullet2_x -= bullet_speed
        if bullet2_x < 0:
            bullet2_x = 0

    pygame.draw.rect(win, pygame.Color('red'), (tank1_x, tank1_y, tank_width, tank_height))
    pygame.draw.rect(win, pygame.Color('blue'), (tank2_x, tank2_y, tank_width, tank_height))
    pygame.draw.circle(win, pygame.Color('red'), (bullet1_x, bullet1_y), bullet_radius)
    pygame.draw.circle(win, pygame.Color('blue'), (bullet2_x, bullet2_y), bullet_radius)

    font = pygame.font.Font(None, 36)

    if (tank2_x < bullet1_x < tank2_x + tank_width and
            tank2_y < bullet1_y < tank2_y + tank_height):
        print("Победил игрок 1!")
        leftwon = 0
    if (tank1_x < bullet2_x < tank1_x + tank_width and
            tank1_y < bullet2_y < tank1_y + tank_height):
        leftwon = 1
        print("Победил игрок 2!")

    if leftwon == 0:
        bimer_text = font.render("Победитель: Игрок 1", True, pygame.Color("red"))
        win.blit(bimer_text, (50, 10))
    elif leftwon == 1:
        bimer_text = font.render("Победитель: Игрок 2", True, pygame.Color("blue"))
        win.blit(bimer_text, (50, 10))

    if not leftwon == -1:
        canDo = False

    pygame.display.update()

pygame.quit()
sys.exit()
