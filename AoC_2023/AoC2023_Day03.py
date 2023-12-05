from utils import get_input
from collections import defaultdict

example = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def parse_input(data: list[str]) -> tuple:
    numbers = []
    symbols = []
    for row, line in enumerate(data):
        current_num = ""
        for col, char in enumerate(line):
            if char.isnumeric():
                if not current_num:
                    num_start = col
                current_num += char
            else:
                if current_num:
                    numbers.append((int(current_num), row, num_start, col - 1))
                    current_num = ""
                if char != ".":
                    symbols.append((char, row, col))
        if current_num:
            numbers.append((int(current_num), row, num_start, col - 1))
    return (symbols, numbers)


def part1(symbols: list, numbers: list) -> list:
    valid = []
    relation = []
    for num, n_row, n_start, n_end in numbers:
        near_symbols = [
            (s, s_row, s_col)
            for s, s_row, s_col in symbols
            if (abs(n_row - s_row) <= 1 and (n_start - 1 <= s_col <= n_end + 1))
        ]
        if near_symbols:
            valid.append(num)
            relation.append((num, near_symbols))

    print("Part1:", sum(valid))
    return relation


def part2(relation) -> None:
    possible_gears = defaultdict(list)
    for num, near_symbols in relation:
        for symbol in near_symbols:
            if symbol[0] == "*":
                possible_gears[symbol].append(num)

    gears = [nums[0] * nums[1] for _, nums in possible_gears.items() if len(nums) == 2]
    print("Part2:", sum(gears))


if __name__ == "__main__":
    data = get_input(day=3)
    data = example.strip().splitlines()
    symbols, numbers = parse_input(data)
    relation = part1(symbols, numbers)
    part2(relation)
