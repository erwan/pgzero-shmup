import pygame
from pygame.locals import *
from actors import Ship

WIDTH = 512
HEIGHT = 256

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

running = True

# Game state
ship = Ship((50, 50))
all_sprites.add(ship)
bullets = []

# Parameters
speed = 4
bullet_speed = 8

# music.play('war')


def input():
    pressed_keys = pygame.key.get_pressed()
    ship.update(pressed_keys)
    if pressed_keys[K_SPACE]:
        bullet = ship.fire()
        bullets.append(bullet)
        all_sprites.add(bullet)


def draw():
    bg = pygame.image.load('images/bg/fantasy-512-x-256_006.png')
    screen.blit(bg, (0, 0))

    all_sprites.draw(screen)
    pygame.display.flip()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tick at 60 fps
    clock.tick(60)

    for bullet in bullets:
        bullet.update()

    input()
    draw()


pygame.quit()


# def update():
#     for b in bullets:
#         b.x += bullet_speed
#         if (b.x > WIDTH):
#             bullets.remove(b)


# Def on_key_down(key):
#     if key == keys.SPACE:
#         sounds.shot03.play()
#         bullets.append(ship.fire())
#     if key == keys.ESCAPE:
#         exit()
