import math
def split_board_rows(board):
    size = int(math.sqrt(len(board)))
    rows=[]
    for i in range(size):
        rows.append(board[i*size:(i+1)*size])
    return rows


def split_board_columns(board):
    size = int(math.sqrt(len(board)))
    return [board[i::size] for i in range(size)]

def diagonal(board):
    size = int(math.sqrt(len(board)))
    diagonal=[]
    oppo_diagonal=[]
    for i in range(size):
        diagonal.append(board[i+i*size])
    for i in range(size):
        oppo_diagonal.append(board[(size-1)+i*(size-1)])
    reverse_diagonal=oppo_diagonal[::-1]
    return [diagonal, reverse_diagonal]
