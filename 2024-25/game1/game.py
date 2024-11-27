from typing import Any
import pygame

FPS = 60
WIDTH = 640
HEIGHT = 480
cx, cy = 150, 330
g = 0.1

class Hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((20, 20))
        pygame.draw.circle(self.image, (255, 0, 0), (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (10, HEIGHT - 10)
        self.v_jump = 1
        self.vy = 6
        self.vx = 2
        self.mode = 0

    def update(self):
        if self.mode == 1:
            self.vy -= g
            self.rect.y -= self.vy
            self.rect.x += self.vx

        elif self.mode == 4:
            self.vy -= g
            self.rect.y -= self.vy
            self.rect.x += self.vx
    
    def pressed(self):
        if self.mode == 0:
            while True:
                a = g * 0.969 * (cx - self.rect.x) ** 2 / (2 * self.v_jump ** 2)
                b = self.rect.x - cx
                c = g * 0.969 * (cx - self.rect.x) ** 2 / (2 * self.v_jump ** 2) - cy + self.rect.y
                d = (b ** 2 - 4 * a * c)
                if d > 0:
                    break
                self.v_jump += 1
            k = (-b + d ** 0.5) / (2 * a)
            cosa = (1 / (k ** 2 + 1)) ** 0.5
            sina = (1 - cosa ** 2) ** 0.5
            self.vx = self.v_jump * cosa
            self.vy = self.v_jump * sina
            self.mode = 1


def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if distance(pygame.mouse.get_pos(), hero.rect.center) <= 10:
                hero.pressed()

    # обновление
    all_sprites.update()
    # рендеринг
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), (cx, cy), 3)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()