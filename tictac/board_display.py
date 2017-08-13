import board_structure
import math
def empty_board():

    size=int(raw_input("Ask size of the board:"))
    board=[]
    for i in range(size*size):
        board.append(i+1)
    return board

def reprint_board(board):
    size = int(math.sqrt(len(board)))
    board_rows = board_structure.split_board_rows(board)
    for i in range(size):
        print board_rows[i]

