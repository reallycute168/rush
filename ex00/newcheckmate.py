def checkboard(board) :
    try :
        mBoard = board.split()
        num = len(mBoard)
        sta = True
        count = {
            "K" : 0, "Q" : 0, "B" : 0, "R" : 0, "P" : 0 
        }

        for row in board.split() :
            n = len(row) 
            if num != n :
                print("Not Sq")
                sta = False
            for col in row :
                if col in count : 
                    count[col] += 1
                elif col != "." : 
                    print("Table ERROR \nonly K Q B R P and .")
                    sta = False

        if all(x == 0 for x in count.values()):
            print("Now you have just only board, How do u play? Hmmm")
            sta = False
        if not count["K"] :
            print("Where are King?")
            sta = False

        if count["K"] > 1 : 
            print("K must have only 1") 
            sta = False
        if count["Q"] > 1 : 
            print("Q must have only 1")
            sta = False
        if count["R"] > 2 : 
            print("R must have only 2")
            sta = False
        if count["B"] > 2 : 
            print("B must have only 2")
            sta = False
        if count["P"] > 8 : 
            print("P must have only 8")
            sta = False
        
        if not sta :
            return False
        return True
    except : 
        print("This is ERROR about board")

def checkmate(board) :
    try :
        mBoard = board.split()
        n = len(mBoard)
        posKing = None

        for row in range(n):
            for col in range(n) :
                if mBoard[row][col] == "K" :
                    posKing = (row, col)

        kx, ky = posKing

        #pawn
        if posKing[0] < n-1 and (mBoard[kx+1][ky+1] == "P" or mBoard[kx+1][ky-1] == "P"):
            print("Success \n(checkmate by P)")
            return


        all_direc = {
            "B" : [(-1,-1), (-1,1), (1,-1), (1,1)] ,
            "R" : [(-1,0), (1,0), (0,-1), (0,1)] ,
            "Q" : [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)] 
        }

        for key, direc in all_direc.items() :
            for  dx, dy in direc:
                x, y = kx, ky
                
                while True :
                    x, y = x+dx, y+dy
                    if  not ( 0 <= x < n and 0 <= y < n ):
                        break
                    elif mBoard[x][y] == key :
                        print(f"Success \n(checkmate by {key})")
                        return
                    elif mBoard[x][y] != "." :
                        break

        
        print("Fail")
    except :
        print("This is ERROR about chess")