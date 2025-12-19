EMPTY = ' '
PLAYER1 = 'X'
PLAYER2 = '0'
SYMBOLS = {0: EMPTY, 1: PLAYER1, 2: PLAYER2}


def create_board(rows, cols):
    """Create an empty Connect Four board."""
    board = []
    for row in range(rows):
        current_row = []
        for col in range(cols):
            current_row.append(0)
        board.append(current_row)
    return board

def display_board(board):
    """Display the board in a readable format."""
    
    # Display column numbers header
    column_numbers = ' '
    for i in range(1, len(board[0]) + 1):
        column_numbers += str(i) + ' '
    print(column_numbers)

    # Display separator line
    separator = '-' * (len(board[0]) * 2 + 1)
    print(separator)

    # Display board rows
    for row in board:
        row_str = '|'
        for cell in row:
            row_str += SYMBOLS[cell] + '|'
        print(row_str)
    
    # Display separator line
    separator = '-' * (len(board[0]) * 2 + 1)
    print(separator)
    
    # Display column numbers
    column_numbers = ' '
    for i in range(1, len(board[0]) + 1):
        column_numbers += str(i) + ' '
    print(column_numbers)

def is_valid_column(board, col):
    """Check if a move in the specified column is valid."""
    # Check bounds
    if col < 0 or col >= len(board[0]):
        return False
    # Check if top row is empty
    return board[0][col] == 0

def drop_disc(board, col, player):
    """Drop a disc into the specified column."""
    # Check if move is valid
    if not is_valid_column(board, col):
        return -1
    
    # Find lowest empty row (gravity)
    rows = len(board)
    for row in range(rows - 1, -1, -1): # start from last and go back (upwards)
        if board[row][col] == 0:
            board[row][col] = player
            return row
    
    return -1  # Should not reach here if is_valid_column works

def check_horizontal(board, player):
    """Check if player has 4 in a row horizontally."""
    rows = len(board)
    cols = len(board[0])
    
    for row in range(rows):
        for col in range(cols - 3):  # Only check where 4 can fit
            if (board[row][col] == player and
                board[row][col+1] == player and
                board[row][col+2] == player and
                board[row][col+3] == player):
                return True
    return False

def check_vertical(board, player):
    """Check if player has 4 in a row vertically."""
    rows = len(board)
    cols = len(board[0])
    
    for row in range(rows - 3):  # Only check where 4 can fit
        for col in range(cols):
            if (board[row][col] == player and
                board[row+1][col] == player and
                board[row+2][col] == player and
                board[row+3][col] == player):
                return True
    return False

def check_diagonal(board, player):
    """Check if player has 4 in a row diagonally."""
    rows = len(board)
    cols = len(board[0])
    
    # Check / diagonals (bottom-left to top-right)
    for row in range(3, rows):
        for col in range(cols - 3):
            if (board[row][col] == player and
                board[row-1][col+1] == player and
                board[row-2][col+2] == player and
                board[row-3][col+3] == player):
                return True
    
    # Check \ diagonals (top-left to bottom-right)
    for row in range(rows - 3):
        for col in range(cols - 3):
            if (board[row][col] == player and
                board[row+1][col+1] == player and
                board[row+2][col+2] == player and
                board[row+3][col+3] == player):
                return True
    
    return False

def check_winner(board):
    """Check if any player has won."""
    for player in [1, 2]:
        if (check_horizontal(board, player) or
            check_vertical(board, player) or
            check_diagonal(board, player)):
            return player
    return 0


# ----  Test -------

board = create_board()
display_board(board)
