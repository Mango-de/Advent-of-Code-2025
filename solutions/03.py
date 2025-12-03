from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/03') as f:
        base = test or f.read()
        l = base.splitlines()

    return l


@get_runtime
def part_1(l: list[str]):
    total_output = 0

    for line in l:
        digit1 = max(line[:-1])
        index1 = line.index(digit1)
        digit2 = max(line[index1 + 1 :])

        total_output += int(digit1 + digit2)

    print(total_output)


@get_runtime
def part_2(l: list[str]):
    total_output = 0

    for line in l:
        output = ''
        index = 0

        for i in range(11, -1, -1):  # 11 trough 0 (12 digits)
            digit = max(line[index : len(line) - i])

            output += digit
            index = line.index(digit, index, len(line) - i) + 1

        total_output += int(output)

    print(total_output)


part_1(get_input())
part_2(get_input())
