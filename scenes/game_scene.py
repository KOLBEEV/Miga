import pygame
from .base_scene import Scene
from background import Background
from player import Player
from fish import Fish
from fish_handler import handle_fish_falls
import constant


class GameScene(Scene):
    def __init__(self):
        self.font = pygame.font.Font("src/font/LapsusPro.ttf", 30)
        self.background = Background((constant.WIDTH, constant.HEIGHT))
        self.player = Player(constant.WIDTH / 2, constant.HEIGHT - 10)
        self.all_sprites = pygame.sprite.Group(self.player)
        self.fishes = pygame.sprite.Group()
        self.spawn_timer = 0

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    def update(self):
        self.spawn_timer += 1
        if self.spawn_timer >= 60:
            fish = Fish()
            self.fishes.add(fish)
            self.all_sprites.add(fish)
            self.spawn_timer = 0

        self.all_sprites.update()
        self.player.check_collision(self.fishes)
        handle_fish_falls(self.fishes, self.player)

    def draw(self, screen):
        screen.fill(constant.SKY)
        self.background.draw(screen)
        self.all_sprites.draw(screen)

        score_text = self.font.render(f"Риба: {self.player.score}", True, (0, 0, 0))
        health_text = self.font.render(f"Здоровье: {self.player.health}", True, (255, 0, 0))
        screen.blit(score_text, (10, 10))
        screen.blit(health_text, (10, 50))

    def next_scene(self):
        if self.player.health <= 0:
            from .game_over_scene import GameOverScene
            return GameOverScene()

        return None
