#!/usr/bin/env python3

from checkmate import checkmate 
from checkmate import Pos_K

def check_board(board):
    sta = True
    staKing = False
    b = board.split()
    n = len(b)

    for i in range(n):
        for j in range(n):
            txt = b[i][j]

            if txt not in [".","K", "Q", "P", "R", "B"] :
                print("WHO ARE YOU")
                sta = False
            
            if "K" == txt:
                staKing = True            
    
    for i in b :
        if len(i) != n :
            print("Eiwwwwwww not Table")
            sta = False
    
    if not staKing :
        print("WHERE ARE KING")

        
def main():
    board = """\
    R...
    .N..
    ..P.
    ....\
    """
    check_board(board)
    # checkmate(board)

if __name__ == "__main__":
    main()

