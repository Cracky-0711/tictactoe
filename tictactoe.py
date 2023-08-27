"""
Tic Tac Toe Player
"""

import math
import copy

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
    # EMPTYの数を数えてXかOを判断する
    empty_counter = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                empty_counter += 1
    if empty_counter % 2 == 0:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                actions.append([i,j])
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # player関数でプレイヤーを確認
    x_or_o = player(board)
    new_board = board.copy()
    # 与えられた座標をPlayerの文字(XかO)にする
    if action[0] < 0 or action[0] > 2 or action[1] < 0 or action[1] > 2:
        raise ValueError
    elif new_board[action[0]][action[1]] != None:
        raise ValueError
    new_board[action[0]][action[1]] = x_or_o
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        # 横に３つ並んでないかの確認
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            if board[i][0] != None:
                return board[i][0]
        # 縦に３つ並んでないかの確認
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[0][i] != None:
                return board[0][i]
    # ななめに３つ並んでないかの確認
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] != None:
            return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] != None:
            return board[0][0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empty_counter = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                empty_counter += 1
    if empty_counter == 0:
        return True
    if winner(board) != None:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    if win == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    action = []
    if player(board) == X:
        v = -2
        for a in actions(board):
            n = Min_value(result(board, a))
            if v < n:
                v = n.copy()
                action = a.copy()
    if player(board) == O:
        v = 2
        for a in actions(board):
            n = Max_value(result(board, a))
            if v > n:
                v = n.copy()
                action = a.copy()
    return action
        
    
def Max_value(board):
    v = -1
    if terminal(board):
        return utility(board)
    for action in actions(board):
        a = Min_value(result(board, action))
        if a == 1:
            return a
        if v < a:
            v = a.copy()
    return v

def Min_value(board):
    v = 1
    if terminal(board):
        return utility(board)
    for action in actions(board):
        a = Max_value(result(board, action))
        if a == -1:
            return a
        if v > a:
            v = a.copy()
    return v