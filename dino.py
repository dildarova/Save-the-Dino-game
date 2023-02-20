import pygame
from pygame.sprite import Sprite

screen_w = 900
screen_h = 600

class Dino(Sprite):

    def __init__ (self, screen):
        """initializing Dino"""
        super(Dino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("images/shooting dino.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.y = 550
        self.rect.bottom = self.screen_rect.bottom
        self.jumping = False
        self.moving = "STOP"

    def output(self):
        """drawing Dino"""
        self.screen.blit(self.image, self.rect)

    def show_dino(self):
        """places Dino on its position"""
        self.center = self.screen_rect.bottom

    def update(self):
        """Dino position update"""
        if self.moving == "LEFT":
            self.rect.x -= 5
        if self.moving == "RIGHT":
            self.rect.x += 5
        if self.moving == "JUMP":
            self.rect.y -= 10
        if self.moving == "DOWN":
            self.rect.y += 10
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.moving = "RIGHT"
                if event.key == pygame.K_LEFT:
                    self.moving = "LEFT"
                if event.key == pygame.K_UP:
                    self.moving = "JUMP"
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                    self.moving = "STOP"
                if event.key == pygame.K_UP:
                    self.moving = "DOWN"
        #self.rect.x = self.speed
        if self.rect.right > screen_w:
            self.rect.right = screen_w
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > screen_h:
            self.rect.bottom = screen_h
        if self.rect.top < 0:
            self.rect.top = 0













