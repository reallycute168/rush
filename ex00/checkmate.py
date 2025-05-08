#!/usr/bin/env python3

class Game :
    def __init__(self, board, king, num):
        self.board = board
        self.king = king
        self.num = num


    def check_pawn(self, pos, num) :
        if pos[0] != 0 and pos[1] == 0 :
            print("check", pos[0] - 1, pos[1] + 1)
            
        elif pos[0] != 0 and pos[1] == num - 1 :
            print("pawn check", pos[0] - 1, pos[1] - 1)
        else :
            print("pawn check", pos[0] - 1, pos[1] - 1, "and", pos[0] - 1, pos[1] + 1 )


    
    def check_bishop(pos) :
        pass


    def check_rook(self, pos, num) :
        r = []
        print("rook check ", end=" ")
        for i in range(num) :
            for j in range(num) :
                if i == pos[0] and j == pos[1] :
                    pass
                if i == pos[0] or j == pos[1] :
                    print(i, j, end=", ")

    
    def check_queen(pos) :
        pass
    


    def check(self) :
        for i in range(self.num) :
            for j in range(self.num) :
                txt = self.board[i][j]

                pos = [i, j]

                if txt == "P" :
                    # print("found Pawn at", pos)
                    self.check_pawn(pos, self.num)
                
                # if txt == "B" :
                    # print("found Bishop at", pos)
                    # change to def

                if txt == "R" :
                    print("found Rook at", pos)
                    self.check_rook(pos, self.num)
                    # change to def

                # if txt == "Q" :
                    # print("found Queen at", pos)
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

