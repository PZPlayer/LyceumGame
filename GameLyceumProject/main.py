import pygame
import sys
import time

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

WHITE = (255, 255, 255)
LIGHT_BLUE = (135, 206, 250)
DARK_BLUE = (70, 130, 180)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Меню")

font = pygame.font.Font(None, 36)

class Button:
    def __init__(self, x, y, width, height, color, hover_color, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.action = action

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.color = self.hover_color
            else:
                self.color = DARK_BLUE

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()

def play():
    print("Запускаем игру!")

rainbow_colors = [
    (255, 0, 0),  # Красный
    (255, 165, 0),  # Оранжевый
    (255, 255, 0),  # Желтый
    (0, 128, 0),  # Зеленый
    (0, 0, 255),  # Синий
    (75, 0, 130),  # Индиго
    (238, 130, 238)  # Фиолетовый
]

font = pygame.font.Font(None, 70)

text_surface = font.render("Double Game", True, rainbow_colors[0])

text_rect = text_surface.get_rect()
text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 5)


def exit_game():
    pygame.quit()
    sys.exit()


start_button = Button(100, 100, 200, 50, DARK_BLUE, LIGHT_BLUE, "Запуск", play)
exit_button = Button(100, 180, 200, 50, DARK_BLUE, LIGHT_BLUE, "Выход", exit_game)
color_index = 0
prev_time = time.time()

while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        start_button.handle_event(event)
        exit_button.handle_event(event)

    current_time = time.time()
    if current_time - prev_time >= 1:
        color_index = (color_index + 1) % len(rainbow_colors)
        text_surface = font.render("Double Game", True, rainbow_colors[color_index])
        prev_time = current_time

    start_button.draw()
    exit_button.draw()
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

