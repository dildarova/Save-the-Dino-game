import pygame
from pygame.sprite import Sprite

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, dino):
        """creating bullets shooting from the dino's gun"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 10, 2)
        self.color = 237, 28, 35
        self.speed = 5
        self.rect.centerx = dino.rect.centerx
        self.rect.right = dino.rect.right
        self.x = float(self.rect.x)

    def update(self):
        """bullet moving"""
        self.x += self.speed
        self.rect.x = self.x

    def draw_bullet(self):
        """drawing bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
