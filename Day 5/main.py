from typing import List, Tuple


with open('input.txt') as file:
    mappings: List[str] = file.readlines()


class Mapping:
    def __init__(self, args):
        self.destination, self.source, self.range = args
        self.offset: int = self.destination - self.source

    def is_mapped(self, target: int) -> bool:
        return self.source <= target < self.source + self.range

    def get_mapped(self, target: int) -> int:
        return target + self.offset if self.is_mapped(target) else target


class MappedLevel:
    def __init__(self, _level: List[List[int]]):
        self.level: List[Mapping] = [Mapping(i) for i in _level]

    def get_mapped(self, target: int) -> int:
        for mapping in self.level:
            if mapping.is_mapped(target):
                return mapping.get_mapped(target)
        return target


def split_maps(lst: List[str]) -> List[List[List[int]]]:
    res: List[List[List[int]]] = []
    for line in lst:
        if line == "\n":
            continue
        if line[0].isalpha():
            res.append([])
        else:
            res[-1].append([int(i) for i in line.split()])
    return res


seeds: List[int] = [int(i) for i in filter(lambda x: x.isnumeric(), mappings.pop(0).split())]
almanac: List[MappedLevel] = [MappedLevel(i) for i in split_maps(mappings)]


# Part 1
seeds_copy = seeds[:]
for level in almanac:
    for j, seed in enumerate(seeds_copy):
        seeds_copy[j] = level.get_mapped(seed)

print(f'Part 1: {min(seeds_copy)}')



# Part 2
seed_ranges: List[Tuple[int, int]] = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
for level in almanac:
    new: List[Tuple[int, int]] = []
    while seed_ranges:
        mn, mx = seed_ranges.pop(0)
        for mp in level.level:
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

