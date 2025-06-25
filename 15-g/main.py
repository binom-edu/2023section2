import pygame, os, random, heapq

FPS = 50
TILE_SIZE = 100
IMG_DIR = os.path.join(os.path.dirname(__file__), 'img')


class Button(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.pressed = False
        self.last_action = pygame.time.get_ticks()
        self.action_rate = 150

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
        shuffle_board(20)

    def update(self):
        now = pygame.time.get_ticks()
        if moves_queue and now > self.last_action + self.action_rate:
            self.last_action = now
            move = moves_queue.pop(0)
            x = board.index(n**2)
            if move == 'w': num = board[x - n]
            elif move == 's': num = board[x + n]
            elif move == 'a': num = board[x - 1]
            elif move == 'd': num = board[x + 1]
            else: return
            for tile in all_tiles:
                if tile.num == num:
                    make_move(tile, move)

class Button_Solve(Button):
    def __init__(self):
        Button.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_DIR, 'buttons', 'sprite_solve.png')).convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 0.45)
        self.rect = self.image.get_rect()
        self.rect.topright = (550, TILE_SIZE * 6)
        all_buttons.add(self)

    def action(self):
        solve()

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
        self.moving = False
        all_tiles.add(self)

    def is_spotted(self):
        x, y = pygame.mouse.get_pos()
        return self.rect.left <= x - TILE_SIZE <= self.rect.right and self.rect.top <= y - TILE_SIZE <= self.rect.bottom
    
    def update(self):
        global board_locked
        x0, y0 = self.rect.topleft
        x, y = self.move_to
        if self.moving and x == x0 and y == y0: 
            self.moving = False
            board_locked = False
            print('board unlocked')
            return
        if x0 < x:
            self.rect.x += 20
            self.moving = True
        elif x0 > x:
            self.rect.x -= 20
            self.moving = True
        elif y0 < y:
            self.rect.y += 20
            self.moving = True
        elif y0 > y:
            self.rect.y -= 20
            self.moving = True


def new_game():
    all_tiles.empty()
    for i in range(n**2):
        board[i] = i + 1
        tile = Tile(i + 1)
        tile.move_to = tile.rect.topleft = (i % n * TILE_SIZE, i // n * TILE_SIZE)

def make_move(tile: Tile, move: str):
    print('плитка', tile.num, 'ход', move)
    global board_locked
    if board_locked: return
    board_locked = True
    print('board locked')
    x = board.index(n**2)
    i, j = x // n, x % n
    x0, y0 = tile.rect.topleft
    if move == 'w' and i != 0:
        board[x], board[x-n] = board[x-n], board[x]
        tile.move_to = (x0, y0 + TILE_SIZE)
    elif move == 's' and i != n - 1:
        board[x], board[x+n] = board[x+n], board[x]
        tile.move_to = (x0, y0 - TILE_SIZE)
    elif move == 'a' and j != 0:
        board[x], board[x-1] = board[x-1], board[x]
        tile.move_to = (x0 + TILE_SIZE, y0)
    elif move == 'd' and j != n - 1:
        board[x], board[x+1] = board[x+1], board[x]
        tile.move_to = (x0 - TILE_SIZE, y0)

def make_move_old(board, move):
    x = board.index(n**2)
    i, j = x // n, x % n
    if move == 'w' and i != 0:
        board[x], board[x-n] = board[x-n], board[x]
    elif move == 's' and i != n - 1:
        board[x], board[x+n] = board[x+n], board[x]
    elif move == 'a' and j != 0:
        board[x], board[x-1] = board[x-1], board[x]
    elif move == 'd' and j != n - 1:
        board[x], board[x+1] = board[x+1], board[x]

def get_neighbours_old(board):
    ans = []
    for move in 'wasd':
        bc = board.copy()
        make_move_old(bc, move)
        if bc != board:
            if move == 'w': m = 's'
            elif move == 's': m = 'w'
            elif move == 'a': m = 'd'
            elif move == 'd': m = 'a'
            ans.append((m, bc))
    return ans

def get_hash(board):
    ans = 0
    mod = 10 ** 9 + 7
    k = 23
    for i in range(len(board)):
        ans = (ans + board[i] * k**i) % mod
    return ans

def h(board):
    ans = 0
    for i in range(n**2):
        if board[i] != i + 1:
            ans += 1
    return ans

def solve():
    button_shuffle.last_action = pygame.time.get_ticks() + 1000
    begin = pygame.time.get_ticks()
    h0 = get_hash(sorted(board))

    d = {}
    q = []
    heapq.heapify(q)

    d[get_hash(board)] = 0
    heapq.heappush(q, (0 + h(board), board))
    flag = False
    while q:
        v = heapq.heappop(q)[1]
        hv = get_hash(v)
        for move, u in get_neighbours_old(v):
            hu = get_hash(u)
            if hu not in d:
                d[hu] = d[hv] + 1
                heapq.heappush(q, (d[hu] + h(u), u))
            if hu == h0:
                moves = d[hu]
                flag = True
                del q
                break
        if flag:
            break
    print('Требуется ходов:', moves)
    print('Позиций проверено:', len(d))
    print('Затрачено времени:', pygame.time.get_ticks() - begin)


    st = []
    cur = sorted(board)
    st.append(cur)
    while moves > 0:
        for move, u in get_neighbours_old(cur):
            hu = get_hash(u)
            if hu in d and d[hu] == moves - 1:
                st.append(move)
                cur = u
                moves -= 1
                break
    st.reverse()
    global moves_queue
    moves_queue = st.copy()
    
    # while st:
    #     print_board(st.pop())
    #     print('==============')
    #     sleep(1)

def select_move(tile: Tile) -> str:
    x = board.index(tile.num)
    i, j = x // n, x % n
    if i > 0 and board[x - n] == n**2:
        return 's'
    if i < n - 1 and board[x + n] == n**2:
        return 'w'
    if j > 0 and board[x - 1] == n**2:
        return 'd'
    if j < n - 1 and board[x + 1] == n**2:
        return 'a'
    return ''

def shuffle_board(cnt):
    button_shuffle.last_action = pygame.time.get_ticks() + 1000
    bc = board.copy()
    for i in range(cnt):
        x = bc.index(n**2)
        i, j = x // n, x % n
        neighbours = []
        if i > 0: neighbours.append(['w', x - n])
        if i < n - 1: neighbours.append(['s', x + n])
        if j > 0: neighbours.append(['a', x - 1])
        if j < n - 1: neighbours.append(['d', x + 1])
        move, pos = random.choice(neighbours)
        moves_queue.append(move)
        bc[x], bc[pos] = bc[pos], bc[x]
    print(bc)
    
        

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
moves_queue = []

game_on = True
board_locked = False
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
            for tile in all_tiles:
                if tile.is_spotted():
                    move = select_move(tile)
                    if move: make_move(tile, move)
                    
        elif event.type == pygame.MOUSEBUTTONUP:
            for button in all_buttons:
                if button.pressed:
                    if button.is_spotted():
                        button.action()
                    button.release()
    # update
    all_tiles.update()
    all_buttons.update()
    # render
    screen.fill((0, 0, 0))
    scene.fill((255, 230, 128))
    
    all_buttons.draw(screen)
    all_tiles.draw(scene)

    screen.blit(scene, (100, 100))
    pygame.display.flip()

pygame.quit()