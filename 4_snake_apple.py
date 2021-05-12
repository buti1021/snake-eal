import pygame
import random
from collections import namedtuple

SCHWARZ = (0, 0, 0)
BLAU = (50, 153, 213)
GRUEN = (0, 255, 0)
Block = namedtuple("Block", ("x", "y"))


BLOCK_GROESSE = 40
# Breite & Höhe muss durch doppelte Blockgröße teilbar sein
BREITE = 800
HOEHE = 720

pygame.init()
fenster = pygame.display.set_mode((BREITE, HOEHE))  # fenster mit größe initialisieren


def draw_snake(snake: list[tuple]) -> None:
    for b in snake:
        draw_square(b, SCHWARZ)


def draw_square(block: tuple[int], color: tuple[int]):
    pygame.draw.rect(fenster, color, [block.x, block.y, BLOCK_GROESSE, BLOCK_GROESSE])


def update_snake_and_draw(snake: list[tuple], snake_head: tuple, apple: tuple):
    fenster.fill(BLAU)
    snake.append(snake_head)
    snake.pop(0)
    draw_snake(snake)
    draw_square(apple, GRUEN)
    pygame.display.update()


def game_loop():
    # Starten in (fast) der Mitte
    snake_head = Block(x=BREITE / 2, y=HOEHE / 2)
    snake_middle = Block(x=BREITE / 2 - BLOCK_GROESSE, y=HOEHE / 2)
    snake_end = Block(x=BREITE / 2 - (BLOCK_GROESSE * 2), y=HOEHE / 2)
    apple = Block(
        x=random.randrange(0, BREITE, BLOCK_GROESSE),
        y=random.randrange(0, HOEHE, BLOCK_GROESSE),
    )
    snake = [snake_end, snake_middle, snake_head]
    draw_square(apple, GRUEN)
    draw_snake(snake)
    pygame.display.update()
    spiel_laeuft = True
    x_change = 0
    y_change = 0
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
                    x_change = -BLOCK_GROESSE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    print("rightkey")
                    x_change = +BLOCK_GROESSE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    print("upkey")
                    x_change = 0
                    y_change = -BLOCK_GROESSE
                elif event.key == pygame.K_DOWN:
                    print("downkey")
                    x_change = 0
                    y_change = +BLOCK_GROESSE
        snake_head = Block(snake_head.x + x_change, snake_head.y + y_change)
        print(apple)
        if snake_head == apple:
            print(apple)
            apple = Block(
                x=random.randrange(0, BREITE, BLOCK_GROESSE),
                y=random.randrange(0, HOEHE, BLOCK_GROESSE),
            )
            draw_square(apple, GRUEN)
            pygame.display.update()
        update_snake_and_draw(snake, snake_head, apple)
        pygame.time.Clock().tick(10)


if __name__ == "__main__":
    game_loop()
