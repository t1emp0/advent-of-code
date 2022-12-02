from utils import get_input


def parse_data(data):
    elves = []
    current = 0
    for cals in data:
        if cals:
            current += int(cals)
        else:
            elves.append(current)
            current = 0
    elves.append(current)
    return elves


def part1(elves):
    print("Max calories", max(elves))


def part2(elves):
    print("Top 3", sum(sorted(elves)[-3:]))


if __name__ == "__main__":
    data = get_input(day=1)
    elves = parse_data(data)
    part1(elves)
    part2(elves)
