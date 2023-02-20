import pygame
meteorite_gap = 200
meteorite_frequency = 1500
scroll_speed = 4

class Stones(pygame.sprite.Sprite):
    """falling meteorit class"""

    def __init__(self, x, y, screen):
        """initialize and set 0 position"""
        super(Stones, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/meteorit on fire.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.flip(self.image, False, True)
        self.rect.bottomleft = [x,y - int(meteorite_gap/2)]


    def show_stones(self):
        self.screen.blit(self.image, self.rect)
        self.rect.bottomleft

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()




