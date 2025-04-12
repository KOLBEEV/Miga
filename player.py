import pygame
import constant
from animator import Animator
from sound_manager import SoundManager
from constant import HEIGHT


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.animator = Animator(
            sprite_sheet='src/image/player/miga.png',
            frame_width=80,
            frame_height=110,
            animations={
                "idle": (0, 0, 1),
                "run": (1, 0, 2),
                "jump": (0, 1, 1),
                "fall": (0, 2, 1),
            },
            fps=8
        )
        self.facing_left = False
        self.image = self.animator.get_image()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity_y = 0
        self.jumping = False
        self.speed = 5
        self.score = 0
        self.health = 5
        self.sound_manager = SoundManager()

    def update(self):
        moving = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.facing_left = True
            moving = True
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.facing_left = False
            moving = True
        if keys[pygame.K_SPACE]:
            self.jump()

        self.velocity_y += 0.5
        self.rect.y += self.velocity_y

        if self.rect.bottom > constant.HEIGHT - 10:
            self.rect.bottom = HEIGHT - 10
            self.velocity_y = 0
            self.jumping = False

        if self.jumping:
            self.animator.set_animation("jump" if self.velocity_y < 0 else "fall")
        elif moving:
            self.animator.set_animation("run")
        else:
            self.animator.set_animation("idle")

        self.animator.update()
        self.image = self.animator.get_image(flip=self.facing_left)
        self.rect = self.image.get_rect(topleft=self.rect.topleft)

    def jump(self):
        if not self.jumping:
            self.velocity_y = -12
            self.jumping = True

    def check_collision(self, fishes):
        if pygame.sprite.spritecollide(self, fishes, True):
            self.score += 1
            self.sound_manager.play('collect')
            self.sound_manager.play('auf', chance=0.2)

    def damage(self, count=1):
        self.health -= 1
        self.sound_manager.play('damage')
