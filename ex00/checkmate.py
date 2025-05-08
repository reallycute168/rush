#!/usr/bin/env python3
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


def checkmate():
    if Pos_K == Enemy :
        print("Success")
    else :
        print("Fail")


board = """
R...
.N..
.P..
....
"""

def Pos_K(board):
    '''tingwaidevwtom'''
    b = board.split()
    n = len(b)
    for row in range(n):
        for col in range(len(b[row])):
            if b[row][col] == "K" :
                king_pos = (row,col)
                print(king_pos)
                return king_pos

print(Pos_K)

