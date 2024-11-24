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
    count_x=0
    count_o=0
    for i in board:
        for val in i:
            if(val==X):
                count_x+=1
            elif(val==O):
                count_o+=1
    if(count_x>count_o):
        return O
    else:
        return X

    
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is None:  # Check if the cell is empty
                possible_actions.add((i, j))
    return possible_actions

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if not (0 <= action[0] < 3 and 0 <= action[1] < 3):
        raise ValueError("Action out of bounds")
    
    if board[action[0]][action[1]] is not EMPTY:
        raise ValueError("Invalid action")

    # Create a deep copy of the board
    new_board = copy.deepcopy(board)

    # Apply the action for the current player
    new_board[action[0]][action[1]] = player(board)
    return new_board




def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
     # Check rows for a winner
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
    
    # Check columns for a winner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    
    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    
    # If no winner, return None
    return None      


    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True  # Game is over if there is a winner

    # Check if the board is full (no empty cells)
    for row in board:
        if EMPTY in row:
            return False

    return True  # Game is over if no moves are left



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)  # Use the winner function to check the winner
    
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0

    raise NotImplementedError


def minimax(board):
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        _, action = max_value(board, -math.inf, math.inf)
    else:
        _, action = min_value(board, -math.inf, math.inf)

    return action


def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board), None

    v = -math.inf
    best_action = None
    for action in actions(board):
        new_board = result(board, action)
        min_val, _ = min_value(new_board, alpha, beta)
        if min_val > v:
            v = min_val
            best_action = action
        alpha = max(alpha, v)
        if alpha >= beta:
            break

    return v, best_action


def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board), None

    v = math.inf
    best_action = None
    for action in actions(board):
        new_board = result(board, action)
        max_val, _ = max_value(new_board, alpha, beta)
        if max_val < v:
            v = max_val
            best_action = action
        beta = min(beta, v)
        if beta <= alpha:
            break

    return v, best_action