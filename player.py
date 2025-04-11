import pygame
import constant
from sound_manager import SoundManager
from constant import HEIGHT


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((60, 100))
        self.image.fill(constant.BLUE)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity_y = 0
        self.jumping = False
        self.speed = 5
        self.score = 0
        self.health = 5
        self.sound_manager = SoundManager()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE]:
            self.jump()

        self.velocity_y += 0.5
        self.rect.y += self.velocity_y

        if self.rect.bottom > constant.HEIGHT - 10:
            self.rect.bottom = HEIGHT - 10
            self.velocity_y = 0
            self.jumping = False

    def jump(self):
        if not self.jumping:
            self.velocity_y = -12
            self.jumping = True

    def check_collision(self, fishes):
        if pygame.sprite.spritecollide(self, fishes, True):
            self.score += 1
            self.sound_manager.play('collect')
            self.sound_manager.play('auf', chance=0.2)
