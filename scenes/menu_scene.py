import pygame
from Tools.scripts.generate_opcode_h import header

from .base_scene import Scene
import constant


class MenuScene(Scene):
    def __init__(self):
        self.font = pygame.font.Font("src/font/LapsusPro.ttf", 40)
        self.small_font = pygame.font.Font("src/font/LapsusPro.ttf", 28)

        self.options = [constant.START_GAME, constant.TRAIN, constant.SHOP, constant.SETTINGS, constant.EXIT]
        self.selected_index = 0

        self.records = [
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

        start_x = 100
        start_y = 150
        spacing = 60

        for i, option in enumerate(self.options):
            color = (0, 0, 0)
            if i == self.selected_index:
                color = (255, 0, 0)
            text = self.font.render(option, True, color)
            screen.blit(text, (start_x, start_y + i * spacing))

        header = self.font.render(constant.RECORDS, True, (0, 0, 0))
        screen.blit(header, (constant.WIDTH - 300, 100))

        for i, (name, score) in enumerate(self.records):
            line = self.small_font.render(f"{i+1}. {name} - {score}", True, (0, 0, 0))
            screen.blit(line, (constant.WIDTH - 300, 160 + i * 40))

    def next_scene(self):
        return getattr(self, "_next_scene", None)
