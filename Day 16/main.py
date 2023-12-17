import sys
from typing import List, Tuple, Set, Dict, Callable

with open('input.txt') as file:
    grid: List[List[chr]] = [list(i.strip()) for i in file.readlines()]


interact: Dict[chr, Callable] = {
    '.': lambda d: [d],
    '\\': lambda d: [(d[::-1])],
    '/': lambda d: [(-d[1], -d[0])],
    '|': lambda d: [(0, 1), (0, -1)] if d[0] else [d],
    '-': lambda d: [(1, 0), (-1, 0)] if d[1] else [d],
}

def merge_tuple(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    return a[0] + b[0], a[1] + b[1]


# NOTE: this is kind of slow and manually setting the recursion limit is dangerous.
# NOTE: Should probably swap for some form of iterative method. Or just find a better solution.
def charge(_charged: Set[Tuple[Tuple[int, int], Tuple[int, int]]], _delta: Tuple[int, int], _pos: Tuple[int, int]):
    if (_delta, _pos) in _charged or not (0 <= _pos[0] < len(grid) and 0 <= _pos[1] < len(grid[0])):
        return
    _charged.add((_delta, _pos))

    move: List[Tuple[int, int]] = interact[grid[_pos[1]][_pos[0]]](_delta)

    for delt in move:
        charge(_charged, delt, merge_tuple(_pos, delt))


def simulate(start: Tuple[int, int], delta: Tuple[int, int]) -> int:
    charged: Set[Tuple[Tuple[int, int], Tuple[int, int]]] = set()
    charge(charged, delta, start)
    return len(set([i[1] for i in charged]))


# Part 1:
sys.setrecursionlimit(5000)
print(f'Part 1: {simulate((0, 0), (1, 0))}')


# Part 2:
mx: int = max(
    max(simulate((i, 0), (0, 1)) for i in range(len(grid[0]))),
    max(simulate((i, len(grid) - 1), (0, -1)) for i in range(len(grid[0]))),
    max(simulate((0, i), (1, 0)) for i in range(len(grid))),
    max(simulate((len(grid[0]) - 1, i), (-1, 0)) for i in range(len(grid)))
)

print(f'Part 2: {mx}')



