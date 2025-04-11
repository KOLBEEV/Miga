import pygame
import constant
import random

class Fish(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(
            surface=pygame.image.load('src/image/fish/fish1.png').convert_alpha(),
            size=(90, 30)
        )
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, constant.WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed_y = 2

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > constant.HEIGHT:
            self.kill()
