def display_board(board):

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_input():

    marker = ''
    # KEEP ASKING PLAYER 1 to choose X or O

    while marker != 'X' and marker != 'O':
        marker = input("Player 1: Choose to play as X or O: ").upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    """Keep track of the player's board positions."""
    board[position] = marker


def win_check(board, mark):
    """Define winning conditions."""

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across bottom
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark) or  # diagonal
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down left
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down middle
            (board[9] == mark and board[6] == mark and board[3] == mark))    # down right


import random

def choose_first():
    """Decide which player starts the game."""
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    """Check if there are available spaces on the board, True or False."""
    return board[position] == ' '


def full_board_check(board):
    """Check if the board is full and return True or False."""
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    """Get the player's requested board position for their marker (1-9)"""
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Choose your next position: 1-9 "))

        return position


def replay():
    """Ask the player if they want to play again, return True or False."""
    return input("Do you want to play again? Enter Yes or No: ").lower().startswith('y')

# WHILE LOOP TO RUN THE GAME
print("Welcome to Tic Tac Toe!")

while True:

    # PLAY THE GAME

    # SET EVERYTHING UP(BOARD, WHO'S FIRST, CHOOSE MARKERS X,O)

    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input("Ready to play? y or n? ")

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    # GAME PLAY

    while game_on:

        if turn =='Player 1':

            #Show the board
            display_board(board)

            # Choose a position
            position = player_choice(board)

            # Place the marker on the positon
            place_marker(board, player1_marker, position)

            # Check if they won
            if win_check(board, player1_marker):
                display_board(board)
                print("Player 1 has won!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("Tie game!")
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            # Show the board
            display_board(board)

            # Choose a position
            position = player_choice(board)

            # Place the marker on the positon
            place_marker(board, player2_marker, position)

            # Check if they won
            if win_check(board, player2_marker):
                display_board(board)
                print("Player 2 has won!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("Tie game!")
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
