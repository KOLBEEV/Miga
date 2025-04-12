import pygame


class Animator:
    def __init__(self, sprite_sheet, frame_width, frame_height, animations, fps=10):
        self.sprite_sheet = pygame.image.load(sprite_sheet).convert_alpha()
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.fps = fps
        self.animations = self._cut_animations(animations)
        self.current_anim = "idle"
        self.current_frame = 0
        self.timer = 0

    def _cut_animations(self, animations):
        result = {}
        for name, (row, offset, frame_count) in animations.items():
            frames = []
            for i in range(frame_count):
                x = (offset + i) * self.frame_width
                y = row * self.frame_height
                rect = pygame.Rect(x, y, self.frame_width, self.frame_height)

                if x + self.frame_width > self.sprite_sheet.get_width():
                    raise ValueError(f"Кадр выходит за пределы по x: {x}px")

                frame = self.sprite_sheet.subsurface(rect)
                frames.append(frame)
            result[name] = frames

        return result

    def set_animation(self, name):
        if name != self.current_anim:
            self.current_anim = name
            self.current_frame = 0
            self.timer = 0

    def update(self):
        self.timer += 1
        if self.timer >= (60 // self.fps):
            self.current_frame = (self.current_frame + 1) % len(self.animations[self.current_anim])
            self.timer = 0

    def get_image(self, flip=False):
        image = self.animations[self.current_anim][self.current_frame]
        if flip:
            image = pygame.transform.flip(image, True, False)
        return image
