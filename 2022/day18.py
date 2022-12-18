from utils import get_input
import numpy as np

neighbours = np.array(
    [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
)


def part1(cubes):
    meeting_faces = 0
    axis_cycles = [(0, 1, 2), (2, 0, 1), (1, 2, 0)]

    # Sort by plane and then compare connected cubes
    for ax1, ax2, ax3 in axis_cycles:
        cubes = cubes[cubes[:, ax3].argsort()]
        cubes = cubes[cubes[:, ax2].argsort(kind="mergesort")]
        cubes = cubes[cubes[:, ax1].argsort(kind="mergesort")]

        for c in range(1, len(cubes)):
            this, prev = cubes[c], cubes[c - 1]
            if (
                this[ax1] == prev[ax1]
                and this[ax2] == prev[ax2]
                and this[ax3] - prev[ax3] == 1
            ):
                meeting_faces += 1

    total_surface_area = len(cubes) * 6 - meeting_faces * 2
    return total_surface_area


def part2(cubes):
    max_x, max_y, max_z = cubes.max(axis=0)
    cubes_set = set([(c[0], c[1], c[2]) for c in cubes])

    air_cubes = set(
        [
            (x, y, z)
            for x in range(1, max_x)
            for y in range(1, max_y)
            for z in range(1, max_z)
            if (x, y, z) not in cubes_set
        ]
    )

    previous_interior_len = 0
    stable_interior = False

    while not stable_interior:
        for cube in set(air_cubes):
            for neighbour in list(map(tuple, neighbours + np.array(cube))):
                if neighbour not in cubes_set and neighbour not in air_cubes:
                    air_cubes.remove(cube)
                    break

        stable_interior = previous_interior_len == len(air_cubes)
        previous_interior_len = len(air_cubes)

    interior_surface_area = part1(np.array(list(air_cubes)))
    return interior_surface_area


if __name__ == "__main__":
    data = get_input(day=18)
    cubes = np.array([list(map(int, d.split(","))) for d in data])

    total_surface_area = part1(cubes)
    print("Total surface area:", "\t", total_surface_area)

    interior_surface_area = part2(cubes)
    print("Interior surface area:", "\t", interior_surface_area)

    exterior_surface_area = total_surface_area - interior_surface_area
    print("Exterior surface area:", "\t", exterior_surface_area)
