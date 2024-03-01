import pygame
from pygame.locals import *
import sys
from ship import *

size = width, height = 800, 600

screen = pygame.display.set_mode(size)

def main():
    pygame.init()

    background_image = pygame.image.load("imagenes\space.png")
    background_rect = background_image.get_rect()

    pygame.display.set_caption("Asteroid")

    ship = Ship(size)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        ship.update()
        screen.blit(background_image, background_rect)
        screen.blit(ship.imagen, ship.rect)
        pygame.display.update()
        pygame.time.delay(10)

if __name__ == "__main__":
    main()