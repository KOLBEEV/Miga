import constant


def handle_fish_falls(fishes, player):
    for fish in fishes.copy():
        if fish.rect.top > constant.HEIGHT - 50:
            player.damage()
            fish.kill()
