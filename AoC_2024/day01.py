# %%
example = """3   4
4   3
2   5
1   3
3   9
3   3
"""

# %%
from utils import get_input

from collections import Counter


def part1(data):
    list_1 = sorted([int(d.split("  ")[0]) for d in data])
    list_2 = sorted([int(d.split("  ")[1]) for d in data])
    res = sum([abs(i - j) for i, j in zip(list_1, list_2)])
    print("Part1:", res)


def part2(data):
    list_1 = sorted([int(d.split("  ")[0]) for d in data])
    list_2 = Counter([int(d.split("  ")[1]) for d in data])
    res = sum([i * list_2[i] for i in list_1])
    print("Part2:", res)


if __name__ == "__main__":
    data = get_input(day=1, year=2024)
    data = example.strip().splitlines()
    part1(data)
    part2(data)

# %%
