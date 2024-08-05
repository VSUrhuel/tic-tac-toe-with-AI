"""
Tic Tac Toe Player
"""

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
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                countX += 1
            elif board[i][j] == O:
                countO += 1 
    if countX > countO:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    options = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                options.add((i,j))
    return options


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if type(action) is not tuple:
        raise ValueError
    if board[action[0]][action[1]] != EMPTY:
        raise ValueError
    
    boardCopy = [[EMPTY for i in range(3)] for j in range(3)]
    
    for i in range(3):
        for j in range(3):
            boardCopy[i][j] = board[i][j]
    for i in range(3):
        for j in range(3):
            if i == action[0] and j == action[1]:
                boardCopy[i][j] = player(board)
                
               
                return boardCopy
    
    return boardCopy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkPlayerWinner(board, X):
        return X
    elif checkPlayerWinner(board, O):
        return O
    return None

def checkPlayerWinner(board, player):

    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True
    return False

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if checkPlayerWinner(board, X):
        return 1
    elif checkPlayerWinner(board, O):
        return -1
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if player(board) == X:
        max = -math.inf
        for action in actions(board):
            if minValue(result(board, action)) > max:
                max = minValue(result(board, action))
                optimal = action
        return optimal    
    else:
        min = math.inf
        for action in actions(board):
            if maxValue(result(board, action)) < min:
                min = maxValue(result(board, action))
                optimal = action
        return optimal
    
   
def maxValue(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, minValue(result(board, action)))
    return v

def minValue(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))
    return v
