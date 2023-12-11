import re
from typing import List, Dict

with open('input.txt') as file:
    calibration: List[str] = file.readlines()

# Part 1
finals: List[int] = []
for code in calibration:
    nums: str = ''.join([i for i in code if i.isnumeric()])
    finals.append(int(nums[0] + nums[-1]))

print(f'Part 1: {sum(finals)}')


# Part 2
possible: Dict[str, str] = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}
finals: List[int] = []
for code in calibration:
    adjusted: List[str] = [possible.get(i, i) for i in re.findall('(?=(' + '|'.join(list(possible)) + r'|\d))', code)]
    finals.append(int(adjusted[0] + adjusted[-1]))

print(f'Part 2: {sum(finals)}')

