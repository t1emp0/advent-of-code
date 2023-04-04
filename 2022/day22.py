# %%
example = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
"""

#%%
from utils import get_input
import numpy as np
from collections import deque


def parse_input(data):
    board, instr = data[:-2], data[-1]

    max_len = max([len(b) for b in board])
    board = np.array([list(b.ljust(max_len)) for b in board])

    letters = [-1] + [i for i in range(len(instr)) if instr[i] in ["L", "R"]]
    instr_new = [instr[letters[i - 1] + 1 : letters[i]] for i in range(1, len(letters))]
    instr_new.append(instr[letters[-1] + 1 :])

    instr = list(map(int, instr_new)), [instr[i] for i in letters[1:]]

    return board, instr


def print_board(board):
    [print("".join(b)) for b in board]


def rotate_board(pos, board, turn, facing):
    turn = 1 if turn == "R" else -1
    facing.rotate(-turn)
    pos_x = turn * (len(board[0]) - 1 - pos[1]) % (len(board[0]) - 1)
    pos_y = -turn * (len(board) - 1 - pos[0]) % (len(board) - 1)
    board = np.rot90(board, k=turn)
    return [pos_x, pos_y], board


def part1(board, instr):
    moves, turns = instr
    pos = [0, np.where(board[0] == ".")[0][0]]
    directions = [">", "v", "<", "^"]
    facing = deque(directions)

    for i, move in enumerate(moves):
        line = board[pos[0]]
        col = pos[1]

        for _ in range(move):
            new_col = (col + 1) % len(line)

            if line[new_col] == " ":
                new_col = np.where(line != " ")[0][0]

            if line[new_col] == "#":
                break
            line[col] = facing[0]
            col = new_col

        pos[1] = col
        # print(pos)

        if i == len(turns):
            line[col] = facing[0]
            # print(turns[i - 1], move)
            break

        pos, board = rotate_board(pos, board, turns[i], facing)

    # Return board to starting rotation (right) to get the correct coords
    end_facing = directions.index(facing[0])
    while facing[0] != directions[0]:
        # print("correcting rotation", facing[0])
        pos, board = rotate_board(pos, board, "R", facing)

    print_board(board)

    pos += np.array([1, 1])
    password = 1000 * pos[0] + 4 * pos[1] + end_facing
    print("Part1:", password)


def part2(data):
    print("Part2:")


if __name__ == "__main__":
    data = get_input(day=22, strip=False)
    # data = example.splitlines()
    board, instr = parse_input(data)
    part1(board, instr)
    # low 88276, 88278

    # part2(data)

# %%
