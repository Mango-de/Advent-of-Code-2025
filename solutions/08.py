from itertools import combinations
from math import prod

from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/08') as f:
        base = test or f.read()
        l = [tuple(int(y) for y in x.split(',')) for x in base.splitlines()]

    return l


# when sorting by distance, it is sufficient to use squared distances
# d1 < d2 <=> d1^2 < d2^2 for d1, d2 >= 0
def calculate_squared_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    return sum((a[i] - b[i]) ** 2 for i in range(len(a)))


@get_runtime
def solve(l: list[tuple[int, int, int]], *, part: int):
    parent: dict[tuple, tuple] = {point: point for point in l}
    size: dict[tuple, int] = {point: 1 for point in l}

    distance_mapping = {
        (a, b): calculate_squared_distance(a, b) for a, b in combinations(l, 2)
    }

    # sorted by squared distance
    connections = [
        k
        for k, _ in sorted(
            distance_mapping.items(),
            key=lambda item: item[1],
        )
    ]

    def find(i: tuple[int, int, int]) -> tuple[int, int, int]:
        if parent[i] == i:
            return i

        parent[i] = find(parent[i])

        return parent[i]

    def union(i: tuple[int, int, int], j: tuple[int, int, int]):
        root_i = find(i)
        root_j = find(j)

        if root_i != root_j:
            if size[root_i] < size[root_j]:
                root_i, root_j = root_j, root_i

            parent[root_j] = root_i
            size[root_i] += size[root_j]
            del size[root_j]

    match part:
        case 1:
            for connection_count, (a, b) in enumerate(connections):
                if connection_count == 1000:
                    break

                union(a, b)

            circuit_sizes = list(size.values())
            circuit_sizes.sort(reverse=True)

            print(prod(circuit_sizes[:3]))

        case 2:
            for a, b in connections:
                union(a, b)

                if len(size) == 1:
                    print(a[0] * b[0])
                    break


solve(get_input(), part=1)
solve(get_input(), part=2)
