import pygame
import random
from utils import resource_path


class SoundManager:
    def __init__(self):
        self.sounds = {}
        self.channels = {}

        self.register_sound('collect', [
            resource_path('src/sound/collect/collect.mp3'),
        ])
        self.register_sound('auf', [
            resource_path('src/sound/auf/1.wav'),
            resource_path('src/sound/auf/2.wav'),
        ])
        self.register_sound('damage', [
            resource_path('src/sound/damage/1.wav'),
            resource_path('src/sound/damage/2.wav'),
        ])

    def register_sound(self, key, file_list):
        self.sounds[key] = []
        for path in file_list:
            try:
                sound = pygame.mixer.Sound(path)
                self.sounds[key].append(sound)
            except pygame.error as e:
                print(f"Ошибка загрузки {e}")

    def play(self, key, chance=1.0):
        if key not in self.sounds or not self.sounds[key]:
            print(f"Звук {key} не найден")
            return

        if random.random() <= chance:
            sound = random.choice(self.sounds[key])
            channel =pygame.mixer.find_channel()
            if channel:
                channel.play(sound)
            else:
                print("Нет свободного канала")
