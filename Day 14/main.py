from typing import List

with open('input.txt') as file:
    dish: List[List[chr]] = [list(filter(lambda x: x != '\n', [*i])) for i in file.readlines()]


# Overkill
def tilt(_dish: List[List[chr]], direction: str) -> None:
    if direction == 'N':
        for i in range(1, len(_dish)):
            for slot, tile in enumerate(_dish[i]):
                if tile == 'O':
                    j = i - 1
                    while j >= 0 and _dish[j][slot] not in '#O':
                        _dish[j][slot], _dish[j + 1][slot] = 'O', '.'
                        j -= 1
    if direction == 'S':
        for i in range(len(_dish) - 1, -1, -1):
            for slot, tile in enumerate(_dish[i]):
                if tile == 'O':
                    j = i + 1
                    while j < len(_dish) and _dish[j][slot] not in '#O':
                        _dish[j][slot], _dish[j - 1][slot] = 'O', '.'
                        j += 1
    if direction == 'W':
        for i in range(1, len(_dish[0])):
            for slot in range(len(_dish)):
                if _dish[slot][i] == 'O':
                    j = i - 1
                    while j >= 0 and _dish[slot][j] not in '#O':
                        _dish[slot][j], _dish[slot][j + 1] = 'O', '.'
                        j -= 1
    if direction == 'E':
        for i in range(len(_dish[0]) - 1, -1, -1):
            for slot in range(len(_dish)):
                if _dish[slot][i] == 'O':
                    j = i + 1
                    while j < len(_dish[0]) and _dish[slot][j] not in '#O':
                        _dish[slot][j], _dish[slot][j - 1] = 'O', '.'
                        j += 1


# Part 1
p1_dish: List[List[chr]] = [i[:] for i in dish]

tilt(p1_dish, 'N')

ans: int = 0
n = len(p1_dish)
for i, level in enumerate(p1_dish):
    ans += (n - i) * level.count('O')

print(f'Part 1: {ans}')


# Part 2:
p2_dish: List[List[chr]] = [i[:] for i in dish]
remaining = 0
seen = []
for i in range(1000000000):
    dx = ''.join(''.join(i for i in line) for line in p2_dish)
    if dx in seen:
        cycle_start: int = seen.index(dx)
        cycle_length = i - cycle_start
        for _ in range((1000000000 - cycle_start) % cycle_length):
            for dr in ['N', 'W', 'S', 'E']:
                tilt(p2_dish, dr)
        break
    for dr in ['N', 'W', 'S', 'E']:
        tilt(p2_dish, dr)
    seen.append(dx)




ans: int = 0
n = len(p2_dish)
for i, level in enumerate(p2_dish):
    ans += (n - i) * level.count('O')


print(f'Part 2 {ans}')


