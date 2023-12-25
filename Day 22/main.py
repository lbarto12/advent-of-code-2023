from typing import List, Tuple, Dict, Set


with open('input.txt') as file:
    coords: List[Tuple[Tuple[int, ...], ...]] = []

    for line in file.readlines():
        _a, _b = line.split('~')
        coords.append((tuple(map(int, _a.split(','))), tuple(map(int, _b.strip().split(',')))))



def does_intersect(a: Tuple[Tuple[int, ...], ...], b: Tuple[Tuple[int, ...], ...]) -> bool:
    return max(a[0][0], b[0][0]) <= min(a[1][0], b[1][0]) and \
        max(a[0][1], b[0][1]) <= min(a[1][1], b[1][1])

def gravity(_coords: List[Tuple[Tuple[int, ...], ...]]) -> List[Tuple[Tuple[int, ...], ...]]:
    order: List[Tuple[Tuple[int, ...], ...]] = sorted(_coords, key=lambda x: x[0][2])

    for i, brick in enumerate(order):
        z: int = 1
        for _below in order[:i]:
            if does_intersect(brick, _below):
                z = max(z, _below[1][2] + 1)
        (x1, y1, z1), (x2, y2, z2) = brick
        order[i] = ((x1, y1, z), (x2, y2, z2 - (z1 - z)))

    return order


# Part 1
bricks: List[Tuple[Tuple[int, ...], ...]] = gravity(coords)

supports: Dict[int, Set[int]] = {i: set() for i, _ in enumerate(bricks)}
depends: Dict[int, Set[int]] = {i: set() for i, _ in enumerate(bricks)}

for j, above in enumerate(bricks):
    for i, below in enumerate(bricks[:j]):
        if does_intersect(below, above) and above[0][2] == below[1][2] + 1:
            supports[i].add(j)
            depends[j].add(i)


print(f"Part 1: {sum(all(len(depends[j]) >= 2 for j in supports[i]) for i, _ in enumerate(bricks))}")


# Part 2
ans: int = 0

for i, _ in enumerate(bricks):
    queue: List[int] = [block for block in supports[i] if len(depends[block]) == 1]
    fall: List[int] = queue[:]

    while queue:
        for s in filter(lambda x: x not in fall, supports[queue.pop(0)]):
            if all(x in fall for x in depends[s]):
                queue.append(s)
                fall.append(s)

    ans += len(fall)


print(f'Part 2: {ans}')






