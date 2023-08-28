# Define the board size and the symbols for each player
BOARD_SIZE = 3
X = "X"
O = "O"
EMPTY = " "

# Define a class to represent the board state
class Board:
    def __init__(self):
        # Initialize an empty board as a list of lists
        self.board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        # Initialize the current player as X
        self.player = X

    def display(self):
        # Print the board to the console
        for row in self.board:
            print("|".join(row))
        print()

    def is_valid(self, x, y):
        # Check if a move is valid, i.e. within the board and on an empty cell
        return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE and self.board[x][y] == EMPTY

    def make_move(self, x, y):
        # Make a move on the board and switch the current player
        if self.is_valid(x, y):
            self.board[x][y] = self.player
            self.player = O if self.player == X else X
            return True
        return False

    def is_full(self):
        # Check if the board is full, i.e. no empty cells left
        return EMPTY not in [cell for row in self.board for cell in row]

    def get_winner(self):
        # Check if there is a winner, i.e. three symbols in a row, column, or diagonal
        # Return the winner symbol (X or O) or None if there is no winner yet
        # Loop through rows
        for i in range(BOARD_SIZE):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != EMPTY:
                return self.board[i][0]
        # Loop through columns
        for j in range(BOARD_SIZE):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] != EMPTY:
                return self.board[0][j]
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != EMPTY:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != EMPTY:
            return self.board[0][2]
        # No winner yet
        return None

# Define a function to implement the minimax algorithm
def minimax(board, depth, is_maximizing):
    # Base case: check if the game is over (win, loss, or draw)
    winner = board.get_winner()
    if winner == X:
        return 1 # X wins
    elif winner == O:
        return -1 # O wins
    elif board.is_full():
        return 0 # Draw

    # Recursive case: evaluate all possible moves and choose the best one
    if is_maximizing:
        # Maximizing player (X) wants to choose the move with the highest score
        best_score = -float("inf") # Initialize the best score as negative infinity
        best_move = None # Initialize the best move as None
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board.is_valid(i, j):
                    # Make a temporary move and evaluate its score using recursion
                    board.make_move(i, j)
                    score = minimax(board, depth + 1, False) # Switch to minimizing player
                    board.make_move(i, j) # Undo the temporary move
                    board.player = X # Switch back to maximizing player
                    # Update the best score and move if needed
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move # Return the best move for X

    else:
        # Minimizing player (O) wants to choose the move with the lowest score
        best_score = float("inf") # Initialize the best score as positive infinity
        best_move = None # Initialize the best move as None
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board.is_valid(i, j):
                    # Make a temporary move and evaluate its score using recursion
                    board.make_move(i, j)
                    score = minimax(board, depth + 1, True) # Switch to maximizing player
                    board.make_move(i, j) # Undo the temporary move
                    board.player = O # Switch back to minimizing player
                    # Update the best score and move if needed
                    if score < best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move # Return the best move for O

# Define a function to get the human player's move from input
def get_human_move(board):
    while True:
        # Get the row and column numbers from the user
        try:
            x = int(input("Enter row number (1-3): ")) - 1
            y = int(input("Enter column number (1-3): ")) - 1
        except ValueError:
            print("Invalid input. Please enter numbers between 1 and 3.")
            continue
        # Check if the move is valid and return it if so
        if board.is_valid(x, y):
            return (x, y)
        else:
            print("Invalid move. The cell is already occupied or out of range.")

# Define a function to play the game interactively on the console
def play_game():
    # Create a new board and display it
    board = Board()
    board.display()

    # Loop until the game is over
    while True:
        # Get the move for the current player
        if board.player == X:
            # X is the computer, use minimax to get the best move
            print("Computer's turn (X):")
            move = minimax(board, 0, True)
        else:
            # O is the human, get the move from input
            print("Human's turn (O):")
            move = get_human_move(board)
        
        # Make the move on the board and display it
        x, y = move
        board.make_move(x, y)
        board.display()

        # Check if the game is over and print the result
        winner = board.get_winner()
        if winner == X:
            print("X wins!")
            break
        elif winner == O:
            print("O wins!")
            break
        elif board.is_full():
            print("It's a draw!")
            break

# Start the game
play_game()
