from itertools import pairwise

from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/05') as f:
        base = test or f.read()
        fresh, available = base.split('\n\n')
        fresh = [tuple(map(int, line.split('-'))) for line in fresh.splitlines()]
        available = [int(line) for line in available.splitlines()]

    return fresh, available


@get_runtime
def part_1(fresh: list[tuple[int, int]], available: list[int]):
    fresh_count = 0

    for a in available:
        for start, end in fresh:
            if start <= a <= end:
                fresh_count += 1
                break

    print(fresh_count)


@get_runtime
def part_2(fresh: list[tuple[int, int]], _):
    fresh.sort(key=lambda x: x[0])

    while True:
        for i, ((s1, e1), (s2, e2)) in enumerate(pairwise(fresh)):
            if e1 >= s2 and e2 >= s1:
                start = min(s1, s2)
                end = max(e1, e2)

                fresh.pop(i)
                fresh.pop(i)
                fresh.insert(i, (start, end))

                break

        else:  # no ranges merged -> finished
            break

    print(sum(end - start + 1 for start, end in fresh))


part_1(*get_input())
part_2(*get_input())
