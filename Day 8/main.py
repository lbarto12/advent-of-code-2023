import math
import re
from typing import Dict, Tuple

with open('input.txt') as file:
    instructions, _, *_paths = file.readlines()
    paths: Dict[str, Tuple] = {}
    for line in _paths:
        key, _val = re.match(r'(\w+) = \((.+)\)', line).groups()
        val: Tuple = tuple(_val.split(', '))
        paths[key] = val


# Part 1
idx: int = 0
steps: int = 1
current: str = 'AAA'
path_converter: Dict[str, int] = {'L': 0, 'R': 1}
n: int = len(instructions)

while (current := paths[current][path_converter.get(instructions[idx])]) != 'ZZZ':
    idx += 1
    if idx >= n - 1:
        idx = 0
    steps += 1

print(f'Part 1: {steps}')


# Part 2
idx: int = 0
keys = [i for i in paths if i.endswith('A')]
required_steps = []

for position in keys:
    steps: int = 0
    while not position.endswith('Z'):
        position = paths[position][path_converter.get(instructions[idx])]
        idx += 1
        if idx >= n - 1:
            idx = 0
        steps += 1
    required_steps.append(steps)

print(f'Part 2: {math.lcm(*required_steps)}')

