from utils import get_input


def find_marker(data, marker_length):
    for c in range(len(data)):
        if c < marker_length - 1:
            continue
        four = data[c - marker_length : c]
        if len(set(four)) == marker_length:
            print(f"{marker_length=}:", c)
            return


def part1(data):
    find_marker(data, 4)


def part2(data):
    find_marker(data, 14)


if __name__ == "__main__":
    data = get_input(day=6, splitlines=False)
    part1(data)
    part2(data)
