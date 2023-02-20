import time

import pygame, sys
from bullet import Bullet
from stones import Stones
from stats import Stats
from pygame.sprite import Group
from dino import Dino

bg = pygame.image.load("images/screen pic jungle.jpg")
screen_w = 900
screen_h = 600
screen = pygame.display.set_mode((screen_w, screen_h))
bullets = Group()
stones = Group()

def events(screen, dino):
    """events handling"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
             # shooting - space
                new_bullet = Bullet(screen, dino)
                bullets.add(new_bullet)

def update(screen, dino, bullets, stones):
    """screen update"""
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    dino.output()
    stones.update()
    stones.draw(screen)
    pygame.display.flip()

def update_bullets(screen, bullets):
    """updating bullets position"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.right >= screen_w:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, stones, True, True)
    if collisions:
        #for stones in collisions.values():
            #stats.score += 10 * len(stones)
        bullets.empty()

def dino_kill(stats, screen, dino, stones, bullets):
    """collision of dino and stones"""
    if stats.dino_lives > 0:
        stats.dino_lives -= 1
        stones.empty()
        bullets.empty()
        dino.show_dino()
        stones.show_stones()
        time.sleep(2)
    else:
        stats.run_game = False
        sys.exit()


def stones_update(screen, dino, stones, bullets):
    """stones state"""
    stones.update()
    if pygame.sprite.spritecollideany(dino, stones):
        dino_kill(stats, screen, dino, stones, bullets)



