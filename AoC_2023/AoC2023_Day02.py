# %%
example = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

from utils import get_input
from functools import reduce


def part1and2(data):
    bag_items = {"red": 12, "green": 13, "blue": 14}

    games = []
    for game in data:
        subsets = game.split(":")[1].replace(";", ",").split(",")
        subsets = [s.strip().split(" ") for s in subsets]
        subsets.sort(key=lambda x: int(x[0]))
        results = {color: int(number) for number, color in subsets}
        games.append(results)

    valid_ids = []
    for idx, game in enumerate(games):
        if all([game[color] <= bag_items[color] for color in game]):
            valid_ids.append(idx + 1)

    print("Part1:", sum(valid_ids))
    print("Part2:", sum([reduce(lambda x, y: x * y, game.values()) for game in games]))


if __name__ == "__main__":
    data = get_input(day=2)
    # data = example.strip().splitlines()
    part1and2(data)
