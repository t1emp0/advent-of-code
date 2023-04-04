# %%
example = """1
2
-3
3
-2
0
4
"""

#%%
from utils import get_input
import numpy as np


def part1(data):
    COORD_POS = [1000, 2000, 3000]

    nums = list(map(int, data))
    offset = np.zeros((len(nums),), dtype=np.int8)
    # print(nums)
    # print(offset)

    for num in range(len(nums)):
        start = (num + offset[num]) % (len(nums) - 1)
        end = (start + nums[start]) % (len(nums) - 1)
        if end == 0:
            end = len(nums)
        if end > start - offset[num]:
            offset[start : end + 1] -= 1
        elif end < start - offset[num]:
            offset[start : end + 1] += 1
        # print(num, ":", nums[start], "\t::", start, "->", end, "|", offset[num])
        nums.insert(end, nums.pop(start))
        # print(nums)
        # print(offset)
        # print()

    zero_pos = nums.index(0)
    coords = [nums[(pos + zero_pos) % len(nums)] for pos in COORD_POS]

    print("Part1:", coords, sum(coords))
    # high 6879, 7052


def part2(data):
    print("Part2:")


if __name__ == "__main__":
    data = get_input(day=20)
    # data = example.strip().splitlines()
    part1(data)
    part2(data)

# %%
