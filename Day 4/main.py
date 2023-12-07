import re

with open('input.txt') as file:
    cards = file.readlines()

def calculate_card(_card: str) -> int:
    winning, nums = ({int(n) for n in i.split()} for i in re.match(r'Card *\d+: ([\d ]+) \| ([\d ]+)', _card).groups())
    return len(winning.intersection(nums))


# Part 1
print(f'Part 1: {sum(int((1 << calculate_card(card)) / 2) for card in cards)}')


# Part 2
counts = [1] * len(cards)
for i, card in enumerate(cards):
    for j in range(i + 1, i + calculate_card(card) + 1):
        counts[j] += counts[i]

print(f'Part 2: {sum(counts)}')


