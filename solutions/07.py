from collections import Counter

from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/07') as f:
        base = test or f.read()
        l = [list(x) for x in base.splitlines()]

    return l


@get_runtime
def part_1(l: list[list[str]]):
    splits = 0

    current_beams = {(l[0].index('S'), 0)}
    processed_beams = set()

    while current_beams:
        x, y = current_beams.pop()

        if (x, y) in processed_beams:
            continue

        processed_beams.add((x, y))

        if y == len(l) - 1:
            continue

        if l[y + 1][x] == '.':
            current_beams.add((x, y + 1))
        elif l[y + 1][x] == '^':
            current_beams.add((x - 1, y + 1))
            current_beams.add((x + 1, y + 1))

            splits += 1

    print(splits)


@get_runtime
def part_2(l: list[list[str]]):
    timelines = Counter({l[0].index('S'): 1})

    for row in l[1:]:
        new_timelines = Counter()

        for x, count in timelines.items():
            if row[x] == '.':
                new_timelines[x] += count
            elif row[x] == '^':
                new_timelines[x - 1] += count
                new_timelines[x + 1] += count

        timelines = new_timelines

    print(sum(timelines.values()))


part_1(get_input())
part_2(get_input())
