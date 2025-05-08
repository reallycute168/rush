#!/usr/bin/env python3

from checkmate import checkmate 
# from checkmate import Pos_K

def main():
    board = """\
.......
Q.....P
.......
...P.R.
.B.....
.....K.
.......\
    """
    checkmate(board)

if __name__ == "__main__":
    main()
