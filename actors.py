from pgzero.actor import Actor
from pygame.math import Vector2


class Ship(Actor):
    def __init__(self, **kwargs):
        super(Ship, self).__init__('ship/blue-01.png', **kwargs)

    def fire(self):
        bullet = Actor('projectile', pos=self.pos)
        bullet.exact_pos = bullet.start_pos = Vector2(self.pos)
        return bullet
