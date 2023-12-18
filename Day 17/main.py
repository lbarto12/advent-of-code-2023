from typing import List, Tuple, Dict, Optional, Callable
import heapq
from collections import defaultdict


with open('input.txt') as file:
    Direction = Position = Tuple[int, int]  # For my own clarity in solving this problem
    Graph = List[List[int]]
    graph: Graph = [list(map(int, line.strip())) for line in file.readlines()]

def merge_tuple(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    return a[0] + b[0], a[1] + b[1]

def valid_pos(_graph: Graph, _pos: Position) -> bool:
    return 0 <= _pos[0] < len(_graph) and 0 <= _pos[1] < len(_graph[0])

def dijkstra(_graph: Graph, get_straight: Callable, limit: int):
    dists: Dict[Position: Dict[Tuple[Direction, int]: int]] \
        = {(i, j): defaultdict(lambda: float("inf")) for j in range(len(_graph[0])) for i in range(len(_graph))}
    queue: List[Tuple[int, Position, Direction, int]] = [(0, (0, 0), (0, 0), 1)]

    while queue:
        current_dist, position, p_dir, straight = heapq.heappop(queue)
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_straight: int = get_straight(p_dir, direction, straight)
            new_pos: Position = merge_tuple(position, direction)
            if not valid_pos(_graph, new_pos) or not new_straight or new_straight == limit:
                continue

            new_dist: int = current_dist + _graph[new_pos[0]][new_pos[1]]
            if new_dist < dists[new_pos][(direction, new_straight)]:
                dists[new_pos][(direction, new_straight)] = new_dist
                heapq.heappush(queue, (new_dist, new_pos, direction, new_straight))

    return dists[(len(_graph) - 1, len(_graph[0]) - 1)]


# Part 1
def get_straight_p1(dr1: Direction, dr2: Direction, s: int) -> Optional[int]:
    return None if dr1 == (-dr2[0], -dr2[1]) else s + 1 if dr1 == dr2 else 1


print(f'Part 1: {min(dijkstra(graph, get_straight_p1, 4).values())}')



# Part 2
def get_straight_p2(dr1: Direction, dr2: Direction, s: int) -> Optional[int]:
    return s + 1 if dr1 == dr2 else 1 if s >= 4 or dr1 == (0, 0) else None


print(f'Part 2: {min(h for (_, f), h in dijkstra(graph, get_straight_p2, 11).items() if f >= 4)}')
