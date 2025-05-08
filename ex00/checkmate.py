#!/usr/bin/env python3

class Game :
    def __init__(self, board, king, num):
        self.board = board
        self.king = king
        self.num = num


    def check_pawn(pos) :
        pass

    
    def check_bishop(pos) :
        pass


    def check_rook(pos) :
        pass

    
    def check_queen(pos) :
        pass
    


    def check(self) :
        for i in range(self.num) :
            for j in range(self.num) :
                txt = self.board[i][j]

                pos = [i, j]

                if txt == "P" :
                    print("found Pawn at", pos)
                    # change to def
                
                if txt == "B" :
                    print("found Bishop at", pos)
                    # change to def

                if txt == "R" :
                    print("found Rook at", pos)
                    # change to def

                if txt == "Q" :
                    print("found Queen at", pos)
                    # change to def
    




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
        posK = [pos_Kx, pos_Ky]
        print("King is", posK )
        myGame = Game(board.split(), posK, len(board.split()))
        myGame.check()

