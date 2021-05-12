import pygame
import time

pygame.init()
BREITE = 960
HOEHE = 720
BLAU = (50, 153, 213)
GRUEN = (0, 255, 0)
SCHWARZ = (0, 0, 0)
fenster = pygame.display.set_mode((BREITE, HOEHE))
x = 0
y = 0
pygame.draw.rect(fenster, "blue", (x, y, 20, 20))
pygame.display.update()
run = True
while run:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.KEYDOWN:  # Nur events die ein Tastendruck sind
            if event.key == pygame.K_LEFT:
                print("linke Pfeiltaste gedrückt")
        if event.type == pygame.QUIT:
            run = False
