import pygame, os

FPS = 30
TILE_SIZE = 100
IMG_DIR = os.path.join(os.path.dirname(__file__), 'img')


class Button(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.pressed = False

    def is_spotted(self):
        x, y = pygame.mouse.get_pos()
        return self.rect.left <= x <= self.rect.right and self.rect.top <= y <= self.rect.bottom

    def press(self):
        self.rect.x += 5
        self.rect.y += 5
        self.pressed = True

    def release(self):
        self.rect.x -= 5
        self.rect.y -= 5
        self.pressed = False

class Button_New(Button):
    def __init__(self):
        Button.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_DIR, 'buttons', 'sprite_new.png')).convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 0.45)
        self.rect = self.image.get_rect()
        self.rect.topleft = (50, TILE_SIZE * 6)
        all_buttons.add(self)
    
    def action(self):
        new_game()

class Button_Shuffle(Button):
    def __init__(self):
        Button.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_DIR, 'buttons', 'sprite_shuffle.png')).convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 0.45)
        self.rect = self.image.get_rect()
        self.rect.midtop = (300, TILE_SIZE * 6)
        all_buttons.add(self)
    
    def action(self):
        print('Нажата кнопка Перемешать')

class Button_Solve(Button):
    def __init__(self):
        Button.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_DIR, 'buttons', 'sprite_solve.png')).convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 0.45)
        self.rect = self.image.get_rect()
        self.rect.topright = (550, TILE_SIZE * 6)
        all_buttons.add(self)

    def action(self):
        print('Нажата кнопка Решить')

class Tile(pygame.sprite.Sprite):
    def __init__(self, num):
        pygame.sprite.Sprite.__init__(self)
        self.num = num
        if num == 16:
            self.image = pygame.surface.Surface((TILE_SIZE, TILE_SIZE))
            self.image.set_alpha(0)
        else:
            img = pygame.image.load(os.path.join(IMG_DIR, 'tiles', str(num) + '.png')).convert_alpha()
            self.image = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect()
        all_tiles.add(self)

def new_game():
    all_tiles.empty()
    for i in range(n**2):
        board[i] = i + 1
        tile = Tile(i + 1)
        tile.rect.topleft = (i % n * TILE_SIZE, i // n * TILE_SIZE)

pygame.init()
screen = pygame.display.set_mode((600, 800), 0, 32)
pygame.display.set_caption('Пятнашки')
clock = pygame.time.Clock()
scene = pygame.surface.Surface((TILE_SIZE * 4, TILE_SIZE * 4))

all_buttons = pygame.sprite.Group()
all_tiles = pygame.sprite.Group()

button_new = Button_New()
button_shuffle = Button_Shuffle()
button_solve = Button_Solve()

n = 4
board = [i + 1 for i in range(n**2)]
new_game()
print(board)

game_on = True
while game_on:
    clock.tick(FPS)

    # events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in all_buttons:
                if button.is_spotted():
                    button.press()
        elif event.type == pygame.MOUSEBUTTONUP:
            for button in all_buttons:
                if button.pressed:
                    if button.is_spotted():
                        button.action()
                    button.release()
    # update
    # render
    screen.fill((0, 0, 0))
    scene.fill((255, 230, 128))
    
    all_buttons.draw(screen)
    all_tiles.draw(scene)

    screen.blit(scene, (100, 100))
    pygame.display.flip()

pygame.quit()