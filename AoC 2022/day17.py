# %%
input_rocks = """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
"""

example = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

#%%
from utils import get_input
import numpy as np
from tqdm import tqdm

CAVE_WIDTH = 7


def parse_rocks(input_rocks):
    rocks = []
    current_rock = []
    for line in input_rocks.split("\n"):
        if line:
            current_rock.append(line)
        else:
            rocks.append(current_rock)
            current_rock = []
    return rocks


def gas_moves(right_move, rock_pos, rock_index, rock, cave):
    if right_move and can_move_right(rock_pos, rock_index, rock, cave):
        return (0, 1)
    if not right_move and can_move_left(rock_pos, rock_index, rock, cave):
        return (0, -1)
    return (0, 0)


def add_rock(cave, rock_pos, rock):
    for i, row in enumerate(rock):
        for j, col in enumerate(row):
            if col != ".":
                cave[len(cave) - rock_pos[0] - (len(rock) - i)][rock_pos[1] + j] = 1


def can_move_right(rock_pos, rock_index, rock, cave):
    if rock_pos[1] + len(rock[0]) == CAVE_WIDTH:
        return False

    # if rock_index != 1 and not cave[
    #     len(cave) - rock_pos[0] : len(cave) - rock_pos[0] + len(rock),
    #     rock_pos[1] + len(rock[0]) : rock_pos[1] + len(rock[0]) + 1,
    # ].any():
    #     return True

    conflicts = [
        [(0, 3)],
        [(0, 1), (1, 2), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(0, 1), (1, 1)],
    ]

    for conflict in conflicts[rock_index]:
        if (
            cave[len(cave) - 1 - rock_pos[0] - conflict[0]][
                rock_pos[1] + conflict[1] + 1
            ]
            == 1
        ):
            return False
    return True


def can_move_left(rock_pos, rock_index, rock, cave):
    if rock_pos[1] == 0:
        return False

    # if not cave[
    #     len(cave) - rock_pos[0] : len(cave) - rock_pos[0] + len(rock),
    #     rock_pos[1] - 1 : rock_pos[1]
    # ].any():
    #     return True

    conflicts = [
        [(0, 0)],
        [(0, 1), (1, 0), (2, 1)],
        [(0, 0), (1, 2), (2, 2)],
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(0, 0), (1, 0)],
    ]

    for conflict in conflicts[rock_index]:
        if (
            cave[len(cave) - 1 - rock_pos[0] - conflict[0]][
                rock_pos[1] + conflict[1] - 1
            ]
            == 1
        ):
            return False
    return True


def can_fall(rock_pos, rock, rock_index, cave):
    if rock_pos[0] == 0:
        return False

    if (
        rock_index != 1
        and not cave[
            len(cave) - rock_pos[0] : len(cave) - rock_pos[0] + 1,
            rock_pos[1] : rock_pos[1] + len(rock[0]),
        ].any()
    ):
        return True

    conflicts = [
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 1), (1, 0), (1, 2)],
        [(0, 0), (0, 1), (0, 2)],
        [(0, 0)],
        [(0, 0), (0, 1)],
    ]

    for conflict in conflicts[rock_index]:
        if cave[len(cave) - rock_pos[0] - conflict[0]][rock_pos[1] + conflict[1]]:
            return False
    return True


def simulate(rocks, moves, max_rock):
    ROCK_SPAWN = np.array((3, 2))  # heigh, width

    cave = np.zeros((3, CAVE_WIDTH), dtype=np.uint8)

    pieces = {}
    (cycle_index, cycle_height) = (0, 0)

    height = 0
    move_index = 0
    last_cut = 0

    rock_index = 0

    with tqdm(total=max_rock) as pbar:
        while rock_index < max_rock:
            rock = rocks[rock_index % len(rocks)]

            new_lines = max(0, (height + 3 + len(rock)) - (len(cave) + last_cut))
            cave = np.concatenate(
                (np.zeros((new_lines, CAVE_WIDTH), dtype=np.uint8), cave), axis=0
            )

            rock_pos = np.array((height - last_cut, 0)) + ROCK_SPAWN

            while True:
                rock_pos += gas_moves(
                    moves[move_index], rock_pos, rock_index % len(rocks), rock, cave
                )
                # Gas moves
                move_index = (move_index + 1) % len(moves)

                if can_fall(rock_pos, rock, rock_index % len(rocks), cave):
                    rock_pos += (-1, 0)
                else:
                    add_rock(cave, rock_pos, rock)
                    break

            # cut_line = np.where(cave.sum(axis=1) == CAVE_WIDTH)[0]
            # if cut_line.size > 1:
            #     height = len(cave) + last_cut - np.where(cave.sum(axis=1) > 0)[0][0]
            #     # print("height before:", height)

            #     # print("Cut", cut_line)
            #     last_cut += len(cave) - cut_line[0]
            #     cave = cave[: cut_line[0]]
            #     if cave.sum() == 0:
            #         print(rock_index)

            # print("Rock", rock_index)
            # print(cave[:10])

            # if np.where(cave.sum(axis=1) > 0)[0].any():
            #     height = len(cave) + last_cut - np.where(cave.sum(axis=1) > 0)[0][0]

            # int(len(cave))
            # print("height after", height)
            # print()

            old_height = height
            height = len(cave) + last_cut - np.where(cave.sum(axis=1) > 0)[0][0]

            current = (height - old_height, rock_index % len(rocks), move_index)
            if current in pieces.keys() and cycle_index == 0:
                print("MAGIC", current)
                print(rock_index, height)
                cycle_index = rock_index
                cycle_height = height - pieces[current]
                cycle_end = max_rock - (max_rock % rock_index)
                rock_index = cycle_end
                print(rock_index, height)
            else:
                pieces[current] = height
            rock_index += 1
            pbar.update(1)

    print(cycle_height, cycle_index, cycle_end)
    print(cycle_height * ((max_rock // cycle_index) - 1) + height)
    return height


def part1(rocks, moves):
    MAX_ROCK = 2022
    height = simulate(rocks, moves, MAX_ROCK)
    print("Part1:", height)


def part2(rocks, moves):
    # El hecho es que hay ciclos de: (indice instruccion, tipo figura, aumento altura)
    MAX_ROCK = 1_000_000_000_000
    height = simulate(rocks, moves, MAX_ROCK)
    print("Part2:", height)


# %%
if __name__ == "__main__":
    # moves = get_input(day=17)
    moves = example.strip().splitlines()
    moves = [move == ">" for move in list(moves[0])]
    rocks = parse_rocks(input_rocks)
    part1(rocks, moves)
    part2(rocks, moves)
# %%
# %%
