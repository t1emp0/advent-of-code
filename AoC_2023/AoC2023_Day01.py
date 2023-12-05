# %%
example = """"""

from utils import get_input


def part1(data: list[str]):
    numbers = [[num for num in d if num.isnumeric()] for d in data]
    pairs = [int(f"{nums[0]}{nums[-1]}") for nums in numbers]
    print("Part1:", sum(pairs))


def get_numbers(data, number_names):
    digits = [[num for num in d if num.isnumeric()] for d in data]
    first_digits = [int(nums[0]) if nums else "" for nums in digits]
    idxs_first_spelled = [[d.find(num) for num in number_names] for d in data]

    first_numbers = []
    for digit, idx_spelled, d in zip(first_digits, idxs_first_spelled, data):
        try:
            idx_min_spelled = min([i for i in idx_spelled if i >= 0])
        except ValueError:
            idx_min_spelled = ""

        if idx_min_spelled == "" or (digit and d.find(str(digit)) < idx_min_spelled):
            first_numbers.append(digit)
        else:
            first_numbers.append(idx_spelled.index(idx_min_spelled) + 1)
    return first_numbers


def part2(data: list[str]):
    nums_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    first_numbers = get_numbers(data, nums_list)
    last_numbers = get_numbers(
        [d[::-1] for d in data], [key[::-1] for key in nums_list]
    )

    print("Part2:", sum([int(f"{f}{l}") for f, l in zip(first_numbers, last_numbers)]))


if __name__ == "__main__":
    data = get_input(day=1)
    # data = example.strip().splitlines()
    part1(data)
    part2(data)
