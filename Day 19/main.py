import copy
import functools
import re
from typing import List, Dict, Tuple

with open('input.txt') as file:
    workflows, parts = [i.split('\n') for i in file.read().split('\n\n')]
    parts: List = [dict(re.findall(r'(\w)=(\d+)', i)) for i in parts]
    workflows: Dict[str, Tuple[List[Tuple[str, ...]], str]] = \
        {re.search(r'(\w+){', i).group(1): (re.findall(r'(\w+?)([<>])(\d+):(\w+)[,}]', i[i.index('{'):]),
                                            re.search(r',(\w+)}', i).group(1)) for i in workflows}


# Part 1
def accepted(_part, _workflows) -> bool:
    workflow: Tuple[List[Tuple[str, ...]], str] = _workflows['in']
    while workflow:
        for target, op, cmp, outcome in workflow[0]:
            if eval(f'{_part[target]}{op}{cmp}'):
                break
        else:
            outcome = workflow[-1]
        if outcome == 'A':
            return True
        workflow = workflows.get(outcome)
    return False


print(f"Part 1: {sum(sum(map(int, part.values())) for part in parts if accepted(part, workflows))}")


# Part 2
def range_accepted(_ranges: Dict[chr, Tuple[int, int]],
                   _workflows: Dict[str, Tuple[List[Tuple[str, ...]], str]],
                   _workflow: str) -> int:
    if _workflow in 'AR':
        return functools.reduce(lambda a, c: (c[1] - c[0] + 1) * a, _ranges.values(), 1) if _workflow == 'A' else 0

    workflow, default = _workflows[_workflow]

    acc: int = 0
    new_ranges: Dict[chr, Tuple[int, int]] = copy.copy(_ranges)
    for target, op, num, destination in workflow:
        num = int(num)
        mn, mx = new_ranges[target]
        if (op == '<' and mx < num) or (op == '>' and mn > num):
            acc += range_accepted(new_ranges, _workflows, destination)
        elif mn < num < mx:
            l, r = (mn, num - (op == '<')), (num + (op == '>'), mx)
            new_ranges[target] = l if op == '>' else r
            acc += range_accepted(copy.copy(new_ranges) | {target: l if op == '<' else r}, _workflows, destination)

    return acc + range_accepted(new_ranges, _workflows, default)


print(f'Part 2: {range_accepted(dict(zip("xmas", [(1, 4000)] * 4)), workflows, "in")}')
