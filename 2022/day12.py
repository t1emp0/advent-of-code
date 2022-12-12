from utils import get_input
from copy import deepcopy
from collections import defaultdict


def get_start_end(data):
    START_CHAR, END_CHAR = "S", "E"
    start = [(i, d.index(START_CHAR)) for i, d in enumerate(data) if START_CHAR in d][0]
    end = [(i, d.index(END_CHAR)) for i, d in enumerate(data) if END_CHAR in d][0]
    data[start[0]][start[1]] = "a"
    data[end[0]][end[1]] = "z"
    return start, end


def heuristic(start, end):
    return abs(end[0] - start[0]) + abs(end[1] - start[1])


def get_value(current: tuple, data: list):
    return ord(data[current[0]][current[1]])


def get_neighbors(current: tuple, data: list):
    valid_neighbors = []
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    val = get_value(current, data)
    for dir in dirs:
        neighbor = (current[0] + dir[0], current[1] + dir[1])
        if not (0 <= neighbor[0] < len(data) and 0 <= neighbor[1] < len(data[0])):
            continue
        n_val = get_value(neighbor, data)
        if n_val <= (val + 1):
            valid_neighbors.append(neighbor)
    return valid_neighbors


def reconstruct_path(cameFrom: dict, current: tuple):
    total_path = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.append(current)
    return total_path


def A_Star(start: tuple, goal: tuple, data) -> list:
    openSet = set()
    openSet.add(start)

    cameFrom = {}

    gScore = defaultdict(lambda: float("inf"))
    gScore[start] = 0

    fScore = defaultdict(lambda: float("inf"))
    fScore[start] = heuristic(start, goal)
    while openSet:
        localfScore = {k: v for k, v in fScore.items() if k in openSet}
        current = min(localfScore, key=localfScore.get)
        if current == goal:
            return reconstruct_path(cameFrom, current)

        openSet.remove(current)
        for neighbor in get_neighbors(current, data):
            tentative_gScore = gScore[current] + 1
            if tentative_gScore < gScore[neighbor]:
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = tentative_gScore + heuristic(neighbor, goal)
                if neighbor not in openSet:
                    openSet.add(neighbor)
    return []


def part1(data):
    start, end = get_start_end(data)
    path = A_Star(start, end, data)
    print("Starting path:", len(path) - 1)


def part2(data):
    _, end = get_start_end(data)

    starts = [
        (i, j)
        for i, d in enumerate(data)
        if "a" in d
        for j, c in enumerate(d)
        if c == "a"
    ]

    best_path = float("inf")
    for start in starts:
        # Small optimization made search x5 faster
        start_neighbors = [data[n[0]][n[1]] for n in get_neighbors(start, data)]
        if "b" not in start_neighbors:
            continue

        path = A_Star(start, end, data)
        if path:
            l = len(path) - 1
            if l < best_path:
                best_path = l

    print("Best_path:", best_path)


if __name__ == "__main__":
    data = get_input(day=12)
    data = [list(d) for d in data]
    part1(deepcopy(data))
    part2(deepcopy(data))
