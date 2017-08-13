import math
import board_display
import board_check

def board_print_n_check(board):
    board_display.reprint_board(board)
    board_check.game_over_check(board)

def mark_board():
    '''Mark "X" (Player 1) or "O" (Player2) at requested position'''
    board = board_display.empty_board()
    board_display.reprint_board(board)
    while board_check.game_over_check(board)!=True:
        position=raw_input("Player 1: Input position for Mark 'X'")
        board[int(position)-1]="X"
        board_print_n_check(board)
        position = raw_input("Player 2: Input position for Mark 'O'")
        board[int(position) - 1] = "O"
        board_print_n_check(board)

mark_board()
