from utils import get_input
import numpy as np


def normalize_data(data, offset):
    GENERATOR_X = 500
    pairs = np.array([(d[i], d[i - 1]) for d in data for i in range(1, len(d))])

    min_x = pairs[:, :, 0].flatten().min()
    pairs = pairs - np.array((min_x - offset, 0))

    return pairs, GENERATOR_X - min_x + offset


def create_cave(pairs, offset):
    max_x = pairs[:, :, 0].flatten().max() + 1
    max_y = pairs[:, :, 1].flatten().max() + (3 if offset else 1)

    cave = np.zeros((max_y, max_x + offset * 2), dtype=np.uint8)

    if offset:
        cave[-1] += 1

    for start, end in pairs:
        count = np.abs(end - start).max()
        norm = np.sign(end - start)
        current = start
        for _ in range(count + 1):
            cave[current[1]][current[0]] = 1
            current += norm

    return cave


def next_sand(sand, cave):
    s_y, s_x = sand
    if not cave[s_y + 1][s_x]:
        return (s_y + 1, s_x)
    if not cave[s_y + 1][s_x - 1]:
        return (s_y + 1, s_x - 1)
    if not cave[s_y + 1][s_x + 1]:
        return (s_y + 1, s_x + 1)
    return None


def simulate_sand(cave, generator):
    sand_count = 0

    while True:
        sand = (0, generator)
        next = next_sand(sand, cave)

        while next:
            if next[0] == len(cave) - 1:
                return sand_count
            sand = next
            next = next_sand(sand, cave)

        cave[sand[0]][sand[1]] = 1
        sand_count += 1

        if cave[0][generator] == 1:
            return sand_count


def part1(data):
    offset = 0
    data, generator = normalize_data(data, offset)
    cave = create_cave(data, offset)
    sand = simulate_sand(cave, generator)
    print("Part 1:", sand)


def part2(data):
    offset = 100
    data, generator = normalize_data(data, offset)
    cave = create_cave(data, offset)
    sand = simulate_sand(cave, generator)
    print("Part 2:", sand)


if __name__ == "__main__":
    data = get_input(day=14)
    data = [[list(map(int, i.split(","))) for i in d.split(" -> ")] for d in data]
    part1(data)
    part2(data)
