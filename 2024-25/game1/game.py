import pygame, os

FPS = 60
WIDTH = 640
HEIGHT = 480
IMG_DIR = os.path.join(os.path.dirname(__file__), 'img')
ANIMATION_RATE = 100
cx, cy = 150, 330
g = 0.06
k = 40 * 10 ** (-4)

class Hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imgs = []
        for filename in os.listdir(os.path.join(IMG_DIR, 'hero')):
            img = pygame.transform.scale(
                pygame.image.load(os.path.join(IMG_DIR, 'hero', filename)), 
                (60,60)
                ).convert_alpha()
            self.imgs.append(img)
        self.img_number = 0
        self.image = self.imgs[self.img_number]
        self.angle = 0
        self.last_update = pygame.time.get_ticks()
        # self.image = pygame.surface.Surface((20, 20))
        # pygame.draw.circle(self.image, (255, 0, 0), (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (10, HEIGHT - 10)
        self.v_jump = 1
        self.vy = 6
        self.vx = 2
        self.mode = 0

    def update(self):
        

        if self.mode == 1:
            # анимация костюмов
            now = pygame.time.get_ticks()
            if now - self.last_update > ANIMATION_RATE:
                self.img_number = (self.img_number + 1) % len(self.imgs)
                self.angle += 15
                self.image = pygame.transform.rotate(self.imgs[self.img_number], self.angle)
                self.last_update = now
            self.vy -= g
            self.rect.centery -= self.vy
            self.rect.centerx += self.vx
            if distance(self.rect.center, (cx, cy )) < 30:
                self.rect.center = (cx, cy)
                self.mode = 2
                self.angle = 0
                self.image = pygame.transform.rotate(self.imgs[self.img_number], self.angle)

        elif self.mode == 3:
            self.rect.center = pygame.mouse.get_pos()

        elif self.mode == 4:
            # анимация костюмов
            # now = pygame.time.get_ticks()
            # if now - self.last_update > ANIMATION_RATE:
            #     self.img_number = (self.img_number + 1) % len(self.imgs)
            #     self.angle += 15
            #     self.image = pygame.transform.rotate(self.imgs[self.img_number], self.angle)
            #     self.last_update = now
            dx = cx - self.rect.centerx
            dy = cy - self.rect.centery
            ax = k * dx
            ay = k * dy
            self.vx += ax
            self.vy += ay
            self.rect.centery += self.vy
            self.rect.centerx += self.vx
            if self.vx * ax < 0 or self.vy * ay < 0:
                self.mode = 5
        
        elif self.mode == 5:
            # анимация костюмов
            now = pygame.time.get_ticks()
            if now - self.last_update > ANIMATION_RATE:
                self.img_number = (self.img_number + 1) % len(self.imgs)
                self.angle += 15
                self.image = pygame.transform.rotate(self.imgs[self.img_number], self.angle)
                self.last_update = now
            self.vy += g
            self.rect.centerx += self.vx
            self.rect.centery += self.vy

        if self.rect.bottom > HEIGHT - 10:
            self.rect.bottom = HEIGHT - 10
            self.mode = 0
    
    def pressed(self):
        if self.mode == 0:
            while True:
                a = g * 1.3 * (cx - self.rect.x) ** 2 / (2 * self.v_jump ** 2)
                b = self.rect.x - cx
                c = g * 1.3 * (cx - self.rect.x) ** 2 / (2 * self.v_jump ** 2) - cy + self.rect.y
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
        
        elif self.mode == 2:
            self.vx = self.vy = 0
            self.mode = 3


def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('О птичках')
bg = pygame.image.load(os.path.join(IMG_DIR, 'bg18.png')).convert_alpha()
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
            if distance(pygame.mouse.get_pos(), hero.rect.center) <= 30:
                hero.pressed()
        if event.type == pygame.MOUSEBUTTONUP and hero.mode == 3:
            hero.mode = 4


    # обновление
    all_sprites.update()
    # рендеринг
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), (cx, cy), 3)
    if hero.mode in [3, 4]:
        pygame.draw.line(screen, (255, 255, 255), (cx, cy), hero.rect.center, 2)
    screen.blit(bg, (0, 167, WIDTH - 1, HEIGHT - 1))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()