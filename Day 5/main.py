from typing import Dict, List

def split_maps(lst: List[str]) -> List[List[List[int]]]:
    res = []
    for line in lst:
        if line == "\n":
            continue
        if line[0].isalpha():
            res.append([])
        else:
            res[-1].append([int(i) for i in line.split()])
    return res

class Mapping:
    def __init__(self, args):
        self.destination, self.source, self.range = args
        self.offset: int = self.destination - self.source

    def is_mapped(self, target: int) -> bool:
        return self.source <= target < self.source + self.range

    def get_mapped(self, target: int) -> int:
        return target + self.offset if self.is_mapped(target) else target

class MappedLevel:
    def __init__(self, level: List[List[int]]):
        self.level = [Mapping(i) for i in level]

    def get_mapped(self, target: int) -> int:
        for mapping in self.level:
            if mapping.is_mapped(target):
                return mapping.get_mapped(target)
        return target


with open('input.txt') as file:
    _read = file.readlines()
    seeds: List[int] = [int(i) for i in filter(lambda x: x.isnumeric(), _read.pop(0).split())]
    almanac_read: List[List[List[int]]] = split_maps(_read)
    almanac: List[MappedLevel] = [MappedLevel(i) for i in almanac_read]


# Part 1
seeds_copy = seeds[:]
for level in almanac:
    for j, seed in enumerate(seeds_copy):
        seeds_copy[j] = level.get_mapped(seed)

print(f'Part 1: {min(seeds_copy)}')



# Part 2
seed_ranges = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]

for level in almanac:
    maps = level.level
    new = []
    while seed_ranges:
        mn, mx = seed_ranges.pop(0)
        for mp in maps:
            start, end = max(mn, mp.source), min(mx, mp.source + mp.range)
            if start < end:
                new.append((start + mp.offset, end + mp.offset))
                if start > mn:
                    seed_ranges.append((mn, start))
                if mx > end:
                    seed_ranges.append((end, mx))
                break
        else:
            new.append((mn, mx))
    seed_ranges = new

print(f'Part 2: {min(i[0] for i in seed_ranges)}')





