import pygame
import random
from .base_scene import Scene
import constant


class GameOverScene(Scene):
    def __init__(self, score):
        self.score = score
        self.buyer_prices = {
            "Марат": 0.5, "Александр": 2.0, "Фёдор": 1.0, "Вячеслав": 1.0
        }
        self.font = pygame.font.Font("src/font/LapsusPro.ttf", 40)
        self.small_font = pygame.font.Font("src/font/LapsusPro.ttf", 30)

        self.restart = False
        self.roulette_done = False
        self.roulette_timer = 0
        self.roulette_delay = 2 * constant.FPS

        self.buyers = ["Марат", "Александр", "Фёдор", "Вячеслав"]
        self.current_choice = random.choice(self.buyers)

        self.options = [constant.PLAY_AGAIN, constant.EXIT_TO_MENU]
        self.selected_index = 0
        self._next_scene = None

    def handle_event(self, event):
        if self.roulette_done:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_index = (self.selected_index - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected_index = (self.selected_index + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    if self.selected_index == 0:
                        from .game_scene import GameScene
                        self._next_scene = GameScene()
                    elif self.selected_index == 1:
                        from .menu_scene import MenuScene
                        self._next_scene = MenuScene()

    def update(self):
        if not self.roulette_done:
            self.roulette_timer +=1
            if self.roulette_timer % 10 == 0:
                self.current_choice = random.choice(self.buyers)

            if self.roulette_timer >= self.roulette_delay:
                self.roulette_done = True

        if self.roulette_done and not hasattr(self, "money"):
            rate = self.buyer_prices.get(self.current_choice, 1.0)
            self.money = int(self.score * constant.PRICE * rate)

    def draw(self, screen):
        screen.fill((20, 20, 40))

        panel_width, panel_height = 500, 400
        panel_rect = pygame.Rect(
            (constant.WIDTH - panel_width) // 2,
            (constant.HEIGHT - panel_height) // 2,
            panel_width,
            panel_height
        )

        pygame.draw.rect(screen, (240, 240, 255), panel_rect, border_radius=20)
        pygame.draw.rect(screen, (180, 180, 220), panel_rect, width=4, border_radius=20)

        y_offset = panel_rect.y + 30
        center_x = panel_rect.centerx
        spacing = 40

        title = self.font.render("ИГРА ОКОНЧЕНА", True, (30, 30, 60))
        screen.blit(title, (
            panel_rect.centerx - title.get_width() // 2,
            y_offset
        ))
        y_offset += spacing + 10

        roulette_label = self.small_font.render("Покупатель:", True, (60, 60, 80))
        screen.blit(roulette_label, (
            panel_rect.centerx - roulette_label.get_width() // 2,
            y_offset
        ))
        y_offset += spacing

        roulette_value = self.font.render(self.current_choice, True, (255, 100, 50))
        screen.blit(roulette_value, (
            panel_rect.centerx - roulette_value.get_width() // 2,
            y_offset
        ))
        y_offset += spacing

        fish_text = self.small_font.render(f"Ты собрал {self.score} рыб", True, (60, 60, 80))
        screen.blit(fish_text, (
            panel_rect.centerx - fish_text.get_width() // 2,
            y_offset
        ))
        y_offset += spacing

        if hasattr(self, "money"):
            money_text = self.small_font.render(f"Оплата: {self.money} ₽", True, (0, 100, 0))
            screen.blit(money_text, (
                panel_rect.centerx - money_text.get_width() // 2,
                y_offset
            ))
            y_offset += spacing + 10

        if self.roulette_done:
            for i, option in enumerate(self.options):
                color = (255, 80, 60) if i == self.selected_index else (50, 50, 50)
                text = self.small_font.render(option, True, color)
                text_rect = text.get_rect(center=(center_x, y_offset))
                screen.blit(text, text_rect)
                y_offset += spacing

    def next_scene(self):
        return self._next_scene
