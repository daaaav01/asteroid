import pygame
from pygame.locals import *
from pygame.sprite import *
import math

class Bullet(Sprite):
    def __init__(self, pos, angle, vel, cont):
        Sprite.__init__(self)
        self.vel = vel
        self.alcance = 25
        self.contenedor = cont
        self.image = pygame.image.load("imagenes/punto.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(pos[0], pos[1])
        self.angule = angle

    def update(self):
        self.alcance -= 1
        self.vel[0] += math.cos(math.radians((self.angule)%360))
        self.vel[1] -= math.sin(math.radians((self.angule)%360))
        self.rect = self.rect.move(self.vel)
        self.rect.x = self.rect.x % self.contenedor[0]
        self.rect.y = self.rect.y % self.contenedor[1]