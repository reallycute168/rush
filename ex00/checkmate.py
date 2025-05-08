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
    pass

def Pos_K(board):
    b = board.split()
    n = len(b)
    for row in range(n):
        for col in range(n):
            if board[row][col] == "K" :
                king_pos = int(row,col)
                print(king_pos)
print(Pos_K)
