from utils import get_input
import numpy as np
from copy import deepcopy


def parse_data(data: list[str] | str):
    data = [d.strip() for d in data]
    monkeys = []
    monkey = {}
    for d in data:
        if not d:
            monkeys.append(monkey)
            monkey = {}
        else:
            colon = d.index(":")
            if d.startswith("Starting items"):
                monkey["items"] = d[colon + 2 :].split(", ")
            elif d.startswith("Operation"):
                monkey["operation"] = d[colon + 2 + 6 :]
            elif not d.startswith("Monkey"):
                monkey[d[:colon].split(" ")[-1].lower()] = int(d.split(" ")[-1])
    monkeys.append(monkey)

    return monkeys


def simulate_monkeys(monkeys: list[dict], n_rounds: int, part: int):
    tracker = [0] * len(monkeys)
    mcm = np.prod([m["test"] for m in monkeys])

    for _ in range(n_rounds):
        for idx, monkey in enumerate(monkeys):
            for i in monkey["items"]:
                new = eval(monkey["operation"].replace("old", str(i)))
                if part == 1:
                    new = new // 3
                if part == 2 and new > mcm:
                    new = new % mcm
                test = new % monkey["test"] == 0
                to = monkey[str(test).lower()]
                monkeys[to]["items"].append(new)

            tracker[idx] += len(monkey["items"])
            monkey["items"] = []

    maxs = sorted(tracker)[-2:]
    print(f"Part {part}:", maxs[0] * maxs[1])


def part1(monkeys):
    N_ROUNDS = 20
    simulate_monkeys(monkeys, N_ROUNDS, 1)


def part2(monkeys):
    N_ROUNDS = 10_000
    simulate_monkeys(monkeys, N_ROUNDS, 2)


if __name__ == "__main__":
    data = get_input(day=11)
    monkeys = parse_data(data)
    part1(deepcopy(monkeys))
    part2(deepcopy(monkeys))
