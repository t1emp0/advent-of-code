from utils import get_input
import numpy as np
from tqdm import tqdm
import re


def manhattan_dist(start, end):
    return abs(end[0] - start[0]) + abs(end[1] - start[1])


def part1(points):
    sensors = [(p[:2], manhattan_dist(p[:2], p[2:])) for p in points]

    CHECK_ROW = 2000000

    pos = set()
    for sensor, dist in sensors:
        diff = abs(CHECK_ROW - sensor[1])
        if diff < dist:
            remaining = dist - diff
            start, end = sensor[0] - remaining, sensor[0] + remaining
            [pos.add(i) for i in range(start, end)]
    print("Part1:", len(pos))


def check_row(sensors, excess, n):
    # For each sensor: we get its absolute start and end, on this row
    starts = sensors[:, 0] - excess
    ends = sensors[:, 0] + excess

    # Since there's only one point, it must be in the boundary: next to an edge
    boundary = starts[0 < starts] - 1
    np.append(boundary, ends[ends < n] + 1)

    # If no sensor range contains the number, it is the one we are looking for!
    for num in boundary:
        for start, end in zip(starts, ends):
            if start <= num <= end:
                break
        else:
            return num


def part2(points):
    sensors = np.array([(*p[:2], manhattan_dist(p[:2], p[2:])) for p in points])
    sensors, distances = sensors[:, :2], sensors[:, 2]

    N = 4_000_000
    for row in tqdm(range(N + 1)):
        excess = distances - np.abs(row - sensors[:, 1])
        missing = check_row(sensors[excess > 0], excess[excess > 0], N)
        if missing:
            # Conversion to int to prevent np.int32 overflow
            print("Part 2:", missing, row)
            print(int(missing) * N + row)
            return


if __name__ == "__main__":
    data = get_input(day=15)
    points = [re.findall("[-]*[0-9]+", d) for d in data]
    points = [list(map(int, vals)) for vals in points]

    part1(points)
    part2(points)
