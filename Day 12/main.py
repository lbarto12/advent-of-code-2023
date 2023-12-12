import re
from typing import List, Tuple
from functools import cache

with open('input.txt') as file:
    springs: List[Tuple[str, List[int]]] = []
    for i in file.readlines():
        a, b = i.split(' ')
        springs.append((a, list(map(int, b.split(',')))))


@cache
def num_possible(_line: str, *patterns: re.Pattern) -> int:
    if len(patterns) == 0:
        return int("#" not in _line)
    matches = idx = 0
    while (match := patterns[0].search(_line[idx:])) and "#" not in _line[:idx + match.start()]:
        matches += num_possible(_line[idx + match.end() - 1:], *patterns[1:])
        idx += match.start() + 1
    return matches


sm: int = 0
for line, record in springs:
    sm += num_possible(f'.{line}.', *[re.compile(f"[.?][#?]{{{i}}}[.?]") for i in record])

print(f'Part 1: {sm}')


# Part 2
unfolded: List[Tuple[str, List[int]]] = [('?'.join([line] * 5), record * 5) for line, record in springs]
sm: int = 0
for line, record in unfolded:
    sm += num_possible(f".{line}.", *[re.compile(f"[.?][#?]{{{i}}}[.?]") for i in record])

print(f'Part 2: {sm}')



