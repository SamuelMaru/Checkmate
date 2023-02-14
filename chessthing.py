
#THIS IS THE REDO (FASTER)

def valid_pos(pos, board):
    x,y = pos[0],pos[1]
    width = len(board[0])
    height = len(board)
    if (0<=x<width) and (0<=y<height):
        return True
    return False

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
    rooks = find_rooks(board)
    for rook in rooks:
        x_position = rook[0]
        y_position = rook[1]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if ((i==x_position) or (j==y_position)) and (x_position,y_position)!= (i,j):
                    squares.append([i,j])
    return squares



def king_moves(gameboard,attacked):
    king_pos = find_king(gameboard)
#idea: loop through all combos to see if the king can move anywhere
    for i in range(-1,2):
        for j in range(-1,2):
            move = [king_pos[0]+i,king_pos[1]+j]
            if valid_pos(move,gameboard):
                if move not in attacked:
                    return True
    return False


def checkmate(board):
    attacked_squaress = attacked_squares(board)
    possible_moves = king_moves(board, attacked_squaress)
    return not possible_moves
