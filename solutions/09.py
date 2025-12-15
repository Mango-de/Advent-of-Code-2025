from itertools import combinations

from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/09') as f:
        base = test or f.read()
        l = [tuple(int(y) for y in x.split(',')) for x in base.splitlines()]

    return l


@get_runtime
def part_1(l: list[tuple[int, int]]):
    largest_area = 0

    for (y1, x1), (y2, x2) in combinations(l, 2):
        area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        largest_area = max(largest_area, area)

    print(largest_area)


@get_runtime
def part_2(l: list[tuple[int, int]]):
    pass


part_1(get_input())
part_2(get_input())
