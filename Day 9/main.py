from typing import List


with open('input.txt') as file:
    data: List[List[int]] = [[int(num) for num in line.split()] for line in file.readlines()]


def extrapolate(seq: List[int], idx: int, direction: int) -> int:
    diffs: List[int] = [seq[i + 1] - num for i, num in enumerate(seq[:-1])]
    return 0 if all(diff == 0 for diff in seq) else seq[idx] + direction * extrapolate(diffs, idx, direction)


print(f'Part 1: {sum(map(lambda i: extrapolate(i, idx=-1, direction=1), data))}')
print(f'Part 2: {sum(map(lambda i: extrapolate(i, idx=0, direction=-1), data))}')

