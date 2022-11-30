# Leetcode problems

# 827. Making a large island
# https://leetcode.com/problems/making-a-large-island/
# Hard

#%%
from typing import List, Tuple, Dict

Island = List[List]
Coord = Tuple[int, int]
Component = List[Coord]


def largestIsland(grid: Island) -> int:
    print_matrix(grid)

    components = create_components(grid)
    # print(components)

    (counted_grid, counted_dict) = count_components(len(grid), components)
    # print_matrix(counted_grid)

    max_island = get_max_island(counted_grid, counted_dict)
    # print()
    print(max_island)
    return max_island


def create_components(g: Island) -> List[Component]:
    n = len(g)
    visited = []
    [visited.append([False] * n) for _ in range(n)]
    queue = []

    components = []

    for i in range(n):
        for j in range(n):
            current_component = []
            # Skip nodes if already visited or are water
            if visited[i][j] or not g[i][j]:
                continue

            queue.append((i, j))
            visited[i][j] = True
            while queue:
                (s1, s2) = queue.pop(0)
                current_component.append((s1, s2))

                for (n1, n2) in get_neighbours(n, s1, s2):
                    if visited[n1][n2] or not g[n1][n2]:
                        continue

                    visited[n1][n2] = True
                    queue.append((n1, n2))

            components.append(current_component)
    return components


def count_components(
    n: int, components: List[Component]
) -> Tuple[List[List[int]], Dict[int, int]]:
    merged_dict = {j: idx + 1 for (idx, comp) in enumerate(components) for j in comp}
    components_size = {idx + 1: len(comp) for (idx, comp) in enumerate(components)}

    counted_grid = []
    for i in range(n):
        counted_grid.append(
            [
                merged_dict[(i, j)] if (i, j) in merged_dict.keys() else 0
                for j in range(n)
            ]
        )
    return (counted_grid, components_size)


def get_max_island(counted_grid: Island, components_size: Dict[int, int]) -> int:
    """
    Calculates the max possible island by iterating through the water spaces
    """
    n = len(counted_grid)
    max_island = 0
    max_pos = None
    for i in range(n):
        for j in range(n):
            if counted_grid[i][j] > 0:
                continue
            neighbours = get_neighbours(n, i, j)
            components = set([counted_grid[x][y] for (x, y) in neighbours])
            island_counts = [components_size[comp] for comp in components if comp != 0]
            max_island = max(sum(island_counts), max_island)
            if sum(island_counts) == max_island:
                max_pos = (i, j)

    if max_pos:
        counted_grid[max_pos[0]][max_pos[1]] = "X"
    else:
        return n * n
    print()
    print_matrix(counted_grid)
    return max_island + 1


def get_neighbours(n: int, i: int, j: int):
    N = (i - 1, j) if i - 1 >= 0 else None
    E = (i, j + 1) if j + 1 < n else None
    S = (i + 1, j) if i + 1 < n else None
    W = (i, j - 1) if j - 1 >= 0 else None
    return set([i for i in (N, E, S, W) if i != None])


def print_matrix(matrix: List[List]):
    [print(str(i)) for i in matrix]


# %%
test = [
    [[1, 0], [0, 1]],
    [[1, 1], [1, 0]],
    [[1, 1], [1, 1]],
    [[0, 1, 1, 1], [1, 0, 0, 0], [0, 1, 0, 1], [0, 0, 1, 1]],
]

for t in test:
    print("-" * 10)
    largestIsland(t)
