from functools import reduce
from itertools import combinations
from operator import xor

from z3 import Int, Optimize, sat  # can be installed via `pip install z3-solver`

from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/10') as f:
        base = test or f.read()
        l = base.splitlines()
        res = []

        for line in l:
            parts = line.split(' ')
            indicator_length = len(parts[0]) - 2

            indicator_lights = int(
                parts.pop(0)[1:-1].replace('#', '1').replace('.', '0'), 2
            )
            joltage_requirements = [int(x) for x in parts.pop(-1)[1:-1].split(',')]
            # after popping indicator lights and joltage requirements, the remaining parts are button wirings
            button_wiring_schematics = [
                [int(y) for y in x[1:-1].split(',')] for x in parts
            ]

            res.append(
                (
                    indicator_length,
                    indicator_lights,
                    button_wiring_schematics,
                    joltage_requirements,
                )
            )

    return res


def button_to_int(button: list[int], n: int) -> int:
    value = 0

    for i in button:
        # set rightmost bit to 1 and shift it left to correct position
        # then OR it with current value to set that bit
        value |= 1 << (n - 1 - i)

    return value


@get_runtime
def part_1(l: list[tuple[int, int, list[list[int]], list[int]]]):
    total_button_presses = 0

    for indicator_length, indicator_lights, button_wiring_schematics, _ in l:
        button_wiring_schematics = [
            button_to_int(x, indicator_length) for x in button_wiring_schematics
        ]
        n = len(button_wiring_schematics)
        found = False

        for k in range(1, n + 1):
            # pressing a button more than once makes no sense as xoring twice is the same as not doing anything
            for indices in combinations(range(n), k):
                selection = [button_wiring_schematics[i] for i in indices]
                result = reduce(xor, selection)

                if result == indicator_lights:
                    found = True
                    break

            if found:
                total_button_presses += k
                break

    print(total_button_presses)


@get_runtime
def part_2(l: list[tuple[int, int, list[list[int]], list[int]]]):
    total_button_presses = 0

    for _, _, button_wiring_schematics, joltage_requirements in l:
        opt = Optimize()
        vars = [Int(f'x_{i}') for i in range(len(button_wiring_schematics))]

        for x in vars:  # non-negativity constraint for all variables
            opt.add(x >= 0)

        for i, target_val in enumerate(joltage_requirements):
            summe = 0  # sum over all buttons' effects on joltage i based on wiring schematic

            for j, affected_indices in enumerate(button_wiring_schematics):
                # if button j affects joltage i, include its variable in the sum
                if i in affected_indices:
                    summe += vars[j]

            opt.add(summe == target_val)

        opt.minimize(sum(vars))  # objective: minimize button presses

        if opt.check() == sat:  # checks if solvable
            model = opt.model()

            total_button_presses += sum(model[x].as_long() for x in vars)

    print(total_button_presses)


part_1(get_input())
part_2(get_input())
