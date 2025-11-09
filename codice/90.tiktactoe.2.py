NUM_MOVES = 9
NO_WINNER = 0

def get_move(player):
    move = input(f"Player {player} enter your move (row,col): ")
    parts = move.split(',')
    row = int(parts[0].strip()) - 1
    col = int(parts[1].strip()) - 1
    while not(0 <= row < 3 and 0 <= col < 3):
        print("Row and column must be between 1 and 3.")
        move = input(f"Player {player} enter your move (row,col): ")
        parts = move.split(',')
        row = int(parts[0].strip()) - 1
        col = int(parts[1].strip()) - 1
    return row, col

## MAIN FLOW

board = [[0,0,0],[0,0,0],[0,0,0]]

current_player = 1
count_moves = 0
winner = NO_WINNER

row, col = get_move(current_player)
valid_move = (board[row][col] == 0) 
while not valid_move:
    print("Invalid move: cell already taken. Try again.\n")
    row, col = get_move(current_player)
    valid_move = (board[row][col] == 0) 

board[row][col] = player
count_moves += 1
winner = check_winner(board)
while count_moves < NUM_MOVES and winner == NO_WINNER:
    print("Valid mode, no winner, change player")
    row, col = get_move(current_player)
    valid_move = (board[row][col] == 0) # check_move_validity(row,col)
    if valid_move:
        board[row][col] = player #update_board(board, row, col, current_player)
        count_moves += 1
        winner = check_winner(board)
        # changing player -- eventually not useful
        if current_player == 1:
            current_player = 2
        else:
            current_player = 1
        # current_player = (current_player % 2) + 1

        # Check winner
    else:
        print("Invalid move: cell already taken. Try again.\n")

if winner != 0:
    print(f"Player {winner} wins the game!")
else:
    print("Game over: it's a draw.")
