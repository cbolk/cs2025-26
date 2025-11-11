def check_rows(board):
    for row in board:
        if row[0] != 0 and row[0] == row[1] and row[1] == row[2]:
            return row[0]
    return 0

def check_columns(board):
    for col in range(3):
        if board[0][col] != 0 and board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            return board[0][col]
    return 0

def check_diagonals(board):
    # Top-left to bottom-right
    if board[0][0] != 0 and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    # Top-right to bottom-left
    if board[0][2] != 0 and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    return 0

def check_winner(board):
    winner = check_rows(board)
    if winner != 0:
        return winner
    winner = check_columns(board)
    if winner != 0:
        return winner
    winner = check_diagonals(board)
    return winner

# ---- MAIN SCRIPT --------

board = []
for i in range(3):
    row_input = input(f"Enter row {i + 1} (comma-separated): ")
    row = []
    for value in row_input.split(','):
        row.append(int(value.strip()))
    board.append(row)

# Examble board
# board = [
#     [1, 2, 0],
#     [2, 1, 0],
#     [2, 1, 1]
# ]

result = check_winner(board)
if result == 0:
    print("No winner.")
else:
    print(f"Player {result} wins!")
