import random
from collections import deque
from time import sleep

def print_board(board):
    for i in range(n):
        for j in range(n):
            x = i * n + j
            if board[x] != n ** 2:
                print(board[x], end='\t')
            else:
                print(' ', end='\t')
        print()

def make_move(board, move):
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

def new_game(d):
    for i in range(d):
        make_move(board, random.choice('wasd'))

def get_hash(board):
    ans = 0
    mod = 10 ** 9 + 7
    k = 23
    for i in range(len(board)):
        ans = (ans + board[i] * k**i) % mod
    return ans

def get_neighbours(board):
    ans = []
    for move in 'wasd':
        bc = board.copy()
        make_move(bc, move)
        if bc != board:
            ans.append(bc)
    return ans

n = 4
board = [i + 1 for i in range(n**2)]
h0 = get_hash(board)

new_game(100)
print_board(board)
# while board != sorted(board):
#     move = input().lower()
#     make_move(move)
#     print_board()

# bfs
d = {}
q = deque()
d[get_hash(board)] = 0
q.append(board)
flag = False
while q:
    v = q.popleft()
    hv = get_hash(v)
    for u in get_neighbours(v):
        hu = get_hash(u)
        if hu not in d:
            d[hu] = d[hv] + 1
            q.append(u)
        if hu == h0:
            moves = d[hu]
            flag = True
            del q
            break
    if flag:
        break
print('Требуется ходов:', moves)
print('Позиций проверено:', len(d))
st = []
cur = sorted(board)
st.append(cur)
while moves > 0:
    for u in get_neighbours(cur):
        hu = get_hash(u)
        if hu in d and d[hu] == moves - 1:
            st.append(u)
            cur = u
            moves -= 1
            break
while st:
    print_board(st.pop())
    print('==============')
    sleep(1)