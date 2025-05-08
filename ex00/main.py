#!/usr/bin/env python3

from checkmate import checkmate 
# from checkmate import Pos_K

def main():
    board = """\
.......
......P
..K....
.P.P...
.......
.......
.......\
    """
    checkmate(board)

if __name__ == "__main__":
    main()
