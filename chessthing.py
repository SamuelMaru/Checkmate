def remove_duplicates(lst):
    new_lst = []
    for ele in lst:
        if ele not in new_lst:
            new_lst.append(ele)
    return new_lst


def findpos(gameBoard, piece):
    pos = []
    for i in range(len(gameBoard)):
        for j in range(len(gameBoard[i])):
            if piece == gameBoard[i][j]:
                pos.append([i, j])


    if piece == "K":
        return pos[0]
    else:
        return pos


def attacked_squares(gameboard):
    squares = []
    rook_pos = findpos(gameboard,"R")
    print(rook_pos)
    for i in range(len(gameboard)):
        if "R" in gameboard[i]:
            for j in range(len(gameboard[i])):
                if gameboard[i][j]!= "R":
                    squares.append([i,j])
                else:
                    pass

    for i in range(len(rook_pos)):
        for j in range(len(gameboard)):
            for k in range(len(gameboard[j])):
                if rook_pos[i][0] == j:
                    squares.append([k,j])
    return remove_duplicates(squares)

def not_attacked_squares(attacked_squares,gameboard):
    all_squares = []
    for i in range(len(gameboard)):
        for j in range(len(gameboard[i])):
            all_squares.append([i,j])
    for i in attacked_squares:
        all_squares.remove(i)
    return all_squares

def king_moves(gameboard,safe_squares):
    print(safe_squares)
    king_pos = findpos(gameboard,"K")
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


