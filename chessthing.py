
#THIS IS THE REDO (FASTER)

def valid_pos(pos, board):
    x,y = pos[0],pos[1]
    width = len(board[0])
    height = len(board)
    if (0<=x<width) and (0<=y<height):
        return True
    return False

def find_rooks(board):
  rooks = set()
  for i in range(len(board)):
    for j in range(len(board[i])):
      if (board[i][j] == "R"):
        rooks.add([i , j])
  return rooks

def find_bishops(board):
    bishops = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == "B"):
                bishops.add((i, j))
    return bishops

def find_king(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == "K"):
                return (i,j)
    return None

def rook_attacks(board):
    squares = set()
    rooks = find_rooks(board)
    for rook in rooks:
        x_position = rook[0]
        y_position = rook[1]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if ((i==x_position) or (j==y_position)) and (x_position,y_position)!= (i,j):
                    squares.add((i,j))
    return squares

def bishop_attacks(board):
    def check(squares,board,x,y):
        for k in range(1,len(board)):
            if (not valid_pos([x_position+x*k,y_position+y*k],board)) or (board[x_position+x*k][y_position+y*k] != "-" and board[x_position+x*k][y_position+y*k] != "K"):
                break
            else:

                squares.add((x_position+x*k,y_position+y*k))
        return squares
    #IN PROGRESS
    squares = set()
    bishops = find_bishops(board)
    for bishop in bishops:
        x_position = bishop[0]
        y_position = bishop[1]

        for x in ([-1,1]):
            for y in ([-1, 1]):
                check(squares,board,x,y)
    return squares



def king_moves(gameboard,attacked):
    king_pos = find_king(gameboard)
#idea: loop through all combos to see if the king can move anywhere
    for i in range(-1,2):
        for j in range(-1,2):
            move = (king_pos[0]+i,king_pos[1]+j)
            if valid_pos(move,gameboard):
                if move not in attacked:
                    return True
    return False


def checkmate(board):
    attacked_squaress = rook_attacks(board).union(bishop_attacks(board))
    possible_moves = king_moves(board, attacked_squaress)
    return not possible_moves
