import pygame
import constant
import random
from utils import resource_path


class Fish(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(
            surface=pygame.image.load(resource_path('src/image/fish/fish1.png')).convert_alpha(),
            size=(90, 30)
        )
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, constant.WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed_y = 2

    def update(self):
        self.rect.y += self.speed_y
