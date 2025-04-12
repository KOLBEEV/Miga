import pygame
from .base_scene import Scene
import constant
import requests


class MenuScene(Scene):
    def __init__(self):
        self.font = pygame.font.Font("src/font/LapsusPro.ttf", 40)
        self.small_font = pygame.font.Font("src/font/LapsusPro.ttf", 28)

        self.options = [constant.START_GAME, constant.TRAIN, constant.SHOP, constant.SETTINGS, constant.EXIT]
        self.selected_index = 0

        self.records = self.fetch_records()

    def fetch_records(self):
        try:
            url = "https://miga-score-server.onrender.com/top"
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"[Ошибка загрузки рекордов]: {e}")

        return [
            ("Игрок1", 0),
            ("Игрок2", 0),
            ("Игрок3", 0),
            ("Игрок4", 0),
            ("Игрок5", 0),
            ("Игрок6", 0),
        ]

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.selected_index = (self.selected_index + 1) % len(self.options)
            elif event.key == pygame.K_UP:
                self.selected_index = (self.selected_index - 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                selected_option = self.options[self.selected_index]
                if selected_option == constant.START_GAME:
                    from .game_scene import GameScene
                    self._next_scene = GameScene()
                elif selected_option == constant.EXIT:
                    pygame.quit()
                    exit()

    def update(self):
        pass

    def draw(self, screen):
        screen.fill(constant.SKY)

        menu_rect = pygame.Rect(80, 100, 400, 400)
        pygame.draw.rect(screen, (240, 240, 255), menu_rect, border_radius=20)
        pygame.draw.rect(screen, (180, 180, 220), menu_rect, width=4, border_radius=20)

        start_y = menu_rect.y + 30
        spacing = 60

        for i, option in enumerate(self.options):
            is_selected = i == self.selected_index

            button_rect = pygame.Rect(menu_rect.x + 20, start_y + i * spacing, 360, 50)
            bg_color = (200, 220, 255) if is_selected else (255, 255, 255)
            text_color = (20, 20, 40) if is_selected else (60, 60, 60)

            pygame.draw.rect(screen, bg_color, button_rect, border_radius=10)
            pygame.draw.rect(screen, (100, 100, 150), button_rect, width=2, border_radius=10)

            text = self.font.render(option, True, text_color)
            text_rect = text.get_rect(center=button_rect.center)
            screen.blit(text, text_rect)

        board_rect = pygame.Rect(constant.WIDTH - 360, 100, 260, 400)
        pygame.draw.rect(screen, (255, 245, 230), board_rect, border_radius=20)
        pygame.draw.rect(screen, (180, 150, 120), board_rect, width=4, border_radius=20)

        header = self.font.render(constant.RECORDS, True, (80, 40, 20))
        header_rect = header.get_rect(center=(board_rect.centerx, board_rect.y + 40))
        screen.blit(header, header_rect)

        for i, (name, score) in enumerate(self.records):
            line = self.small_font.render(f"{i+1}. {name} - {score}", True, (60, 30, 20))
            screen.blit(line, (board_rect.x + 20, board_rect.y + 80 + i * 40))

    def next_scene(self):
        return getattr(self, "_next_scene", None)
