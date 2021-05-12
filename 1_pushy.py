import pygame

SCHWARZ = "black"
BLAU = (50, 153, 213)
GRUEN = (0, 255, 0)

BLOCK_GROESSE = 40
# Breite & Höhe muss durch doppelte Blockgröße teilbar sein
BREITE = 800
HOEHE = 720

pygame.init()
fenster = pygame.display.set_mode((BREITE, HOEHE))  # fenster mit größe initialisieren


def game_loop():
    # Starten in (fast) der Mitte
    x1 = BREITE / 2
    y1 = HOEHE / 2
    spiel_laeuft = True
    while spiel_laeuft:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spiel_laeuft = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("leftkey")
                    x1 -= BLOCK_GROESSE
                elif event.key == pygame.K_RIGHT:
                    print("rightkey")
                    x1 += BLOCK_GROESSE
                elif event.key == pygame.K_UP:
                    print("upkey")
                    y1 -= BLOCK_GROESSE
                elif event.key == pygame.K_DOWN:
                    print("downkey")
                    y1 += BLOCK_GROESSE
            fenster.fill(BLAU)
            pygame.draw.rect(fenster, SCHWARZ, [x1, y1, BLOCK_GROESSE, BLOCK_GROESSE])
            pygame.display.update()


if __name__ == "__main__":
    game_loop()
