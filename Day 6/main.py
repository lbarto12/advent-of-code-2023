from typing import List, Tuple


with open('input.txt') as file:
    raw_records: List[str] = file.readlines()
    records: List[Tuple[int, int]] = list(zip(*[[int(n) for n in i.split()[1:]] for i in raw_records]))


def quadratic(b, c):
    return (-b + (b ** 2 - 4 * c) ** 0.5) / 2, (-b - (b ** 2 - 4 * c) ** 0.5) / 2


# Part 1
count: int = 1
for time, distance in records:
    a, b = quadratic(time, distance)
    count *= abs(int(a + 1) if a.is_integer() else int(a) - int(b))

print(f'Part 1: {count}')


# Part 2
a, b = quadratic(*[int(''.join(i.split()[1:])) for i in raw_records])
print(f"Part 2: {abs(int(a + 1) if a.is_integer() else int(a) - int(b))}")


