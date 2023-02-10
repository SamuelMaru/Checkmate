#THIS IS THE REDO (FASTER)

def remove_duplicates(lst):
    new_lst = []
    for ele in lst:
        if ele not in new_lst:
            new_lst.append(ele)
    return new_lst


def find_rooks(board):
  rooks = []
  for i in range(len(board)):
    for j in range(len(board[i])):
      if (board[i][j] == "R"):
        rooks.append([i , j])
  return rooks

def find_king(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == "K"):
                return [i,j]
    return None

def attacked_squares(board):
    squares = []
    king = find_king(board)
    rooks = find_rooks(board)
    for rook in rooks:
        x_position = rook[0]
        y_position = rook[1]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if ((i==x_position) or (j==y_position)) and (x_position,y_position)!= (i,j):
                    squares.append([i,j])
    return squares

def not_attacked_squares(attacked_squares,board):
    all_squares = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            all_squares.append([i,j])
    for i in range(len(attacked_squares)):
        if attacked_squares[i] in all_squares:
            all_squares.remove(attacked_squares[i])
    return all_squares

def king_moves(gameboard,safe_squares):
    king_pos = find_king(gameboard)
#idea: loop through all combos to see if the king can move anywhere
    for i in range(-1,2):
        for j in range(-1,2):
            move = [king_pos[0]+i,king_pos[1]+j]
            if move in safe_squares:
                return True
    return False


def checkmate(board):
    attacked_squaress = attacked_squares(board)
    safe_sqs = not_attacked_squares(attacked_squaress, board)
    possible_moves = king_moves(board, safe_sqs)
    return not possible_moves


gameBoard = [['-', '-', '-', 'K'],
            ['_', '-', 'R', 'R'],
            ['-', '-', '-', '-'],
            ['-', '-', '-', '-']]

print(checkmate(gameBoard))
