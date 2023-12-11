import math
from typing import List, Tuple, Dict


with open('input.txt') as file:
    floor: List[chr] = [list(i)[:-1] for i in file.readlines()]
    pos: Tuple[int, int]
    for i, row in enumerate(floor):
        if (idx := row.index('S') if 'S' in row else -1) != -1:
            pos = (idx, i)
            break
    start = pos[:]

class Junction:
    def __init__(self, char: chr):
        self.char: chr = char
        self.connections: Dict[Tuple, bool] = {
            (0, 1): char in '|LJS', (0, -1): char in '|F7S',
            (1, 0): char in '-J7S', (-1, 0): char in '-FLS',
        }

    def can_connect(self, junc, from_dir: Tuple[int, int]) -> bool:
        return self.connections[from_dir] and junc.connections[-from_dir[0], -from_dir[1]]


# Part 1
directions: List[Tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]
path: List[Tuple[int, int]] = [pos]
steps: int = 0

while True:
    junction: Junction = Junction(floor[pos[1]][pos[0]])
    for direction in directions:
        new_pos: Tuple[int, int] = pos[0] + direction[0], pos[1] + direction[1]
        if (0 <= new_pos[0] < (len(floor[0])) and 0 <= new_pos[1] < (len(floor))) and \
                Junction(floor[new_pos[1]][new_pos[0]]).can_connect(junction, direction) and new_pos not in path:
            path.append(new_pos)
            pos, steps = new_pos, steps + 1
            break
    else:
        break

print(f'Part 1: {math.ceil(steps / 2)}')


# Part 2
def calculate_area(coordinates: List[Tuple[int, int]]) -> float:
    return abs(
        sum(a * coordinates[i - 1][1] - coordinates[i - 1][0] * b for i, (a, b) in enumerate(coordinates))
    ) / 2


print(f'Part 2: {int(calculate_area(path) - len(path) / 2 + 1)}')
