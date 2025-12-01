from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/01') as f:
        base = test or f.read()
        l = base.splitlines()
        l = [int(line.replace('L', '-').replace('R', '')) for line in l]

    return l


@get_runtime
def part_1(l: list[int]):
    dial_position = 50
    counter = 0

    for rotation in l:
        dial_position += rotation
        dial_position %= 100

        if dial_position == 0:
            counter += 1

    print(counter)


@get_runtime
def part_2(l: list[int]):
    dial_position = 50
    counter = 0

    for rotation in l:
        hundreds = abs(rotation) // 100
        counter += hundreds

        new_pos = (
            dial_position + rotation - hundreds * 100 * (-1 if rotation < 0 else 1)
        )

        if (new_pos > 99 or new_pos <= 0) and dial_position != 0:
            counter += 1

        dial_position = new_pos
        dial_position %= 100

    print(counter)


part_1(get_input())
part_2(get_input())
