import re

# Part 1
with open('input.txt') as file:
    finals = []
    for code in file.readlines():
        nums = ''.join([i for i in code if i.isnumeric()])
        finals.append(int(nums[0] + nums[-1]))
    print(f'Part 1: {sum(finals)}')


# Part 2
with open('input.txt') as file:
    possible = {
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
    finals = []
    for code in file.readlines():
        all_nums = re.findall('(?=(' + '|'.join(list(possible) + list(str(i) for i in range(1, 10))) + '))', code)
        adjusted = [possible.get(i, i) for i in all_nums]
        finals.append(int(adjusted[0] + adjusted[-1]))
    print(f'Part 2: {sum(finals)}')

