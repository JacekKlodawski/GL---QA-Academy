import random

board = [[1,2,3],
         [4,5,6],
         [7,8,9]]


def show_board(board):
    for row in board:
        print(row)

def check_win():
    pass

def draw_player():
    player = random.choice('X','O')
    return player

def switch_player(player):
    if player == 'X':
        player = 'O'
    elif player == 'O':
        player = 'X'

def player_input()
    plr_input = input(f'Player {player} pick a field from 1 to 9')

def check_if_legit_number():


player = draw_player()
moves = 9

while moves > 0:
    show_board(board)
    player_input()
    check_win(board)
    switch_player(player)
    moves =- 1