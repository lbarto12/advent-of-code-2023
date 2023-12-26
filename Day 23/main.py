from typing import List, Tuple, Dict, Set

with open('input.txt') as file:
    paths: List[List[chr]] = [list(i.strip()) for i in file.readlines()]
    assert len(paths) == len(paths[0])
    SIZE = len(paths)


def merge_tuple(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    return a[0] + b[0], a[1] + b[1]

def can_move(_tile: chr, _delta: Tuple[int, int]) -> bool:
    return not {'>': (-1, 0), '<': (1, 0), 'v': (0, -1), '^': (0, 1)}.get(_tile) == _delta

def get_paths(_pos: Tuple[int, int]):
    _paths = []
    for d in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        x, y = merge_tuple(_pos, d)
        if (x, y) == _pos:
            continue
        if 0 <= x < SIZE and 0 <= y < SIZE and paths[y][x] != '#':
            _paths.append((x, y))
    return _paths

def get_longest(_graph, _seen, _pos = (1, 0)) -> int:
    if _pos == (SIZE - 2, SIZE - 1):
        return 1

    _seen.add(_pos)
    mx = 0
    for position, steps in _graph[_pos].items():
        if position in _seen:
            continue
        f = get_longest(_graph, _seen.copy(), position)
        mx = max(steps + f if f else 0, mx)

    return mx


def solve(slopes = False):
    graph = {(1, 0): {}, **{(j, i): {} for i in range(SIZE) for j in range(SIZE) if
                            paths[i][j] != '#' and len(get_paths((j, i))) >= 3}, (SIZE - 2, SIZE - 1): {}}

    for intersection in graph:
        queue = [(0, intersection, (0, 0))]
        seen = set()

        while queue:
            steps, pos, delta = queue.pop(0)

            if pos != intersection and pos in graph:
                graph[intersection][pos] = steps
                continue

            if pos in seen or (slopes and not can_move(paths[pos[1]][pos[0]], delta)):
                continue
            seen.add(pos)

            for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new = merge_tuple(pos, direction)
                if 0 <= new[0] < SIZE and 0 <= new[1] < SIZE and paths[new[1]][new[0]] != '#':
                    queue.append((steps + 1, new, direction))

    return get_longest(graph, set()) - 1


# Parts 1 & 2
print(f'Part 1: {solve(slopes=True)}')
print(f"Part 2: {solve()}")

