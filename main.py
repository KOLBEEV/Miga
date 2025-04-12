import pygame
import constant
from scenes.menu_scene import MenuScene


pygame.init()
screen = pygame.display.set_mode((constant.WIDTH, constant.HEIGHT))
pygame.display.set_caption(constant.TITLE)
pygame.display.set_icon(pygame.image.load("src/image/fish/fish1.png"))
clock = pygame.time.Clock()

current_scene = MenuScene()
running = True

while running:
    for event in pygame.event.get():
        current_scene.handle_event(event)

    current_scene.update()
    current_scene.draw(screen)
    pygame.display.flip()
    clock.tick(constant.FPS)

    new_scene = current_scene.next_scene()
    if new_scene:
        current_scene = new_scene
