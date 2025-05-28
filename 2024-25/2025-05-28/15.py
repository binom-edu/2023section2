import random


def print_board():
    for i in range(n):
        for j in range(n):
            x = i * n + j
            if board[x] != n ** 2:
                print(board[x], end='\t')
            else:
                print(' ', end='\t')
        print()

def make_move(move):
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
        make_move(random.choice('wasd'))

n = 3
board = [i + 1 for i in range(n**2)]
new_game(5)
print_board()
while board != sorted(board):
    move = input().lower()
    make_move(move)
    print_board()