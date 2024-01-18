import pygame
import sys
import time
import sqlite3

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

WHITE = (255, 255, 255)
LIGHT_BLUE = (135, 206, 250)
DARK_BLUE = (70, 130, 180)

window_width = 400
window_height = 200

white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Меню")

font = pygame.font.Font(None, 36)


def save_data(name, quantity):
    conn = sqlite3.connect('films_db (1).sqlite')
    cursor = conn.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS items (name TEXT, quantity INTEGER)')

    cursor.execute('INSERT INTO items VALUES (?, ?)', (name, quantity))

    conn.commit()
    conn.close()


def update_quantity(name, new_quantity):
    conn = sqlite3.connect('films_db (1).sqlite')
    cursor = conn.cursor()

    cursor.execute('UPDATE items SET quantity=? WHERE name=?', (new_quantity, name))

    conn.commit()
    conn.close()


def get_cell_value(name):
    conn = sqlite3.connect('films_db (1).sqlite')
    cursor = conn.cursor()

    cursor.execute(f"SELECT quantity FROM items WHERE name = '{name}'")
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return result[0]
    else:
        return None




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


def clickerStart():
    import Clciker


def shootStart():
    import SecGame


def pinpong():
    import ThirdGame


def play():
    pygame.init()
    width, height = 400, 400
    screen2 = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Button Panel")
    clock = pygame.time.Clock()

    button_color1 = (255, 0, 0)
    button_color2 = (0, 255, 0)
    button_color3 = (0, 0, 255)
    button_color4 = (255, 255, 0)
    exit_color = (255, 255, 255)

    button_width = 100
    button_height = 50
    button_padding = 20

    button_x = (width - (button_width * 2) - button_padding) // 2
    button_y = (height - (button_height * 2) - button_padding) // 2

    is_running = True

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(event.pos):
                    clickerStart()
                elif button2.collidepoint(event.pos):
                    shootStart()
                elif button3.collidepoint(event.pos):
                    pinpong()
                elif button4.collidepoint(event.pos):
                    print("Button 4 clicked")
                elif exit_button.collidepoint(event.pos):
                    is_running = False

        screen2.fill((0, 0, 0))

        button1 = pygame.draw.rect(screen2, button_color1, (button_x, button_y, button_width, button_height))
        button2 = pygame.draw.rect(screen2, button_color2,
                                   (button_x + button_width + button_padding, button_y, button_width, button_height))
        button3 = pygame.draw.rect(screen2, button_color3,
                                   (button_x, button_y + button_height + button_padding, button_width, button_height))
        button4 = pygame.draw.rect(screen2, button_color4, (
            button_x + button_width + button_padding, button_y + button_height + button_padding, button_width,
            button_height))
        exit_button = pygame.draw.rect(screen2, exit_color, (0, 0, button_width, button_height))
        pygame.display.flip()
        clock.tick(60)


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
fontsec = pygame.font.Font(None, 30)

text_surface = font.render("Double Game", True, rainbow_colors[0])
textsurf = fontsec.render(f"Money:{get_cell_value('Money')}", True, pygame.Color("green"))

text_rect = text_surface.get_rect()
textrect = textsurf.get_rect()
textrect = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 18)
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
    screen.blit(textsurf, textrect)
    pygame.display.flip()
