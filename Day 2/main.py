import re

# Part 1
with open('input.txt') as games:
    sm = 0
    limits = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    for game_id, game in enumerate(games.readlines()):
        valid = True
        for color, limit in limits.items():
            all_draws = re.findall(rf'(\d+) {color}', game)
            if any(int(i) > limit for i in all_draws):
                valid = False
        sm += valid * (game_id + 1)
    print(f'Part 1: {sm}')


# Part 2
with open('input.txt') as games:
    sm = 0
    for game in games.readlines():
        prod = 1
        for color in ["red", "green", "blue"]:
            all_draws = list(map(int, re.findall(rf'(\d+) {color}', game)))
            prod *= max(all_draws)
        sm += prod
    print(f'Part 2: {sm}')


