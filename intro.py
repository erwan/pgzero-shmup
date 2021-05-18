import pygame
from actors import Ship

WIDTH = 512
HEIGHT = 256

# Game state
ship = Ship(pos=(50, 50))
bullets = []

# Parameters
speed = 4
bullet_speed = 8

music.play('war')


def update():
    if keyboard.left:
        ship.x -= speed
    if keyboard.right:
        ship.x += speed
    if keyboard.up:
        ship.y -= speed
    if keyboard.down:
        ship.y += speed
    for b in bullets:
        b.x += bullet_speed
        if (b.x > WIDTH):
            bullets.remove(b)


def on_key_down(key):
    if key == keys.SPACE:
        sounds.shot03.play()
        bullets.append(ship.fire())
    if key == keys.ESCAPE:
        exit()


def draw():
    #screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    screen.clear()
    screen.blit('bg/fantasy-512-x-256_006', (0, 0))
    screen.blit('bg/fantasy-512-x-256_005', (0, 0))
    screen.blit('bg/fantasy-512-x-256_004', (0, 0))
    screen.blit('bg/fantasy-512-x-256_003', (0, 0))
    screen.blit('bg/fantasy-512-x-256_002', (0, 0))
    screen.blit('bg/fantasy-512-x-256_001', (0, 0))
    screen.blit('bg/fantasy-512-x-256_000', (0, 0))
    ship.draw()
    for bullet in bullets:
        bullet.draw()
