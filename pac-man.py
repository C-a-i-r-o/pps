import random

# Constants
EMPTY = '.'
PACMAN = 'P'
GHOST = 'G'
COIN = 'C'
ROWS = 5
COLS = 5

# Initialize the game board
board = [[EMPTY] * COLS for _ in range(ROWS)]
pacman_row, pacman_col = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)
board[pacman_row][pacman_col] = PACMAN

ghost_row, ghost_col = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)
while (ghost_row, ghost_col) == (pacman_row, pacman_col):
    ghost_row, ghost_col = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)
board[ghost_row][ghost_col] = GHOST

coin_row, coin_col = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)
while (coin_row, coin_col) == (pacman_row, pacman_col) or (coin_row, coin_col) == (ghost_row, ghost_col):
    coin_row, coin_col = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)
board[coin_row][coin_col] = COIN

# Game loop
while True:
    # Display the current state of the board
    for row in board:
        print(' '.join(row))
    print()

    # Get user input
    move = input("Enter your move (W/A/S/D): ").upper()

    # Update Pac-Man's position
    board[pacman_row][pacman_col] = EMPTY

    if move == 'W' and pacman_row > 0:
        pacman_row -= 1
    elif move == 'A' and pacman_col > 0:
        pacman_col -= 1
    elif move == 'S' and pacman_row < ROWS - 1:
        pacman_row += 1
    elif move == 'D' and pacman_col < COLS - 1:
        pacman_col += 1

    # Check for collisions
    if (pacman_row, pacman_col) == (ghost_row, ghost_col):
        print("Game Over! You were caught by the ghost.")
        break
    elif (pacman_row, pacman_col) == (coin_row, coin_col):
        print("Congratulations! You collected the coin.")
        break

    # Update Pac-Man's new position
    board[pacman_row][pacman_col] = PACMAN

    # Move the ghost randomly
    board[ghost_row][ghost_col] = EMPTY
    ghost_row, ghost_col = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)
    board[ghost_row][ghost_col] = GHOST
