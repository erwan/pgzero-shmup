from os import stat
import pygame
from actors import Background, Ship

WIDTH = 512
HEIGHT = 256

# Game state


class GameState:
    ship = Ship(pos=(50, 50))
    bullets = []
    backgrounds = [
        Background('bg/fantasy-512-x-256_006', 0, WIDTH, HEIGHT),
        Background('bg/fantasy-512-x-256_005', 1, WIDTH, HEIGHT),
        Background('bg/fantasy-512-x-256_004', 2, WIDTH, HEIGHT),
        Background('bg/fantasy-512-x-256_003', 1, WIDTH, HEIGHT),
        Background('bg/fantasy-512-x-256_002', 2, WIDTH, HEIGHT),
        Background('bg/fantasy-512-x-256_001', 3, WIDTH, HEIGHT),
    ]


state = GameState()

# Parameters
speed = 4
bullet_speed = 8

music.play('war')


def update():
    # Keyboard input
    if keyboard.left:
        state.ship.x -= speed
    if keyboard.right:
        state.ship.x += speed
    if keyboard.up:
        state.ship.y -= speed
    if keyboard.down:
        state.ship.y += speed
    # Move bullets forward
    for b in state.bullets:
        b.x += bullet_speed
        if (b.x > WIDTH):
            state.bullets.remove(b)
    # Background scrolling
    for bg in state.backgrounds:
        bg.update()


def on_key_down(key):
    if key == keys.SPACE:
        sounds.shot03.play()
        state.bullets.append(state.ship.fire())
    if key == keys.ESCAPE:
        exit()


def draw():
    screen.surface = pygame.display.set_mode(
        (WIDTH, HEIGHT), pygame.FULLSCREEN)
    screen.clear()
    for bg in state.backgrounds:
        bg.draw(screen)
    state.ship.draw()
    for bullet in state.bullets:
        bullet.draw()
