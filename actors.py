from os import supports_effective_ids
from pgzero.actor import Actor
from pygame.math import Vector2


class Ship(Actor):
    def __init__(self, **kwargs):
        super(Ship, self).__init__('ship/blue-01.png', **kwargs)

    def fire(self):
        bullet = Actor('projectile', pos=self.pos)
        bullet.exact_pos = bullet.start_pos = Vector2(self.pos)
        return bullet


class Background():
    def __init__(self, image, speed, width, height):
        self.image = image
        self.speed = speed
        self.width = width
        self.height = height
        self.offset = 0

    def update(self):
        self.offset += self.speed
        if self.offset > self.width:
            self.offset = 0

    def draw(self, screen):
        screen.blit(self.image, (-self.offset, 0))
        screen.blit(self.image, (self.width - self.offset, 0))
