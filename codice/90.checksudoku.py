ROWCOL = 3
DIM = ROWCOL * ROWCOL


def is_valid_row(board, row_index):
    """Check if row is valid"""
    row = board[row_index]
    # Filter out empty cells (0)
    filled = []
    for cell in row:
        if cell != 0:
            filled.append(cell)
    # Check for duplicates using set
    return len(filled) == len(set(filled))

def is_valid_column(board, col_index):
    """Check if column is valid"""
    column = []
    for row in range(DIM):
        column.append(board[row][col_index])
    
    filled = []
    for cell in column:
        if cell != 0:
            filled.append(cell)
    
    return len(filled) == len(set(filled))


def is_valid_column_v2(board, col_index):
    """Check if column is valid"""
    cont = [0]*DIM
    for row in range(DIM):
        val = board[row][col_index]
        if val != 0: 
            cont[val-1] += 1
    for i in range(DIM):
        if cont[i] > 1:
            return False
    return True


def is_valid_subgrid(board, start_row, start_col):
    """Check 3x3 grid"""
    cells = []
    for i in range(start_row, start_row + ROWCOL):
        for j in range(start_col, start_col + ROWCOL):
            if board[i][j] != 0:
                cells.append(board[i][j])
    return len(cells) == len(set(cells))

def is_valid_sudoku(board):
    """Check entire board"""
    # Check all rows
    for i in range(DIM):
        if not is_valid_row(board, i):
            return False
    
    # Check all columns
    for j in range(DIM):
        if not is_valid_column(board, j):
            return False
    
    # Check all 3x3 subgrids
    for i in range(0, DIM, ROWCOL):
        for j in range(0, DIM, ROWCOL):
            if not is_valid_subgrid(board, i, j):
                return False
    
    return True



# ----- Test --------
valid_board = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]

print(is_valid_sudoku(valid_board))  # True

