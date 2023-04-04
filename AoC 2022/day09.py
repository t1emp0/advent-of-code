from utils import get_input
import numpy as np
from numpy.typing import NDArray

step = tuple[NDArray, int]

move_dict = {
    "R": np.array([1, 0]),
    "L": np.array([-1, 0]),
    "U": np.array([0, 1]),
    "D": np.array([0, -1]),
}


def calc_move(dist: NDArray):
    if any(dist == 0):
        return dist // 2
    return np.sign(dist)


def simulate_rope(steps: list[step], rope_length: int):
    start = [0, 0]
    rope_pos = np.zeros((rope_length, 2))
    tail_path = [start]

    for move, count in steps:
        for _ in range(count):
            rope_pos[0] += move

            for i in range(1, len(rope_pos)):
                dist = rope_pos[i - 1] - rope_pos[i]

                if np.sqrt(dist.dot(dist)) >= 2:
                    rope_pos[i] += calc_move(dist)
                    if i == len(rope_pos) - 1:
                        tail_path.append(list(rope_pos[i]))

    unique_tail_pos = np.unique(tail_path, axis=0)
    print(f"{rope_length=} positions:", len(unique_tail_pos))


def part1(steps):
    ROPE_LENGTH = 2
    simulate_rope(steps, ROPE_LENGTH)


def part2(steps):
    ROPE_LENGTH = 10
    simulate_rope(steps, ROPE_LENGTH)


if __name__ == "__main__":
    data = get_input(day=9)
    steps = [d.split(" ") for d in data]
    steps = [(move_dict[move], int(count)) for (move, count) in steps]
    part1(steps)
    part2(steps)
