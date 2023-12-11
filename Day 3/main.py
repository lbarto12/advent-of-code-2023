from typing import Tuple, List

# Part 1
with open('input.txt') as file:
    engine_map = file.readlines()


def get_directions(x_offset: int, y_offset: int) -> Tuple[int, int]:
    for _y in range(-1, 2):
        for _x in range(-1, 2):
            yield _x + x_offset, _y + y_offset


valid_map: List[List[int]] = [[0 for _ in range(len(engine_map[0]))] for _ in range(len(engine_map))]
for i, row in enumerate(engine_map[1:-1]):
    for j, char in enumerate(row[1:-1]):
        if not (char == "." or char.isnumeric()):
            for x, y in get_directions(j + 1, i + 1):
                valid_map[y][x] = 1

current_number: str = '0'
num_valid: bool = False
sm: int = 0

for i, row in enumerate(engine_map):
    for j, char in enumerate(row):
        if char.isnumeric():
            num_valid = num_valid or valid_map[i][j]
            current_number += char
        else:
            if num_valid:
                sm += int(current_number)
            num_valid = False
            current_number = '0'

print(f'Part 1: {sm}')


# Part 2
def h_flood(_x: int, _y: int, m: int) -> str:
    if not engine_map[_y][_x].isnumeric():
        return ""
    flood: str = h_flood(_x + m, _y, m)
    return f'{flood if m < 0 else ""}{engine_map[_y][_x]}{flood if m > 0 else ""}'

def get_surrounding(__x: int, __y: int) -> List[int]:
    return list(map(int, filter(lambda _: _,
                                {h_flood(_x, _y, -1)[:-1] + h_flood(_x, _y, 1) for _x, _y in get_directions(__x, __y) if
                                 engine_map[_y][_x] != '*'})))


total: int = 0
for i, row in enumerate(engine_map):
    for j, char in enumerate(row):
        if char == '*':
            if len(nums := get_surrounding(j, i)) == 2:
                total += nums[0] * nums[1]

print(f'Part 2: {total}')



