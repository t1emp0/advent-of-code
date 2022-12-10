from utils import get_input
from functools import reduce


def part1(ops):
    strength, reg = 0, 1

    for cycle, instr in enumerate(ops):
        if cycle in range(19, 220, 40):
            strength += (cycle + 1) * reg
        reg += instr

    print("Total strength:", strength)


def part1_oneliner_compact(ops):
    print(reduce(lambda o,n:(o[0]+((n[0]+1)*o[1]if n[0]in range(19,220,40)else 0),o[1]+n[1]),enumerate(ops),(0,1))[0])


def part1_oneliner(ops):
    print("Total strength:", reduce(lambda old, new: (old[0]+ ((new[0] + 1) * old[1] if new[0] in range(19, 220, 40) else 0), old[1] + new[1]), enumerate(ops), (0, 1))[0])


def part1_oneliner_expanded(ops):
    # old = (strength, reg)
    # new = (cycle-1, instr)
    strength = reduce(
        lambda old, new: (
            old[0] + ((new[0] + 1) * old[1] if new[0] in range(19, 220, 40) else 0),
            old[1] + new[1],
        ),
        enumerate(ops),
        (0, 1),
    )[0]

    print("Total strength:", strength)


def part2(ops):
    reg = 1
    screen, line = [], ""

    for cycle, instr in enumerate(ops):
        line += "#" if abs((cycle) % 40 - reg) < 2 else "."
        if (cycle + 1) % 40 == 0:
            screen.append(line)
            line = ""
        reg += instr

    with open("day10_output.txt", "w") as f:
        f.writelines("\n".join(screen))
    print("Part 2: Output written")


if __name__ == "__main__":
    data = get_input(day=10)

    # Adjust operations, so that addx takes 2 cycles and noop adds 0 to reg
    ops_oneliner = sum(
        [[0] + [int(d.split(" ")[1])] if len(d.split(" ")) == 2 else [0] for d in data],
        [],
    )

    part1(ops_oneliner)
    part2(ops_oneliner)

    part1_oneliner_compact(ops_oneliner)
    part1_oneliner(ops_oneliner)
    part1_oneliner_expanded(ops_oneliner)
