import random

def show_board(board):
    for row in board:
        print(row)

def check_win(board, player):
    if board[0][0] == board[0][1] == board[0][2]:
        print(f'Player {player} wins!')
        return True
    elif board[1][0] == board[1][1] == board[1][2]:
        print(f'Player {player} wins!')
        return True
    elif board[2][0] == board[2][1] == board[2][2]:
        print(f'Player {player} wins!')
        return True
    elif board[0][0] == board[1][0] == board[2][0]:
        print(f'Player {player} wins!')
        return True
    elif board[0][1] == board[1][1] == board[2][1]:
        print(f'Player {player} wins!')
        return True
    elif board[0][2] == board[1][2] == board[2][2]:
        print(f'Player {player} wins!')
        return True
    elif board[0][0] == board[1][1] == board[2][2]:
        print(f'Player {player} wins!')
        return True
    elif board[0][2] == board[1][1] == board[2][0]:
        print(f'Player {player} wins!')
        return True

def draw_player():
    player = random.choice(['X', 'O'])
    return player


def make_move(player):
    move = input(f'Player {player} pick a field from 1 to 9')
    return move

def switch_players(player):
    if player == 'X':
        return 'O'
    elif player == 'O':
        return 'X'


def insert_on_board(board, move, player):
    if move == "1":
        board[0][0] = player
    elif move == "2":
        board[0][1] = player
    elif move == "3":
        board[0][2] = player
    elif move == "4":
        board[1][0] = player
    elif move == "5":
        board[1][1] = player
    elif move == "6":
        board[1][2] = player
    elif move == "7":
        board[2][0] = player
    elif move == "8":
        board[2][1] = player
    elif move == "9":
        board[2][2] = player
    return board


def game():
    board = [['1', '2', '3'],
             ['4', '5', '6'],
             ['7', '8', '9']]
    player = draw_player()
    moves = 9

    while moves > 0:
        show_board(board)
#        move = input(f'Player {player} pick a field from 1 to 9')
        move = make_move(player)
        b = 0
        #checking if the value is correct and if the field is taken
        while b != 1:
            if move not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                print('This is not a proper value, please try again.')
                move = make_move(player)
                continue
            if move == "1" and board[0][0] == 'O' or move == "1" and board[0][0] == 'X':
                print('This field is taken, please pick a different one.')
                move = make_move(player)
            elif move == "2" and board[0][1] == 'O' or move == "2" and board[0][1] == 'X':
                print('This field is taken, please pick a different one.')
                move = make_move(player)
            elif move == "3" and board[0][2] == 'O' or move == "3" and board[0][2] == 'X':
                print('This field is taken, please pick a different one.')
                move = make_move(player)
            elif move == "4" and board[1][0] == 'O' or move == "4" and board[1][0] == 'X':
                print('This field is taken, please pick a different one.')
                move = make_move(player)
            elif move == "5" and board[1][1] == 'O' or move == "5" and board[1][1] == 'X':
                print('This field is taken, please pick a different one.')
                move = make_move(player)
            elif move == "6" and board[1][2] == 'O' or move == "6" and board[1][2] == 'X':
                print('This field is taken, please pick a different one.')
                move = make_move(player)
            elif move == "7" and board[2][0] == 'O' or move == "7" and board[2][0] == 'X':
                print('This field is taken, please pick a different one.')
                move = make_move(player)
            elif move == "8" and board[2][1] == 'O' or move == "8" and board[2][1] == 'X':
                print('This field is taken, please pick a different one.')
                move = make_move(player)
            elif move == "9" and board[2][2] == 'O' or move == "9" and board[2][2] == 'X':
                print('This field is taken, please pick a different one.')
                move = make_move(player)
            else:
                b = 1

        insert_on_board(board, move, player)
        #checking if a player won
        if check_win(board, player):
            show_board(board)

            break
        #switching players
        player = switch_players(player)

        moves = moves - 1

        if moves == 0:
            print("Tie!")

game()