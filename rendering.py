import pygame
import os
import classes

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1200, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

font50 = pygame.font.SysFont(None, 50)

BLUE = (30, 30, 100)

BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)

BULLET_FIRE_SOUND = pygame.mixer.Sound("assets/Gun+Silencer.mp3")

FPS = 12


SHIP_IMAGE = pygame.image.load(os.path.join("assets", "ship.png"))
SHIP = pygame.transform.scale(SHIP_IMAGE, (classes.SHIP_WIDTH, classes.SHIP_HEIGHT))



SETTLEMENT_IMAGE = pygame.image.load(os.path.join("assets", "palm.png"))
SETTLEMENT = pygame.transform.scale(
    SETTLEMENT_IMAGE, (classes.SETTLEMENT_WIDTH, classes.SETTLEMENT_HEIGHT)
)


class RadioButton(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, font, text):
        super().__init__()
        text_surf = font.render(text, True, (0, 0, 0))
        self.button_image = pygame.Surface((w, h))
        self.button_image.fill((96, 96, 96))
        self.button_image.blit(text_surf, text_surf.get_rect(center=(w // 2, h // 2)))
        self.hover_image = pygame.Surface((w, h))
        self.hover_image.fill((96, 96, 96))
        self.hover_image.blit(text_surf, text_surf.get_rect(center=(w // 2, h // 2)))
        pygame.draw.rect(
            self.hover_image, (96, 196, 96), self.hover_image.get_rect(), 3
        )
        self.clicked_image = pygame.Surface((w, h))
        self.clicked_image.fill((96, 196, 96))
        self.clicked_image.blit(text_surf, text_surf.get_rect(center=(w // 2, h // 2)))
        self.image = self.button_image
        self.rect = pygame.Rect(x, y, w, h)
        self.clicked = False
        self.buttons = None

    def setRadioButtons(self, buttons):
        self.buttons = buttons

    def update(self, event):
        hover = self.rect.collidepoint(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONDOWN:
            if hover and event.button == 1:
                for rb in self.buttons:
                    rb.clicked = False
                self.clicked = True

        self.image = self.button_image
        if self.clicked:
            self.image = self.clicked_image
        elif hover:
            self.image = self.hover_image


radioButtons = [
    RadioButton(50, 40, 200, 60, font50, "Trade with Florida Keyes"),
    RadioButton(50, 120, 200, 60, font50, "Build ship"),
    RadioButton(50, 200, 200, 60, font50, "other"),
]
for rb in radioButtons:
    rb.setRadioButtons(radioButtons)
radioButtons[0].clicked = True

group = pygame.sprite.Group(radioButtons)

def show_menu():
    group.draw(WIN)
    
    for rb in radioButtons:
        rb.update(event)
    pygame.display.update() 

def draw_window():
    WIN.fill(BLUE)
    pygame.display.update()

    return None


def draw_player_elements(player: classes.Player):
    for sh in player.ships:
        WIN.blit(SHIP, (sh.position[0], sh.position[1]))
    for setl in player.settlements:
        WIN.blit(SETTLEMENT, (setl.position[0], setl.position[1]))
    pygame.display.update()

    return None

