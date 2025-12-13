from itertools import groupby
from math import prod

from utils.runtime import get_runtime


def get_input1(test: str = None):
    with open('inputs/06') as f:
        base = test or f.read()
        l = base.splitlines()

    return [
        list(y) for y in zip(*[[int(x) for x in line.split()] for line in l[:-1]])
    ], l[-1].split()


def get_input2(test: str = None):
    with open('inputs/06') as f:
        base = test or f.read()
        l = base.splitlines()

    return [
        [int(y) for y in list(g)]
        for k, g in groupby(
            [''.join(x).strip() for x in list(zip(*l[:-1]))], key=lambda s: s == ''
        )
        if not k
    ], l[-1].split()


@get_runtime
def solve(number_columns: list[list[int]], operations: list[str]):
    op = {'+': sum, '*': prod}

    print(
        sum(
            [
                op[operation](numbers)
                for numbers, operation in zip(number_columns, operations)
            ]
        )
    )


solve(*get_input1())
solve(*get_input2())
