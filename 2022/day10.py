from utils import get_input


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
