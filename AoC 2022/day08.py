import numpy as np
from utils import get_input


def traverse_forest_horizontal(data, callback):
    # Callback is the specific function that caculates the value we want
    # We can ignore the outer perimeter: therefore the limits on each loop
    return np.asarray(
        [[callback(line, i) for i in range(1, len(line) - 1)] for line in data[1:-1]]
    )


def get_horizontal_visibility(data):
    def get_visibility(line, i):
        return max(line[:i]) < line[i] or max(line[i + 1 :]) < line[i]

    return traverse_forest_horizontal(data, get_visibility)


def get_left_score(line, i):
    for tree in line[i - 1 :: -1]:
        if tree >= line[i]:
            return list(line[i - 1 :: -1]).index(tree) + 1
    return i


def get_horizontal_score(data):
    def get_score(line, i):
        left_score = get_left_score(line, i)
        right_score = get_left_score(line[::-1], len(line) - i - 1)
        return left_score * right_score

    return traverse_forest_horizontal(data, get_score)


def part1(data):
    hor = get_horizontal_visibility(data)
    vert = get_horizontal_visibility(data.T)
    total = hor | vert.T

    perimeter = (len(data) - 1) * 4
    print("Visible trees:", total.sum() + perimeter)


def part2(data):
    hor = get_horizontal_score(data)
    vert = get_horizontal_score(data.T)
    total = hor * vert.T

    print("Max scenic tree:", total.max())


if __name__ == "__main__":
    data = get_input(day=8)
    data = np.array([list(map(int, list(d))) for d in data])
    part1(data)
    part2(data)
