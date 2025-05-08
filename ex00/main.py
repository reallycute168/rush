"""#!/usr/bin/env python3
def cou(b) :
    x = len(b)
    n = 0
    for i in range(1,9) :
        if (i*i + i - 1) == x :
            n = i
    return n

def toTable(b, n) :
    table = [[] for _ in range(n)]
    x = 0
    b =  b.replace("\n","")

    for i in range(n) :
        for j in range(n) :
            table[i].append(b[x])
            x += 1
    return table



def checkmate(board) :
    n = cou(board)
    x = toTable(board,n)

    for i in range(n) :
        for j in range(n) :
            print(x[i][j])



def main() :
    board = \
R..
..k
...\

    checkmate(board)


if __name__ == "__main__" :
    main()

"""

print("Hi Brother")
