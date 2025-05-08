#!/usr/bin/env python3

from checkmate import checkmate 
# from checkmate import Pos_K

def main():
    board = """\
.......
......P
..K....
.......
..R....
.......
.......\
    """
    checkmate(board)

if __name__ == "__main__":
    main()
