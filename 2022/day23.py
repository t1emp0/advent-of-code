from utils import get_input
import numpy as np
from collections import deque

check_north = lambda row, col, dirs: (row - 1, col) if 1 not in dirs else None
check_south = lambda row, col, dirs: (row + 1, col) if 1 not in dirs else None
check_east = lambda row, col, dirs: (row, col + 1) if 1 not in dirs else None
check_west = lambda row, col, dirs: (row, col - 1) if 1 not in dirs else None


def next_step(elf, field, iteration):
    row, col = elf

    if np.count_nonzero(field[row - 1 : row + 2, col - 1 : col + 2]) == 1:
        return (row, col)

    NW, N, NE = field[row - 1, col - 1 : col + 2]
    W, _, E = field[row, col - 1 : col + 2]
    SW, S, SE = field[row + 1, col - 1 : col + 2]

    directions = deque(
        [
            check_north(row, col, [NW, N, NE]),
            check_south(row, col, [SW, S, SE]),
            check_west(row, col, [NW, W, SW]),
            check_east(row, col, [NE, E, SE]),
        ]
    )
    directions.rotate(-iteration)
    directions = [d for d in directions if d is not None]

    return directions[0] if directions else (row, col)


def run_simulation(field, part1=False):
    new_field = np.zeros(np.array(field).shape, dtype=np.uint8)
    new_field[np.where(field == "#")] = 1
    field = np.pad(new_field, pad_width=1, mode="constant", constant_values=0)

    elves = list(zip(*np.where(field == 1)))
    prev_elves = elves.copy()
    iteration = 0

    while True:
        # Calculate next steps and get those unique
        step = [next_step(elf, field, iteration) for elf in elves]
        not_repeated = {e: s for (e, s) in zip(elves, step) if step.count(s) == 1}
        elves = [not_repeated[e] if e in not_repeated else e for e in elves]
        iteration += 1

        # If equilibrium is reached, stop
        if elves == prev_elves:
            break
        prev_elves = elves.copy()

        # Reshape the field so that everyone can move freely
        elves = np.array(elves)
        elves_range = elves.max(axis=0) - elves.min(axis=0)

        field = np.zeros(elves_range + (3, 3), dtype=np.uint8)
        elves = elves - elves.min(axis=0) + (1, 1)
        elves = list(zip(elves[:, 0], elves[:, 1]))

        # Put everyone back in place
        for i, j in elves:
            field[i][j] = 1

        if part1 and iteration == 10:
            break

    inner_points = (len(field) - 2) * (len(field[0]) - 2) - len(elves)
    return inner_points if part1 else iteration


def part1(field):
    inner_points = run_simulation(field, part1=True)
    print("Inner points:", inner_points)


def part2(field):
    num_rounds = run_simulation(field)
    print("Rounds until equilibrium:", num_rounds)


if __name__ == "__main__":
    data = get_input(day=23)
    field = np.array([list(d) for d in data])
    part1(field)
    part2(field)
