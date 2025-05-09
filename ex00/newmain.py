#!/usr/bin/env python3

from newcheckmate import checkboard, checkmate
# from checkmate import Pos_K

def main():
    board = """\
.......
.......
......P
.......
.....K.
....Q..
.......\
    """
    if checkboard(board) :
        checkmate(board)

if __name__ == "__main__":
    main()
