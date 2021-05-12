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
    spiel_laeuft = True
    fenster.fill(BLAU)
    pygame.draw.rect(fenster, SCHWARZ, [10, 20, BLOCK_GROESSE, BLOCK_GROESSE])
    pygame.display.update()
    while spiel_laeuft:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spiel_laeuft = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("leftkey")


if __name__ == "__main__":
    game_loop()
