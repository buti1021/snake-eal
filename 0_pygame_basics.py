import pygame
import time

HOEHE = 300
BREITE = 600
BLAU = (50, 153, 213)
GRUEN = (0, 255, 0)
SCHWARZ = (0, 0, 0)
pygame.init()


fenster = pygame.display.set_mode((BREITE, HOEHE))  # fenster mit größe initialisieren
pygame.draw.rect(
    fenster, BLAU, (0, 0, 20, 20)
)  # obere linke ecke ein blaues quadrat mit den seitenlängen 20 20
pygame.display.update()  # Sonst ändert sich nix
pygame.draw.rect(fenster, GRUEN, (20, 0, 20, 20))  # rechts neben das blaue quadrat ein grünes
pygame.display.update()
start = time.time()
pygame.time.Clock().tick(0.5)  # 0.5 FPS => ungefähr zwei Sekunde
end = time.time()
print(end - start)
fenster.fill(BLAU)  # alles blau machen
font = pygame.font.SysFont("comicsansms", 35)
pygame.draw.rect(fenster, GRUEN, (BREITE, HOEHE, 20, 20))
text = font.render("Keine schöne Schrift D:", True, SCHWARZ)
fenster.blit(text, [50, 100])  # Koordinaten oberes rechtes Eck

pygame.display.update()  # naja eigentlich erst jetzt


run = True
while run:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.KEYDOWN:  # Nur events die ein Tastendruck sind
            if event.key == pygame.K_LEFT:
                print("linke Pfeiltaste gedrückt")
        if event.type == pygame.QUIT:
            run = False
