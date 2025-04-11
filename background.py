import pygame


class Background:
    def __init__(self, screen_size):
        self.layers = []
        self.width, self.height = screen_size

        self.load_layers()

    def load_layers(self):
        layer_data = [
            ("src/image/background/beach.png", 0, 350),
        ]

        for path, x, y in layer_data:
            image = pygame.image.load(path).convert_alpha()
            self.layers.append({
                "image": image,
                "pos": (x, y)
            })

    def draw(self, surface):
        for layer in self.layers:
            surface.blit(layer["image"], layer["pos"])
