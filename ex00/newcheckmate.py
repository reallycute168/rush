def checkboard(board) :
    mBoard = board.split()
    num = len(mBoard)
    count = {
        "K" : 0, "Q" : 0, "B" : 0, "R" : 0, "P" : 0 
    }

    for row in board.split() :
        n = len(row) 
        if num != n :
            print("Not Sq")
            return False
        for col in row :
            if col in count : count[col] += 1
            elif col != "." : print("Table ERROR \nonly K Q B R P and .")
    
    if count["K"] > 1 : 
        print("K must have only 1") 
        return False
    if count["Q"] > 2 : 
        print("Q must have only 1")
        return False
    if count["R"] > 2 : 
        print("R must have only 2")
        return False
    if count["B"] > 2 : 
        print("B must have only 2")
        return False
    if count["P"] > 8 : 
        print("P must have only 8")
        return False
    

    return True


def checkmate(board) :
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
        print("Success")
        return

    #bishop
    bisDirec = [(-1,-1), (-1,1), (1,-1), (1,1)]
    for  dx, dy in bisDirec:
        x, y = kx, ky
        
        while True :
            x, y = x+dx, y+dy
            if  not ( 0 <= x < n and 0 <= y < n ):
                break
            elif mBoard[x][y] == "B" :
                print("Success")
                return
            elif mBoard[x][y] != "." :
                break

    #rook
    rookDirec = [(-1,0), (1,0), (0,-1), (0,1)]
    for  dx, dy in  rookDirec:
        x, y = kx, ky
        
        while True :
            x, y = x+dx, y+dy
            if  not ( 0 <= x < n and 0 <= y < n ):
                break
            elif mBoard[x][y] == "R" :
                print("Success")
                return
            elif mBoard[x][y] != "." :
                break
    
    # queen
    queenDirec = bisDirec + rookDirec
    for  dx, dy in queenDirec :
        x, y = kx, ky
        
        while True :
            x, y = x+dx, y+dy
            if  not ( 0 <= x < n and 0 <= y < n ):
                break
            elif mBoard[x][y] == "Q" :
                print("Success")
                return
            elif mBoard[x][y] != "." :
                break
    print("Fail")