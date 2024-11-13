from typing import Any
import pygame

FPS = 60
WIDTH = 640
HEIGHT = 480

class Hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((20, 20))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
    def update(self):
        self.rect.y += 1

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('О птичках')
clock = pygame.time.Clock()

hero = Hero()
all_sprites = pygame.sprite.Group()
all_sprites.add(hero)

gameOn = True
while gameOn:
    clock.tick(FPS)
    # события
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            gameOn = False
    # обновление
    all_sprites.update()
    # рендеринг
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()