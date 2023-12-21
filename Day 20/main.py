import math
import re
import sys
from typing import List, Dict, Tuple, Union, Optional, Callable, Any


with open('input.txt') as file:
    read: List[str] = file.readlines()
    # my ugliest read ever, but *I* think it's kind of cute ;)
    system: Dict[str, Dict[str, Union[List[str], str]]] = \
        dict([(line.split('->')[0].strip()[1:]
               if line.split('->')[0].strip()[0] in '%&' else line.split('->')[0].strip(),
               {
                   'type': line.split('->')[0].strip()[0],
                   'destinations': [i.strip() for i in line.split('->')[1].strip().split(',')]
               }) for line in read])

class Module:
    PULSE_MAP: Dict[int, int] = {0: 0, 1: 0}

    @staticmethod
    def output_pulse(pulse: int):
        Module.PULSE_MAP[pulse] += 1

    def __init__(self, _name: str):
        self.name: str = _name
        self.destinations: List[Module] = []
        self.parents: List[Module] = []

    def pulse_in(self, _type: int, _, __):
        Module.PULSE_MAP[_type] += 1

    def pulse_out(self, cp: int) -> int:
        return cp

    def add_destination(self, destination: Any):
        self.destinations.append(destination)

    def add_parent(self, parent: Any):
        self.parents.append(parent)

class BroadCaster(Module):
    def __init__(self, _name: str):
        super().__init__(_name)

class FlipFlop(Module):
    def __init__(self, _name):
        super().__init__(_name)
        self.on: bool = False

    def pulse_in(self, _type: int, caller: Module, _):
        super().pulse_in(_type, caller, _)
        if _type == 0:
            self.on = not self.on

    def pulse_out(self, cp: int) -> Optional[int]:
        return int(self.on) if cp == 0 else None

class Conjunction(Module):
    def __init__(self, _name: str):
        super().__init__(_name)
        self.memory: Dict[str, int] = {}
        self._flipped: Dict[str, int] = {}

    def add_parent(self, parent: Module):
        super().add_parent(parent)
        self.memory[parent.name] = 0
        self._flipped[parent.name] = 0

    def pulse_in(self, _type: int, caller: Module, flip_assign: int):
        super().pulse_in(_type, caller, flip_assign)
        self.memory[caller.name] = _type

        if _type and not self._flipped[caller.name]:
            self._flipped[caller.name] = flip_assign


    def pulse_out(self, _) -> int:
        return int(not all(self.memory.values()))

    def has_flipped_all(self) -> bool:
        return all(self._flipped.values())

    def get_flip_points(self) -> Dict[str, int]:
        return self._flipped

def create_system(_system: Dict[str, Dict[str, Union[List[str], str]]]) -> Dict[str, Module]:
    module_system: Dict[str, Module] = {}

    for name, module in _system.items():
        module_type = FlipFlop if module['type'] == '%' \
            else Conjunction if module['type'] == '&' \
            else BroadCaster if name == 'broadcaster' \
            else Module
        module_system[name] = module_type(name)

    for name, module in _system.items():
        for destination in module['destinations']:
            if d := module_system.get(destination):
                d.add_parent(module_system[name])
            module_system[name].add_destination(d)

    return module_system

def push_button(_modules: Dict[str, Module], conjunction_tracker: int = 0):
    queue: List[Tuple[int, Module, Module]] = [(0, Module('button'), _modules['broadcaster'])]

    while queue:
        callers_pulse_in, caller, module = queue.pop(0)

        if (pulse := caller.pulse_out(callers_pulse_in)) is None:
            continue

        if not module:
            Module.output_pulse(caller.pulse_out(callers_pulse_in))
            continue

        module.pulse_in(pulse, caller, conjunction_tracker)
        queue += [(pulse, module, destination) for destination in module.destinations]


# Part 1
modules: Dict[str, Module] = create_system(system)

for _ in range(1000):
    push_button(modules)

print(f'Part 1: {Module.PULSE_MAP[0] * Module.PULSE_MAP[1]}')


# Part 2
modules: Dict[str, Module] = create_system(system)
gate: Module | Conjunction = modules[re.search(r'&(\w+) -> rx', ''.join(read)).group(1)]

button_presses: int = 0
while not gate.has_flipped_all():
    push_button(modules, (button_presses := button_presses + 1))

print(f'Part 2: {math.lcm(*gate.get_flip_points().values())}')
