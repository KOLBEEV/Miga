import pygame
import constant
from scenes.menu_scene import MenuScene
from utils import resource_path


pygame.init()
screen = pygame.display.set_mode((constant.WIDTH, constant.HEIGHT))
pygame.display.set_caption(constant.TITLE)
pygame.display.set_icon(pygame.image.load(resource_path("src/image/fish/fish1.png")))
clock = pygame.time.Clock()

current_scene = MenuScene()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        current_scene.handle_event(event)

    current_scene.update()

    if not pygame.get_init():
        break

    try:
        current_scene.draw(screen)
        pygame.display.flip()
    except pygame.error:
        running = False

    new_scene = current_scene.next_scene()
    if new_scene:
        current_scene = new_scene

    clock.tick(constant.FPS)

pygame.quit()
