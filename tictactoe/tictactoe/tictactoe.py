"""
Tic Tac Toe Player
"""
import copy

import tictactoe as ttt

import math
import random
from copy import deepcopy

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
    player_x = 0
    player_o = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == X:
                player_x += 1
                return player_x
            else:
                player_o += 1
                return player_o


def actions(board):

    moves = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i, j))

    return moves


def checkRow(board, player):

    for i in range(len(board)):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True


def checkColumn(board, player):

    for j in range(len(board)):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            return True


def checkFirstDioganal(board, player):
    counter = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if i == j and board[i][j] == player:
                counter = counter + 1

    if counter == 3:
        return True
    else:
        return False


def checkSecondDiagonal(board, player):
    counter = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + j + 1 == 3 and board[i][j] == player:
                counter = counter + 1

    if counter == 3:
        return True
    else:
        return False


def winner(board):

    if checkRow(board, X) or checkColumn(board, X) or checkSecondDiagonal(board, X) or checkSecondDiagonal(board, X):
        return X
    elif checkRow(board, O) or checkColumn(board, O) or checkSecondDiagonal(board, O) or checkSecondDiagonal(board, O):
        return O

    else:
        print("TIE")


class InvalidActionError(Exception):
    pass


def result(board, action):
    if action not in actions(board):
        raise "Not valid"

    else:
        i, j = action
        copy_board = copy.deepcopy(board)
        copy_board[i][j] = player(board)
    return copy_board

def minimax():



def utility():



def terminal(board):

    if winner(board):
        return X

    elif winner(board):
        return O
    else:
        print("TIE")

