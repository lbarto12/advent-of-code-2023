from typing import List, Dict, Tuple

with open('input.txt') as file:
    instructions: List[Tuple[chr, int, str]] = \
        [(a, int(b), c[1:-1]) for a, b, c in list(map(lambda i: tuple(i.strip().split()), file.readlines()))]


def merge_tuple(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    return a[0] + b[0], a[1] + b[1]

def calculate_area(_vertices: List[Tuple[int, int]]) -> float:
    return abs(sum(a * _vertices[i][1] - _vertices[i][0] * b for i, (a, b) in enumerate(_vertices, -1))) / 2

def solve(_instructions) -> int:
    vertices: List[Tuple[int, int]] = []
    pos: Tuple[int, int] = (0, 0)
    perimeter: int = 0
    for direction, distance, _ in _instructions:
        vertices.append(pos)
        perimeter += distance
        delta: Tuple[int, int] = \
            ((-1 if int(direction == 'L') else 1) * distance if direction in 'RL' else 0,
             (-1 if int(direction == 'U') else 1) * distance if direction in 'UD' else 0)
        pos = merge_tuple(pos, delta)

    return int(calculate_area(vertices) + perimeter // 2 + 1)


# Part1
print(f'Part 1: {solve(instructions)}')


# Part 2
cmd: Dict[chr, chr] = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
print(f'Part 2: {solve([(cmd[i[-1]], int(i[1:-1], 16), "") for _, _, i in instructions])}')

