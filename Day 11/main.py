import sys
from typing import List, Tuple


with open('input.txt') as file:
    galaxies: List[List[chr]] = [list(filter(lambda x: x != "\n", [j for j in i])) for i in file.readlines()]

    for i in range(len(galaxies)):
        if all(c == '.' for c in galaxies[i]):
            galaxies[i] = ['E'] * len(galaxies[0])

    for i in range(len(galaxies[0])):
        if all(galaxies[j][i] in '.E' for j in range(len(galaxies))):
            for j in range(len(galaxies)):
                galaxies[j][i] = 'E'


def min_path(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def after_expansion(coord: Tuple[int, int], expansion: int) -> Tuple[int, int]:
    x, y = coord
    n = len(galaxies)
    ex: int = galaxies[y][:x].count('E')
    ey: int = [galaxies[i][x] for i in range(n - (n - y))].count('E')
    return x + ex * (expansion - 1), y + ey * (expansion - 1)


# Part 1:
coords: List[Tuple[int, int]] = \
    [after_expansion((x, y), 2) for y, row in enumerate(galaxies) for x, val in enumerate(row) if val == '#']
print(f'Part 1: {sum(min_path(c1, c2) for i, c1 in enumerate(coords) for c2 in coords[i + 1:])}')


# Part 2:
coords: List[Tuple[int, int]] = \
    [after_expansion((x, y), 1_000_000) for y, row in enumerate(galaxies) for x, val in enumerate(row) if val == '#']
print(f'Part 2: {sum(min_path(c1, c2) for i, c1 in enumerate(coords) for c2 in coords[i + 1:])}')





