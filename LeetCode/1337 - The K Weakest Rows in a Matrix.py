# Leetcode problems

# 1337. The K Weakest Rows in a Matrix
# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
# Easy

# %%
from typing import List

Matrix = List[List[int]]


def kWeakestRows(mat: Matrix, k: int) -> List[int]:
    soldiers = [sum(row) for row in mat]
    civilians = [len(mat[0]) - soldier for soldier in soldiers]
    full_list = enumerate(zip(soldiers, civilians))
    civ_sorted = sorted(full_list, key=lambda x: x[1][1])
    sold_sorted = sorted(civ_sorted, key=lambda x: x[1][0])
    return [i[0] for i in sold_sorted][:k]


# %%
tests = [
    (
        [
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1],
        ],
        3,
    ),
    ([[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]], 2,),
]

for (mat, k) in tests:
    print(kWeakestRows(mat, k))
# expected = [[2,0,3], [0,2]]

