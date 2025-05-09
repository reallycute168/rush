#!/usr/bin/env python3

class Game :
    def __init__(self, board, king, num):
        self.board = board
        self.king = king
        self.num = num


    def check_pawn(self, pos, num) :
        if pos[0] != 0 and pos[1] == 0 :
            return [[pos[0]-1, pos[1]+1]]
            
        elif pos[0] != 0 and pos[1] == num - 1 :
            return [[pos[0]-1, pos[1]+1]]
        else :
            return [ [pos[0]-1, pos[1]+1], [pos[0]-1, pos[1]-1] ]

    
    def check_bishop(self, pos, num) :
        b = []
        n1 = num - pos[0]
        for i in range(0, n1 - 1) :
            b.append([i, pos[0] + i])
            

        # for i in range(n1, num) :
        #     b.append([i, pos[1]])
        print(b)

    def check_rook(self, pos, num) :
        r = []
        for i in range(num) :
            for j in range(num) :
                if i == pos[0] and j == pos[1] :
                    pass
                if i == pos[0] or j == pos[1] :
                    r.append([i, j])
        return r
    
    def check_queen(pos) :
        pass
    


    def check(self, king) :

        allSta = False

        for i in range(self.num) :
            for j in range(self.num) :
                txt = self.board[i][j]

                pos = [i, j]

                if txt == "P" :
                    # x = self.check_pawn(pos, self.num)
                    # for k in x :
                    #     if k == king :
                    #         print("Success")
                    #         allSta = True

                    if pos[0] > 0 and (  (pos[1] - 1) == king[1] and (pos[0]-1) == king[0]  or (pos[1] + 1) == king[1] and (pos[0]-1) == king[0]   ) :
                        print("check")
                    else :
                        print("no")
                
                if txt == "B" :
                    # x = self.check_bishop(pos, self.num)
                    # self.check_bishop(pos, self.num)
                    a = pos[0] - king[0]
                    b = pos[1] - king[1]
                    if a == b :
                        print("check")
                    else :
                        print("no")


                elif txt == "R" :
                    # x = self.check_rook(pos, self.num)
                    # for k in x :
                    #     if k == king :
                    #         print("Success")
                    #         allSta = True
                    if pos[0] == king[0] or pos[1] == king[1] :
                        print("check")
                    else :
                        print("no")


                # if txt == "Q" :
                    # print("found Queen at", pos)
                    # change to def
                
                if allSta :
                    break
            
            if allSta :
                break

    


def check_board(board):
    sta = True
    staKing = False
    couKing = 0
    b = board.split()
    n = len(b)

    for i in range(n):
        for j in range(n):
            txt = b[i][j]

            if txt not in [".","K", "Q", "P", "R", "B"] :
                print("WHO ARE YOU")
                sta = False

            if "K" == txt:
                couKing += 1
                staKing = True 
    for i in b :
        if len(i) != n :
            print("Eiwwwwwww not Table")
            sta = False

    if not staKing :
        print("WHERE ARE KING")
        sta = False

    if sta and couKing == 1:
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
    try :
        check_b = check_board(board)
        if check_b :

            pos_Kx, pos_Ky = posKing(board.split())
            posK = [pos_Kx, pos_Ky]
            print("King is", posK )
            myGame = Game(board.split(), posK, len(board.split()))
            sta = myGame.check(posK)
        
        else :
            print("ERROR")
    except :
        print("ERROR")

