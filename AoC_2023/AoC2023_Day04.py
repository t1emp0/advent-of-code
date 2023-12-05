# %%
example = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

from utils import get_input
import numpy as np


def part1and2(data):
    result_p1 = 0
    multiplier = np.ones(len(data), dtype=np.int64)
    for idx, line in enumerate(data):
        owned, winning = line.split(":")[1].split("|")
        intersection = set([o for o in owned.split(" ") if o != ""]) & set(
            [w for w in winning.split(" ") if w != ""]
        )
        matches = len(intersection) - 1
        multiplier[idx + 1 : idx + matches + 2] += multiplier[idx]
        result_p1 += 2**matches if intersection else 0

    print("Part1:", result_p1)
    print("Part2:", multiplier.sum())


if __name__ == "__main__":
    data = get_input(day=4)
    # data = example.strip().splitlines()
    part1and2(data)
