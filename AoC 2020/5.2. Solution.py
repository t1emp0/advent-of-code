filepath = "5.1. Puzzle input.txt"

with open(filepath) as fp:
    boards = fp.readlines()

# Remove whitespace characters like \n at the end of each line
boards = [x.strip() for x in boards]

# Convert the board to binary, then to decimal
board_ids = [int(board.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0"), 2) for board in boards]

print(max(board_ids))

# Finding the missing seat_id
missing_id = [x+1 for x in board_ids if (x+1 not in board_ids) and (x+2 in board_ids)]

print(missing_id)