"""
Tic Tac Toe Player
"""

from itertools import count
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
    count_x = 0
    count_o = 0
    for i, fila in enumerate(board):
        for j, valor in enumerate(fila):
            if board[i][j] == X:
                count_x += 1
            elif board[i][j] == O:
                count_o += 1
    if count_x == count_o:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    casillas_vacias = set()
    for i, fila in enumerate(board):
        for j, valor in enumerate(fila):
            if board[i][j] == EMPTY:
                casillas_vacias.add((i, j))
    return casillas_vacias


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Movimiento ilegal")
    i, j = action
    ficha = player(board)
    nuevo = copy.deepcopy(board)
    nuevo[i][j] = ficha
    return nuevo

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Revisar victoria en las filas horizontales
    for fila in board:
        if fila[0] == fila[1] == fila[2] and fila[0] is not EMPTY:
            return fila[0]

    # Revisar victoria en las columnas verticales
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not EMPTY:
            return board[0][col]

    # Revisar victoria en la diagonal principal (\)
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]

    # Revisar victoria en la diagonal secundaria (/)
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]

    # Si se evaluó todo el tablero y no hay tres en raya, no hay ganador aún (o es empate)
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Si la función winner nos devuelve un ganador (X u O), el juego terminó
    if winner(board) is not None:
        return True
        
    # Si no hay ganador, verificamos si aún quedan casillas vacías en el tablero
    for fila in board:
        if EMPTY in fila:
            return False
            
    # Si no hay ganador y no quedan casillas vacías, es un empate y el juego terminó
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Obtenemos al ganador utilizando la función que ya creamos
    ganador = winner(board)
    
    # Asignamos el valor según quién haya ganado
    if ganador == X:
        return 1
    elif ganador ==  O:
        return -1
    else:
        # Si el juego terminó pero el ganador es None, significa que es un empate
        return 0


def max_valor(board):
    """Devuelve el valor máximo posible para el tablero actual."""
    if terminal(board):
        return utility(board)
    
    v = -math.inf
    for action in actions(board):
        v = max(v, min_valor(result(board, action)))
        # Poda: si ya encontró la victoria, no necesita seguir buscando
        if v == 1:
            return v
    return v

def min_valor(board):
    """Devuelve el valor mínimo posible para el tablero actual."""
    if terminal(board):
        return utility(board)
    
    v = math.inf
    for action in actions(board):
        v = min(v, max_valor(result(board, action)))
        # Poda: si ya encontró la victoria para O, corta la búsqueda
        if v == -1:
            return v
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Caso base: si el tablero ya es terminal, no hay movimiento posible
    if terminal(board):
        return None
    
    # Identificamos de quién es el turno
    jugador_actual = player(board)

    # Lógica si el turno es de X (Maximizar)
    if jugador_actual == X:
        mejor_valor = -math.inf
        mejor_accion = None
        for action in actions(board):
            # Simulamos el movimiento y calculamos qué haría el rival (O, el minimizador)
            valor_accion = min_valor(result(board, action))
            if valor_accion > mejor_valor:
                mejor_valor = valor_accion
                mejor_accion = action
        return mejor_accion
    # Lógica si el turno es de O (Minimizar)
    else:
        mejor_valor = math.inf
        mejor_accion = None
        for action in actions(board):
            # Simulamos el movimiento y calculamos qué haría el rival (X, el maximizador)
            valor_accion = max_valor(result(board, action))
            if valor_accion < mejor_valor:
                mejor_valor = valor_accion
                mejor_accion = action
        return mejor_accion
