import numpy as np

board = np.array([['#', '-', '#', '#', '-'],
                  ['#', '-', '#', '#', '#'],
                  ['#', '-', '-', '-', '#'],
                  ['-', '*', '*', '#', '-'],
                  ['-', '#', '-', '-', '-'],
                  ['-', '-', '#', '-', '-']])

"""
The game is a tetris-like falling block game.
The '#' represent boxes.
The '-' represent empty spaces.
The '*' represent obstacles.
All of the boxes fall down one space at a time simultaneously until they hit the bottom, hit a stack of boxes already at the bottom, or hit an obstacle.
If they hit an obstacle they explode and destroy all of the boxes adjacent to them (including corners).

At first I fooled around with trying to go through all of the indices and decide what to do at each point but that's tricky because everything is meant to happen simultaneously and if you have multiple spaces that are adjacent and require some change at the same time it gets difficult to keep track of.
I then decided to reason backwards and start from what the end result is supposed to be.
I decided to go column by column and if there is an obstacle to blow up all of the boxes above them at the beginning.
Then for all of the columns that don't have obstacles I counted the number of boxes and then stacked that many boxes at the bottom spaces.

If I come back to this I want to see if it's possible to streamline it so there isn't 10 million nested for loops.
"""

def game(board):
    for j in range(len(board[0,:])):
        if '*' in board[:, j]:
            for i in range(len(board[:,0])):
                if board[i,j] == "#":
                    for k in range(max(0, i-1), min(i+2,len(board[0,:j]))):
                        for l in range(max(0,j-1), min(j+2,len(board[:,0]))):
                            if board[k,l] != '*':
                                board[k,l] = '-'

    for j in range(len(board[0,:])):
        numSharps = list(board[:,j]).count('#')
        board[board[:,j] == '#',j]='-'
        board[len(board[:,0])-numSharps:,j]='#'
    print(board)

game(board)