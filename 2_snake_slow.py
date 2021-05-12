import pygame
from collections import namedtuple

SCHWARZ = (0, 0, 0)
BLAU = (50, 153, 213)
GRUEN = (0, 255, 0)
ROT = (100, 50, 50)
Block = namedtuple("Block", ("x", "y"))


BLOCK_GROESSE = 40
# Breite & Höhe muss durch doppelte Blockgröße teilbar sein
BREITE = 800
HOEHE = 720

pygame.init()
fenster = pygame.display.set_mode((BREITE, HOEHE))  # fenster mit größe initialisieren


def draw_snake(snake: list[tuple]) -> None:
    for b in snake[:-1]:
        pygame.draw.rect(fenster, SCHWARZ, [b.x + 1, b.y + 1, BLOCK_GROESSE - 1, BLOCK_GROESSE - 1])
    pygame.draw.rect(
        fenster, ROT, [snake[-1].x + 1, snake[-1].y + 1, BLOCK_GROESSE - 1, BLOCK_GROESSE - 1]
    )


def update_snake_and_draw(snake: list[tuple], snake_head: tuple):
    fenster.fill(BLAU)
    snake.append(snake_head)
    snake.pop(0)
    draw_snake(snake)
    pygame.display.update()


def game_loop():
    # Starten in (fast) der Mitte
    snake_head = Block(x=BREITE / 2, y=HOEHE / 2)
    snake_middle = Block(x=BREITE / 2 - BLOCK_GROESSE, y=HOEHE / 2)
    snake_end = Block(x=BREITE / 2 - (BLOCK_GROESSE * 2), y=HOEHE / 2)

    snake = [snake_end, snake_middle, snake_head]
    spiel_laeuft = True
    while spiel_laeuft:
        for event in pygame.event.get():
            if (
                event.type == pygame.QUIT
                or event.type == pygame.KEYDOWN
                and event.key == pygame.K_q
            ):
                spiel_laeuft = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("leftkey")
                    snake_head = Block(snake_head.x - BLOCK_GROESSE, snake_head.y)
                    update_snake_and_draw(snake, snake_head)
                elif event.key == pygame.K_RIGHT:
                    print("rightkey")
                    snake_head = Block(snake_head.x + BLOCK_GROESSE, snake_head.y)
                    update_snake_and_draw(snake, snake_head)
                elif event.key == pygame.K_UP:
                    print("upkey")
                    snake_head = Block(snake_head.x, snake_head.y - BLOCK_GROESSE)
                    update_snake_and_draw(snake, snake_head)
                elif event.key == pygame.K_DOWN:
                    print("downkey")
                    snake_head = Block(snake_head.x, snake_head.y + BLOCK_GROESSE)
                    update_snake_and_draw(snake, snake_head)


if __name__ == "__main__":
    game_loop()
