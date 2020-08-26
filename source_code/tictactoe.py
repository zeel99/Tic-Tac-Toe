"""
Tic Tac Toe Player
"""

import math
import copy
import random
import numpy as np

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    countx=0
    counto=0
    ce=0
    if board == [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]:
        return X
    else:
        for row in board:
            for col in row:
                if col == X:
                    countx+=1
                elif col == O:
                    counto+=1
                else:
                    ce=0


        if countx == counto:
            return X
        elif countx > counto:
            return O
        else:
            return X




def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    res = []
    for row in range(3):
        for col in range(3):
            if board[row][col]== EMPTY:
                 res.append([row,col])

    return res


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board2 = copy.deepcopy(board)
    if board2[action[0]][action[1]] != EMPTY:
        raise NameError('invalid')

    board2[action[0]][action[1]] = player(board)

    return board2

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for letter in [X , O] :
        for i in range(3) :
            if board[i] == [letter , letter , letter] :
                return letter
            if board[0][i] == letter and board[1][i] == letter and board[2][i] == letter :
                return letter
        if board[0][0] == letter and board[1][1] == letter and board[2][2] == letter :
            return letter
        if board[2][0] == letter and board[1][1] == letter and board[0][2] == letter :
            return letter


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    res = 0
    for i in board:
        for j in i:
            if j == X or j == O:
                res += 1

    if winner(board) == X or winner(board) == O or res == 9:
        return True

    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board )== X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board) :

    numberlist = [0,2]
    if board == [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]:
        best_move = [random.choice(numberlist),random.choice(numberlist) ]
        return best_move
    elif (board == [[X, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]] ) or (board == [[EMPTY, EMPTY, X],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]] ) or (board == [[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [X, EMPTY, EMPTY]] ) or (board == [[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, X]] ):
          best_move = 1,1
          return best_move
    else:

        # best_move = miv(board)
        for move in actions(board) :
            if player(board) == X :
                for move in actions(board) :
                    if miv(result(board , move)) == mav(board) :
                        best_move = move
                        return best_move

            else:
                for move in actions(board) :
                    if mav(result(board , move)) == miv(board) :
                        best_move = move
                        return best_move


        #
        # for move in actions(board) :
        #      best_move, state = np.argmax(result(board,move)),
        #      lambda : miv(board,-1,1)
        # return best_move




def mav(board) :
    if terminal(board) :
        return utility(board)
    v = float('-inf')
    for move in actions(board) :
          v = max(v , miv(result(board , move)))
    return v




def miv(board) :
    if terminal(board) :
        return utility(board)
    v = float('inf')
    for move in actions(board) :
        v = min(v , mav(result(board , move)))
    return v


def evaluate(board):
    if player(board) == X:
        score =+ 1

    if player(board) == O:
        score =- 1
    return score 



