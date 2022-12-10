from utils import get_input
from functools import reduce


def part1(ops):
    cycle, reg = 0, 1
    strength = 0

    for instr in ops:
        for _ in range(1 if instr[0] == "noop" else 2):
            cycle += 1
            if cycle % 40 != 0 and cycle % 20 == 0:
                strength += cycle * reg
        reg += int(instr[1]) if len(instr) > 1 else 0

    print("Total strength:", strength)


def part1_oneliner(ops):
    print("Total strength:", reduce(lambda old, new: (old[0]+ ((new[0] + 1) * old[1] if (new[0] + 1) % 40 != 0 and (new[0] + 1) % 20 == 0 else 0), old[1] + new[1]), enumerate(ops), (0, 1))[0])


def part1_oneliner_expanded(ops):
    # old = (strength, reg)
    # new = (cycle-1, instr)
    strength = reduce(
        lambda old, new: (
            old[0]
            + (
                (new[0] + 1) * old[1]
                if (new[0] + 1) % 40 != 0 and (new[0] + 1) % 20 == 0
                else 0
            ),
            old[1] + new[1],
        ),
        enumerate(ops),
        (0, 1),
    )[0]

    print("Total strength:", strength)


def part2(ops):
    cycle, reg = 0, 1
    screen, line = [], ""

    for instr in ops:
        for _ in range(1 if instr[0] == "noop" else 2):
            cycle += 1
            line += "#" if abs((cycle - 1) % 40 - reg) < 2 else "."
            if cycle % 40 == 0:
                screen.append(line)
                line = ""
        reg += int(instr[1]) if len(instr) > 1 else 0

    with open("day10_output.txt", "w") as f:
        f.writelines("\n".join(screen))
    print("Output written")


if __name__ == "__main__":
    data = get_input(day=10)
    ops = [d.split(" ") for d in data]
    part1(ops)
    part2(ops)

    ops_oneliner = sum([[0] + [int(d.split(" ")[1])] if len(d.split(" ")) == 2 else [0] for d in data], [])
    part1_oneliner(ops_oneliner)
