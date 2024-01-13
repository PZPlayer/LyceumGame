import pygame
import sys

pygame.init()

window_width = 400
window_height = 200

white = (255, 255, 255)
black = (0, 0, 0)


class Player:
    def __init__(self, key):
        self.key = key
        self.clicks = 0
        self.timer = 10

    def update(self):
        if self.timer > 0:
            self.timer -= 0.0001

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == self.key:
            print("gfd")
            self.clicks += 1
            if self.timer == 10:
                self.timer = 10


player1 = Player(pygame.K_LSHIFT)
player2 = Player(pygame.K_RCTRL)

window1 = pygame.display.set_mode((window_width, window_height))
window2 = pygame.display.set_mode((window_width, window_height))

font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            import main
        if player1.timer > 0:
            player1.handle_event(event)
            player2.handle_event(event)

    player1.update()
    player2.update()

    window1.fill(white)
    window2.fill(white)

    if player1.timer < 0:

        if player1.clicks > player2.clicks:
            print(1)
            bimer_text = font.render("Победитель: Игрок 1", True, pygame.Color("blue"))
            window1.blit(bimer_text, (50, 10))
            pygame.display.flip()
        elif player2.clicks > player1.clicks:
            bimer_text = font.render("Победитель: Игрок 2", True, pygame.Color("red"))
            window2.blit(bimer_text, (50, 10))
            pygame.display.flip()
            print(2)
        else:
            print(3)
            bimer_text = font.render("Ничья", True, pygame.Color("green"))
            window2.blit(bimer_text, (50, 10))
            pygame.display.flip()
    else:
        btn_text = font.render("Нажми LShift", True, pygame.Color("blue"))
        timer_text = font.render(str(round(int(player1.timer), 2)), True, black)
        window1.blit(btn_text, (window_width / 2 + btn_text.get_width() / 5, window_height / 2 - btn_text.get_height()))
        window1.blit(timer_text, (10, 10))

        btn_text = font.render("Нажми RCntrl", True, pygame.Color("red"))
        timer_text = font.render(str(round(int(player2.timer), 2)), True, black)
        window2.blit(btn_text, (window_width / 2 - btn_text.get_width(), window_height / 2 - btn_text.get_height()))
        window2.blit(timer_text, (10, 10))
        pygame.display.flip()
