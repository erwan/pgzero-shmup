import pygame
from pygame.locals import *
from pygame.math import Vector2
from pygame.sprite import Sprite

WIDTH = 512
HEIGHT = 256

speed = 1


class Bullet(Sprite):
    def __init__(self, pos):
        Sprite.__init__(self)
        self.image = pygame.image.load('images/projectile.png')
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        self.rect.move_ip(4, 0)


class Ship(Sprite):
    def __init__(self, pos):
        Sprite.__init__(self)
        self.image = pygame.image.load('images/ship/blue-01.png')
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -4)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 4)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-4, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(4, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

    def fire(self):
        bullet = Bullet(pos=self.rect.center)
        return bullet
