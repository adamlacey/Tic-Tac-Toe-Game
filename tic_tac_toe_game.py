def play_game():
  board = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
  ]
  player = "X"
  # Continues game until it finishes.
  while not is_game_over(board):
    print(print_board(board))
    print("It's " + player + "'s turn.")
    try:
    # `input` asks the user to type in a string.
    # Which is then converted into a number using `int`.
        row = int(input("Enter a row: "))
        column = int(input("Enter a column: "))
        if row not in [0, 1, 2] or column not in [0, 1, 2]:
            raise ValueError("Invalid input. Please enter either 0, 1 or 2.")
    except ValueError as e:
        # Handle invalid input error if user 
        # doesn't enter correct number.
        print(e)
        continue
    if make_move(board, row, column, player):
        if player == "X":
            player = "O"
        else:
            player = "X"
    else:
        continue
    # Game over, final result printed.
    print(print_board(board))
    if is_draw(board):
        print("It's a draw.")
    else:
        print("Game over!")

# Function to check if game has ended in a draw.
def is_draw(board):
  for row in board:
    for cell in row:
      if cell == ".":
        return False
  return True

# Function to print the current board state.
def print_board(board):
  formatted_rows = []
  for row in board:
    formatted_rows.append(" ".join(row))
  grid = "\n".join(formatted_rows)
  return grid

# Function to check if tile on board is empty.
def is_position_valid(board, row, column):
  return board[row][column] == '.'

# Function to make a move on the board.
def make_move(board, row, column, player):
  if is_position_valid(board, row, column):
    board[row][column] = player
    return True
  else:
    print("This position is already occupied. Please pick a different tile")
    return False

# This function will extract three cells from the board.
def get_cells(board, coord_1, coord_2, coord_3):
  return [
    board[coord_1[0]][coord_1[1]],
    board[coord_2[0]][coord_2[1]],
    board[coord_3[0]][coord_3[1]]
  ]

# Function will check if the group is fully placed
# with player marks, no empty spaces.
def is_group_complete(board, coord_1, coord_2, coord_3):
  cells = get_cells(board, coord_1, coord_2, coord_3)
  return "." not in cells

# Function will check if the group is all the same
# player mark: X X X or O O O
def are_all_cells_the_same(board, coord_1, coord_2, coord_3):
  cells = get_cells(board, coord_1, coord_2, coord_3)
  return cells[0] != '.' and cells[0] == cells[1] and cells[1] == cells[2]

# List of groups to check:

groups_to_check = [
  # Rows
  [(0, 0), (0, 1), (0, 2)],
  [(1, 0), (1, 1), (1, 2)],
  [(2, 0), (2, 1), (2, 2)],
  # Columns
  [(0, 0), (1, 0), (2, 0)],
  [(0, 1), (1, 1), (2, 1)],
  [(0, 2), (1, 2), (2, 2)],
  # Diagonals
  [(0, 0), (1, 1), (2, 2)],
  [(0, 2), (1, 1), (2, 0)]
]

# Function to check if a user won.
def is_game_over(board):
  for group in groups_to_check:
    # If any of them are empty, they're not a
    # winning row, so we skip them.
    if is_group_complete(board, group[0], group[1], group[2]):
      if are_all_cells_the_same(board, group[0], group[1], group[2]):
        return True
  return False # If we get here, we didn't find a winning row.

print("Game time!")
play_game()