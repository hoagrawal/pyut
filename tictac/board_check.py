import math
import board_structure
def row_complete(board):
    size = int(math.sqrt(len(board)))
    rows=board_structure.split_board_rows(board)
    game_over = False
    for i in range(size):
        if rows[i].count("X")==size or rows[i].count("O")==size:
            game_over = True
            break
    return game_over



def column_complete(board):
    size = int(math.sqrt(len(board)))
    columns = board_structure.split_board_columns(board)
    game_over = False
    for i in range(size):
        if columns[i].count("X") == size or columns[i].count("O") == size:
            game_over = True
            break
    return game_over

def diagonal_complete(board):
    size = int(math.sqrt(len(board)))
    diagonals = board_structure.diagonal(board)
    game_over = False
    for i in range(2):
        if diagonals[i].count("X") == size or diagonals[i].count("O") == size:
            game_over = True
            break
    return game_over

def board_full(board):
    full = True
    for position in range(len(board)):
        if board[position] not in ["X", "O"]:
            full = False
    return full

def game_over_check(board):
    game_over=False
    if (board_full(board) or row_complete(board) or column_complete(board) or diagonal_complete(board)) is True:
        game_over=True
        print "Game Over"
        quit()
    return game_over
