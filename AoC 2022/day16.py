# %%
example = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""

#%%
from utils import get_input
import numpy as np


def parse_input(data):
    data = [d.split(" ") for d in data]
    valves = {
        d[1]: (
            int(d[4].split("=")[1].split(";")[0]),
            [v.split(",")[0] for v in d[9:]],
        )
        for d in data
    }
    return valves


def build_adjacency(valves):
    valve_names = list(valves.keys())
    valve_index = {v_name: v_index for v_index, v_name in enumerate(valve_names)}
    # print(valve_names)
    mat = np.zeros((len(valve_names), len(valve_names)), dtype=np.uint32)

    current_valve = valve_names[0]
    explored = set()
    explored.add(current_valve)
    pending = [current_valve]

    while pending:
        current_valve = pending.pop()
        for neighbour in valves[current_valve][1]:
            mat[valve_index[current_valve]][valve_index[neighbour]] = 1
            if neighbour not in explored:
                explored.add(neighbour)
                pending.append(neighbour)

    print(mat)

    res = mat.copy()
    dist = mat.copy()
    for i in range(len(valve_index))[:1]:
        res = mat @ res

        updated = res.copy()
        updated[dist != 0] = 0
        dist = dist + updated
        print()
        print(dist)

        # print(dist)


def get_next_valve(valves, current_valve, remaining_time, useful_valves):

    explored = set(current_valve)
    pending = [current_valve]
    best_valve = ("_", 0)

    while remaining_time > 0 and pending:
        current_valve = pending.pop()
        for neighbour in valves[current_valve][1]:
            if neighbour not in explored:
                explored.add(neighbour)
                pressure = valves[neighbour][0] * (remaining_time - 2)
                if pressure > best_valve[1] and neighbour in useful_valves:
                    best_valve = (neighbour, pressure)
                pending.append(neighbour)
        remaining_time -= 2

    return best_valve


def part1(valves):
    # print(valves)
    AVAILABLE_TIME = 30
    # build_adjacency(valves)

    useful_valves = set(
        [valve for valve, pressure in valves.items() if pressure[0] > 0]
    )
    print(len(useful_valves))
    return

    released_pressure = 0
    remaining_time = AVAILABLE_TIME

    opened_valves = []
    current_valve = "AA"
    while remaining_time and useful_valves:
        next_valve, pressure = get_next_valve(
            valves, current_valve, remaining_time, useful_valves
        )
        released_pressure += pressure
        current_valve = next_valve

        useful_valves.remove(next_valve)
        opened_valves.append(next_valve)
        remaining_time -= 2

    print(opened_valves)
    print(released_pressure)

    print("Part1:")


def part2(data):
    print("Part2:")


if __name__ == "__main__":
    data = get_input(day=16)
    # data = example.strip().splitlines()
    valves = parse_input(data)
    part1(valves)
    # part2(valves)

# %%
