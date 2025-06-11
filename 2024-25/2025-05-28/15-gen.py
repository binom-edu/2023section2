import random

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


n = 4
board = [i + 1 for i in range(n**2)]
new_game(70)
print(*board, file=open('15.txt', 'w'))