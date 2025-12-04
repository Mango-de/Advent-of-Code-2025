from copy import deepcopy
from operator import add

from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/04') as f:
        base = test or f.read()
        l = [list(x) for x in base.splitlines()]

    return l


def get_adjacent_forclifts_count(l: list[list[str]], y: int, x: int) -> int:
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    count = 0

    for direction in directions:
        ny, nx = map(add, (y, x), direction)
        if 0 <= ny < len(l) and 0 <= nx < len(l[ny]) and l[ny][nx] == '@':
            count += 1

    return count


@get_runtime
def part_1(l: list[list[str]]):
    accessible_rolls = 0

    for i, y in enumerate(l):
        for j, x in enumerate(y):
            if x == '@':
                if get_adjacent_forclifts_count(l, i, j) < 4:
                    accessible_rolls += 1

    print(accessible_rolls)


@get_runtime
def part_2(l: list[list[str]]):
    accessible_rolls = 0

    while True:
        temp_l = deepcopy(l)
        removed = 0

        for i, y in enumerate(l):
            for j, x in enumerate(y):
                if x == '@':
                    if get_adjacent_forclifts_count(l, i, j) < 4:
                        removed += 1
                        temp_l[i][j] = 'x'

        if removed > 0:
            accessible_rolls += removed
        else:
            break

        l = temp_l

    print(accessible_rolls)


part_1(get_input())
part_2(get_input())
