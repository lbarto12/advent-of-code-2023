import math
from typing import List, Tuple, Set

with open('input.txt') as file:
    garden: List[List[chr]] = [list(i.strip()) for i in file.readlines()]


def merge_tuple(a: Tuple[int, int], b: Tuple[int, int]):
    return a[0] + b[0], a[1] + b[1]

def solve(_start: Tuple[int, int], max_steps: int):
    queue: List[Tuple[int, Tuple[int, int]]] = [(0, _start)]
    seen: Set[Tuple[int, int]] = set()
    w, h = len(garden[0]), len(garden)
    offset: int = max_steps % 2

    ans: int = 0
    while queue:
        steps, pos = queue.pop(0)

        if pos in seen:
            continue
        seen.add(pos)

        if steps % 2 == offset:
            ans += 1
        if steps == max_steps:
            continue

        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new = merge_tuple((x, y), pos)
            if 0 <= new[0] < w and 0 <= new[1] < h and garden[new[1]][new[0]] != '#':
                queue.append((steps + 1, new))

    return ans


# Part 1
start: Tuple[int, int] = (len(garden[0]) // 2, len(garden) // 2)

print(f'Part 1: {solve(start, 64)}')


# Part 2
def explore_all(_starts: List[Tuple[int, int]], _steps: int) -> int:
    return sum(solve(_start, _steps) for _start in _starts)


size: int = len(garden)
WIDTH: int = 26501365 // size - 1

full_tiles: int = ((WIDTH // 2 * 2 + 1) ** 2) * solve(start, size * 2 + 1) + \
             (((WIDTH + 1) // 2 * 2) ** 2) * solve(start, size * 2)
last_outer: int = explore_all([(start[0], size - 1), (start[0], 0), (size - 1, start[1]), (0, start[1])], size - 1)
small_corners: int = \
    (WIDTH + 1) * explore_all([(0, size - 1), (size - 1, size - 1), (0, 0), (size - 1, 0)], size // 2 - 1)
large_corners: int = \
    WIDTH * explore_all([(0, size - 1), (size - 1, size - 1), (0, 0), (size - 1, 0)], size * 3 // 2 - 1)

print(f"Part 2: {full_tiles + last_outer + small_corners + large_corners}")

