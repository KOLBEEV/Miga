import pygame
import random
from .base_scene import Scene
import constant
from constant import HEIGHT


class GameOverScene(Scene):
    def __init__(self):
        self.font = pygame.font.Font("src/font/LapsusPro.ttf", 40)
        self.small_font = pygame.font.Font("src/font/LapsusPro.ttf", 30)

        self.restart = False
        self.roulette_done = False
        self.roulette_timer = 0
        self.roulette_delay = 2 * constant.FPS

        self.buyers = ["Марат", "Александр", "Фёдор", "Вячеслав"]
        self.current_choice = random.choice(self.buyers)

    def handle_event(self, event):
        if self.roulette_done:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.restart = True

    def update(self):
        if not self.roulette_done:
            self.roulette_timer +=1
            if self.roulette_timer % 10 == 0:
                self.current_choice = random.choice(self.buyers)

            if self.roulette_timer >= self.roulette_delay:
                self.roulette_done = True

    def draw(self, screen):
        screen.fill((30, 0, 0))

        title = self.font.render("Игра окончена", True, (255, 255, 255))
        screen.blit(title, (constant.WIDTH // 2 - title.get_width() // 2, 100))

        roulette_text = self.small_font.render(f"Покупатель: {self.current_choice}", True, (255, 255, 0))
        screen.blit(roulette_text, (constant.WIDTH // 2 - roulette_text.get_width() // 2, 200))

        if self.roulette_done:
            msg = self.font.render("Нажми ENTER чтобы сыграть заново", True, (255, 255, 255))
            screen.blit(msg, (constant.WIDTH // 2 - msg.get_width() // 2, 300))

    def next_scene(self):
        if self.restart:
            from .game_scene import GameScene
            return GameScene()

        return None
