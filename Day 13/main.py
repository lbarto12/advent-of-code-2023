from typing import List

with open('input.txt') as file:
    maps: List[List[List[str]]] = [[list(i) for i in mp.split('\n')] for mp in file.read().split('\n\n')]


def array_diff(a: List[chr], b: List[chr]) -> int:
    return sum(i != j for i, j in zip(a, b))


def find_incidence(_map: List[List[str]]) -> int:
    n: int = len(_map)
    for i in range(1, len(_map)):
        slc: int = min(i, n - i)
        if _map[i - slc:i][::-1] == _map[i:i + slc]:
            return i
    return 0


def find_smudged_incidence(_map: List[List[str]]) -> int:
    for i in range(1, len(_map)):
        if sum(array_diff(a, b) for a, b in zip(_map[:i][::-1], _map[i:])) == 1:
            return i
    return 0


# Part 1
print(f'Part 1: {sum(find_incidence(mp) * 100 + find_incidence(list(zip(*mp))) for mp in maps)}')


# Part 2
print(f'Part 2 {sum(find_smudged_incidence(mp) * 100 + find_smudged_incidence(list(zip(*mp))) for mp in maps)}')



