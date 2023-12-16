import re
from typing import List, Dict

with open('input.txt') as file:
    games: List[str] = file.readlines()

# Part 1
sm: int = 0
limits: Dict[str, int] = {"red": 12, "green": 13, "blue": 14}
for game_id, game in enumerate(games, 1):
    valid: bool = True
    for color, limit in limits.items():
        all_draws: List[str] = re.findall(rf'(\d+) {color}', game)
        if any(int(i) > limit for i in all_draws):
            valid = False
    sm += valid * game_id

print(f'Part 1: {sm}')


# Part 2
sm = 0
for game in games:
    prod: int = 1
    for color in ["red", "green", "blue"]:
        all_draws: List[int] = list(map(int, re.findall(rf'(\d+) {color}', game)))
        prod *= max(all_draws)
    sm += prod

print(f'Part 2: {sm}')


