import functools
from collections import Counter
from typing import List

with open('input.txt') as file:
    hands = list(map(lambda x: (x[0], int(x[1])), [i.split() for i in file.readlines()]))

class HandType:
    FIVE = 6
    FOUR = 5
    HOUSE = 4
    THREE = 3
    TWO = 2
    ONE = 1
    HIGH = 0

def cmp_card(_card: str, part = 1) -> int:
    return {
        "T": 10, "J": 11 if part == 1 else 1, "Q": 12, "K": 13, "A": 14,
    }.get(_card) or int(_card)

def get_type(cards: str, part = 1):
    num_jacks: int = cards.count('J')
    if num_jacks and part == 2:
        counts: List[int] = list(dict(Counter(cards.replace('J', ''))).values())
        mx: int = max(counts) if counts else 0
        if num_jacks + mx >= 4:
            counts = [num_jacks + mx]
        elif (mx == 3 or counts.count(2) == 2) and num_jacks == 1:
            counts = [3, 2]
        else:
            counts[counts.index(mx)] += num_jacks
    else:
        counts: List[int] = list(dict(Counter(cards)).values())
    return {
        5: HandType.FIVE, 4: HandType.FOUR, 3: HandType.HOUSE if 2 in counts else HandType.THREE,
        2: HandType.TWO if counts.count(2) == 2 else HandType.ONE
    }.get(max(counts), HandType.HIGH)



def cmp_hand(a: tuple[str, int], b: tuple[str, int], part = 1) -> int:
    a_val, b_val = get_type(a[0], part), get_type(b[0], part)
    if a_val != b_val:
        return a_val - b_val

    for i in range(5):
        diff: int = cmp_card(a[0][i], part) - cmp_card(b[0][i], part)
        if diff != 0:
            return diff


# Part 1
print(f'Part 1: {sum(v[1] * (i + 1) for i, v in enumerate(sorted(hands, key=functools.cmp_to_key(cmp_hand))))}')


# Part 2
print(f'Part 2: {sum([v[1] * (i + 1) for i, v in enumerate(sorted(hands, key=functools.cmp_to_key(lambda a, b: cmp_hand(a, b, part=2))))])}')

