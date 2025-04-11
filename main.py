import pygame
import constant
from background import Background
from player import Player
from fish import Fish


pygame.init()

font = pygame.font.Font("src/font/LapsusPro.ttf", 30)

screen = pygame.display.set_mode((constant.WIDTH, constant.HEIGHT))
pygame.display.set_caption(constant.TITLE)

clock = pygame.time.Clock()
running = True

background = Background((constant.WIDTH, constant.HEIGHT))

player = Player(constant.WIDTH / 2, constant.HEIGHT - 10)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

fishes = pygame.sprite.Group()
spawn_timer = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    spawn_timer += 1
    if spawn_timer >= 60:
        fish = Fish()
        fishes.add(fish)
        all_sprites.add(fish)
        spawn_timer = 0

    all_sprites.update()

    player.check_collision(fishes)

    screen.fill(constant.WHITE)
    background.draw(screen)
    all_sprites.draw(screen)

    score_text = font.render(f"Очки: {player.score}", True, (0, 0, 0))
    health_text = font.render(f"Здоровье: {player.health}", True, (255, 0, 0))

    screen.blit(score_text, (10, 10))
    screen.blit(health_text, (10, 50))

    pygame.display.flip()
    clock.tick(constant.FPS)

pygame.quit()
