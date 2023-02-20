import pygame, controls
from pygame.sprite import Group
from dino import Dino
from bullet import Bullet
from stones import Stones


def run():
    pygame.init()
    fps = 60
    clock = pygame.time.Clock()
    screen_w = 900
    screen_h = 600
    screen = pygame.display.set_mode((screen_w, screen_h))
    pygame.display.set_caption("Save the Dino!")
    game_over = False
    meteorite_gap = 200
    meteorite_frequency = 1500
    bg = pygame.image.load("images/screen pic jungle.jpg")
    pygame.time.delay(30)
    dino = Dino(screen)
    bullets = Group()
    stones = Group()


    while run:
        controls.events(screen, dino)
        #clock.tick(fps)
        screen.blit(bg, (0,0))
        dino.show_dino()
        bullets.draw(screen)
        controls.update(screen, dino, bullets, stones)
        dino.update()
        pygame.display.update()

run()


