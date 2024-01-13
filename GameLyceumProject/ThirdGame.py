import pygame
import random

pygame.init()

screen_width = 800
screen_height = 400

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BallColor = WHITE

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ping Pong")

ball_pos = [random.randint(100, screen_width - 100), random.randint(50, screen_height - 50)]
maxspeed = 2
ball_speed = [random.choice([-maxspeed, maxspeed]), random.choice([-maxspeed, maxspeed])]
paddle_width = 10
paddle_height = 60
paddle_1_pos = [50, screen_height // 2 - paddle_height // 2]
paddle_2_pos = [screen_width - 50 - paddle_width, screen_height // 2 - paddle_height // 2]
paddle_speed = 5
score = [0, 0]


def update_screen():
    screen.fill(BLACK)
    pygame.draw.rect(screen, pygame.Color("red"), (paddle_1_pos[0], paddle_1_pos[1], paddle_width, paddle_height))
    pygame.draw.rect(screen, pygame.Color("blue"), (paddle_2_pos[0], paddle_2_pos[1], paddle_width, paddle_height))
    pygame.draw.circle(screen, BallColor, ball_pos, 10)



done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            import main

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_1_pos[1] > 0:
        paddle_1_pos[1] -= paddle_speed
    if keys[pygame.K_s] and paddle_1_pos[1] < screen_height - paddle_height:
        paddle_1_pos[1] += paddle_speed
    if keys[pygame.K_UP] and paddle_2_pos[1] > 0:
        paddle_2_pos[1] -= paddle_speed
    if keys[pygame.K_DOWN] and paddle_2_pos[1] < screen_height - paddle_height:
        paddle_2_pos[1] += paddle_speed

    if paddle_1_pos[0] + paddle_width >= ball_pos[0] >= paddle_1_pos[0]:
        if paddle_1_pos[1] <= ball_pos[1] <= paddle_1_pos[1] + paddle_height:
            ball_speed = [random.choice([-maxspeed, 0]), random.choice([-maxspeed, maxspeed])]
            ball_speed[0] = -ball_speed[0]
            BallColor = pygame.Color("red")
            maxspeed += 0.1


    if paddle_2_pos[0] <= ball_pos[0] <= paddle_2_pos[0] + paddle_width:
        if paddle_2_pos[1] <= ball_pos[1] <= paddle_2_pos[1] + paddle_height:
            ball_speed = [random.choice([0, maxspeed]), random.choice([-maxspeed, maxspeed])]
            ball_speed[0] = -ball_speed[0]
            BallColor = pygame.Color("blue")
            maxspeed += 0.1

    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    if ball_pos[0] >= screen_width - 20:
        if paddle_2_pos[1] <= ball_pos[1] <= paddle_2_pos[1] + paddle_height:
            ball_speed[0] = -ball_speed[0]

        else:
            ball_pos = [screen_width // 2, screen_height // 2]
            ball_speed = [random.choice([-2, 2]), random.choice([-2, 2])]
            score[0] += 1

    if ball_pos[0] <= 20:
        if paddle_1_pos[1] <= ball_pos[1] <= paddle_1_pos[1] + paddle_height:
            ball_speed[0] = -ball_speed[0]
        else:
            ball_pos = [screen_width // 2, screen_height // 2]
            ball_speed = [random.choice([-2, 2]), random.choice([-2, 2])]
            score[1] += 1

    if ball_pos[1] >= screen_height - 10 or ball_pos[1] <= 10:
        ball_speed[1] = -ball_speed[1]

    update_screen()

    font = pygame.font.Font(None, 36)
    text = font.render(str(score[0]) + " : " + str(score[1]), True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = (screen_width // 2, 20)
    screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
