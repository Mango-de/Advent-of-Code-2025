from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/02') as f:
        base = test or f.read()
        l = [
            tuple(map(int, x)) for x in [y.strip().split('-') for y in base.split(',')]
        ]

    return l


def get_divisors(n: int) -> set[int]:
    result = set()

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)

    result.remove(1)  # ID must be split into at least two parts

    return result


@get_runtime
def part_1(l: list[tuple[int, int]]):
    result = 0

    for a, b in l:
        for num in range(a, b + 1):
            s = str(num)
            if len(s) % 2 == 0:
                half = len(s) // 2
                if s[:half] == s[half:]:
                    result += num

    print(result)


@get_runtime
def part_2(l: list[tuple[int, int]]):
    result = 0

    for a, b in l:
        for num in range(a, b + 1):
            s = str(num)
            for divisor in get_divisors(len(s)):
                part = len(s) // divisor
                if all(
                    s[i * part : (i + 1) * part] == s[0:part] for i in range(divisor)
                ):
                    result += num
                    break

    print(result)


part_1(get_input())
part_2(get_input())
