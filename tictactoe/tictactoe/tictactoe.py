"""
Tic Tac Toe Player
"""
import copy
import math

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
        for j in range(len(board[0])):
            if board[i][j] == X:
                player_x += 1

            if board[i][j] == O:
                player_o = player_o + 1

    if player_x > player_o:
        return O
    else:
        return X


def actions(board):
    moves = set()

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
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
            if board[i][j] == player and i == j:
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


def result(board, action):
    result = copy.deepcopy(board)

    result[action[0]][action[1]] = player(board)
    return result


def winner(board):
    if checkRow(board, X) or checkColumn(board, X) or checkFirstDioganal(board, X) or checkSecondDiagonal(board, X):
        return X
    elif checkRow(board, O) or checkColumn(board, O) or checkFirstDioganal(board, O) or checkSecondDiagonal(board, O):
        return O


class InvalidActionError(Exception):
    pass


def terminal(board):
    if winner(board) is not None:
        return True
    else:
        return False


def utility(board):
    if winner(board) == X:
        return X

    elif winner(board) == O:
        return -1

    else:
        return 0


def minimax(board):
    # Returns the optimal action for the current player on the board.
    if terminal(board):
        return None

    else:
        if player(board) == X:
            move = max_value(board)
            return move

        else:
            move = min_value(board)
            return move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        aux = max_value(result(board, action))
        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move

    return v, move


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')

    move = None
    for action in actions(board):

        aux, action = min_value(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move

    return v, move
