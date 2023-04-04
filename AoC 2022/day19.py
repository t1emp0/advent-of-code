# %%
example = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
"""


#%%
from utils import get_input
import numpy as np

MAX_TIME = 24


def parse_input(data: list[str]):
    blueprints = [
        [int(word) for word in d.split(" ") if word.isnumeric()] for d in data
    ]
    blueprints = np.array(
        [
            ((b[0], 0, 0, 0), (b[1], 0, 0, 0), (b[2], b[3], 0, 0), (b[4], 0, b[5], 0))
            for b in blueprints
        ]
    )
    return blueprints


#%%
def simulate(time_left, costs, robots, resources):
    print("TL", time_left)
    for time in range(time_left, 0, -1):
        if time <= 20:
            break

        time_past = MAX_TIME - time + 1
        resources += robots
        print(time)
        print(time_left, "T:", time_past)
        print("Rob:", robots)
        print("Res:", resources)

        for i, robot_cost in enumerate(costs):
            # print(robot_cost, resources)
            if (robot_cost <= resources).all():
                new_resources = resources.copy()
                new_resources += robots
                new_resources -= robot_cost
                new_robots = robots.copy()
                new_robots[i] += 1
                print(time + 1)
                print(time - 1, "T:", 2)
                print("Rob:", new_robots)
                print("Res:", new_resources)
                simulate(time - 1, costs, new_robots, new_resources)


# part1(blueprints)
#%%
def part1(blueprints):

    for costs in blueprints[:1]:
        robots = np.array([1, 0, 0, 0])
        resources = np.array([0, 0, 0, 0])
        simulate(MAX_TIME, costs, robots, resources)
    print("Part1:")


def part2(data):
    print("Part2:")


if __name__ == "__main__":
    data = get_input(day=19)
    data = example.strip().splitlines()
    blueprints = parse_input(data)
    part1(blueprints)
    part2(data)
# %%
