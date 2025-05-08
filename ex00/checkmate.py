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
        sta = False

    if sta :
        print("Evrythinh is OK")
        return True
    else : 
        return False

def posKing(board) :
    n = len(board)
    for i in range(n):
        for j in range(n):
            txt = board[i][j]
            
            if txt == "K" :
                return i, j

def checkmate(board):

    check_b = check_board(board)
    if check_b :

        pos_Kx, pos_Ky = posKing(board.split())
        print(pos_Kx, pos_Ky)

# myGame = Game()