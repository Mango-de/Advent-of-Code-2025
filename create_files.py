import os
from datetime import datetime

import dotenv
import requests

dotenv.load_dotenv()

day = datetime.today().day
result = requests.get(
    f'https://adventofcode.com/2025/day/{day}/input',
    cookies={'session': os.environ['SESSION_TOKEN']},
)

for l in result.text.split('\n')[:5]:
    print(l)
print('...')

with open(f'inputs/{day:02d}', 'w') as f:
    f.write(result.text[:-1])

with open(f'solutions/{day:02d}.py', 'w') as f:
    f.write(
        f"""from utils.runtime import get_runtime


def get_input(test: str = None):
    with open('inputs/{day:02d}') as f:
        base = test or f.read()
        l = base.splitlines()

    return l


@get_runtime
def part_1(l: list[str]):
    pass


@get_runtime
def part_2(l: list[str]):
    pass


part_1(get_input())
part_2(get_input())
"""
    )
