# %%
example1 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
example2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

# %%
from utils import get_input
import re


def part1(data):
    data = " ".join(data)
    muls = re.findall("mul\((\d{1,3}),(\d{1,3})\)", data)
    res = [int(x1) * int(x2) for x1, x2 in muls]
    print("Part1:", sum(res))


def part2(data):
    data = " ".join(data)
    res = 0
    enabled = True
    muls = re.findall("mul\((\d{1,3}),(\d{1,3})\)|(don't\(\))|(do\(\))", data)
    for x1, x2, dont, do in muls:
        if dont:
            enabled = False
            continue
        if do:
            enabled = True
            continue
        if enabled:
            res += int(x1) * int(x2)
    print("Part2:", res)


if __name__ == "__main__":
    data = get_input(day=3)
    data = example1.strip().splitlines()
    part1(data)
    data = example2.strip().splitlines()
    part2(data)

# %%
