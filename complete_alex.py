import pygame
from collections import namedtuple
import random

SCHWARZ = (100, 100, 100)
BLAU = (0, 0, 0)
GRUEN = (0,255,0)
ROT = (100, 100 , 100)
Block = namedtuple("Block", ("x", "y"))


BLOCK_GROESSE = 10
# Breite & Höhe muss durch doppelte Blockgröße teilbar sein
BREITE = 300
HOEHE = 300

pygame.init()
fenster = pygame.display.set_mode((BREITE, HOEHE))  # fenster mit größe initialisieren


def draw_snake(snake: list[tuple]) -> None:
    for b in snake:
        pygame.draw.rect(fenster, SCHWARZ, [b.x+1, b.y+1, BLOCK_GROESSE-1, BLOCK_GROESSE-1])

def draw_apple(apple) -> None:
    pygame.draw.rect(fenster, GRUEN, apple)

def is_collision(snake, snake_head):
    if (snake_head[0] == BREITE or snake_head[1] == HOEHE or snake_head[0] < 0 or snake_head[1] < 0):
        return True
    for snakePart in snake:
        if (snakePart[0] == snake_head[0] and snakePart[1] == snake_head[1]):
            return True
    return False


def update_snake_and_draw(snake: list[tuple], snake_head: tuple, apple: tuple):
    fenster.fill(BLAU)
    snake.append(snake_head)
    draw_snake(snake)
    draw_apple(apple)
    pygame.display.update()

def random_number():
    return random.randrange(0, HOEHE, BLOCK_GROESSE)

def game_loop():
    # Starten in (fast) der Mitte
    snake_head = Block(x=BREITE / 2, y=HOEHE / 2)
    snake_middle = Block(x=BREITE / 2 - BLOCK_GROESSE, y=HOEHE / 2)
    snake_end = Block(x=BREITE / 2 - (BLOCK_GROESSE * 2), y=HOEHE / 2)

    apple = [random_number(), random_number(), BLOCK_GROESSE - 1, BLOCK_GROESSE - 1]

    snake = [snake_end, snake_middle, snake_head]
    spiel_laeuft = True
    direction = 1
    while spiel_laeuft:
        if (direction == 1):
            snake_head = Block(snake_head.x + BLOCK_GROESSE, snake_head.y)
        elif (direction == 2):
            snake_head = Block(snake_head.x - BLOCK_GROESSE, snake_head.y)
        elif (direction == 3):
            snake_head = Block(snake_head.x, snake_head.y - BLOCK_GROESSE)
        elif (direction == 4):
            snake_head = Block(snake_head.x, snake_head.y + BLOCK_GROESSE)

        if (snake_head[0] == apple[0] and snake_head[1] == apple[1]):
            apple = [random_number(), random_number(), BLOCK_GROESSE - 1, BLOCK_GROESSE - 1]
        else:
            snake.pop(0)
            if (is_collision(snake, snake_head)):
                spiel_laeuft = False
        update_snake_and_draw(snake, snake_head, apple)



        pygame.time.Clock().tick(20)
        for event in pygame.event.get():
            if (
                event.type == pygame.QUIT
                or event.type == pygame.KEYDOWN
                and event.key == pygame.K_q
            ):
                spiel_laeuft = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if (direction != 1):
                        direction = 2
                    print("leftkey")
                elif event.key == pygame.K_RIGHT:
                    if (direction != 2):
                        direction = 1
                    print("rightkey")
                elif event.key == pygame.K_UP:
                    print("upkey")
                    if (direction != 4):
                        direction = 3

                elif event.key == pygame.K_DOWN:
                    print("downkey")
                    if (direction != 3):
                        direction = 4


if __name__ == "__main__":
    game_loop()
