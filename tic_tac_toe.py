
def clear_output():
    print('\n' * 50)

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])
    
def space_check(board, position):
    return board[position] == ' '

def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player1 choose X or O: ').upper()
        if marker == 'X':
            return ('X', 'O')
        else:
            return('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark)) 

import random

def choose_first():
    z = random.randint(1,2)
    if z == 1:
        return 'Player1 goes first'
    else:
        return'Player2 goes first'

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position): 
        position = int(input('Where do you want to go? (Numbers 1-9):  '))
    return position
    
def replay():
    rematch = input('Do you want to play again?  ')
    if rematch == 'n' or rematch == 'no':
        return False
    return rematch == 'y' or rematch == 'yes'

print('Welcome to Tic Tac Toe!')

while True:
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn)

    play_game = input('Ready to play? yes or no\n')

    if play_game == 'no':
        game_on = False
    else:
        game_on = True

    while game_on:
        if turn == 'Player1 goes first':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
               display_board(the_board)
               print('Player 1 has won') 
               game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('tie game')
                    game_on = False

                else:
                    turn = 'Player2 goes first'

        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
               display_board(the_board)
               print('Player 2 has won') 
               game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('tie game')
                    game_on = False

                else:
                    turn = 'Player1 goes first' 
        
    if not replay():
        break

        
    



    