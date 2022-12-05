from utils import get_input


def part1(data):
    solve(data, reverse=True)


def part2(data):
    solve(data, reverse=False)


def solve(data, reverse):
    data = data.split("\n")
    blank_row = data.index("")
    cols_n = int((len(data[1]) + 1) / 4)

    # there are at max 9 cols, we can use this parse
    rows = [[d[c * 4 + 1] for c in range(cols_n)] for d in data[: blank_row - 1]]
    stacks = zip(*reversed(rows))
    stacks = [[s for s in stack if s != " "] for stack in stacks]

    moves = [move.split(" ") for move in data[blank_row + 1 : -1]]
    moves = [map(int, (m[1], m[3], m[5])) for m in moves]

    for (n, start_col, end_col) in moves:
        crates = stacks[start_col - 1][-n:]
        stacks[start_col - 1] = stacks[start_col - 1][:-n]
        stacks[end_col - 1] += reversed(crates) if reverse else crates

    print(f"Top stacks ({reverse=}):", "".join([s[-1] for s in stacks]))


if __name__ == "__main__":
    data = get_input(day=5, splitlines=False, strip=False)
    part1(data)
    part2(data)
