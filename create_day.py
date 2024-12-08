import argparse
from os.path import isfile
import shutil
import os

import requests
from dotenv import load_dotenv

load_dotenv()
SESSION = os.getenv("SESSION")
if SESSION is None:
    raise ValueError("Populate the SESSION cookie in .env")


TEMPLATE_SOLUTION = """
from rich import print

def part_1(inputs):
    pass


def part_2(inputs):
    pass


def parse_data(raw_data: str):
    pass


def _read_inputs():
    with open("{path}", "r") as f:
        raw_data = f.read().strip()
    return parse_data(raw_data)


if __name__ == "__main__":
    inputs = _read_inputs()
    print(part_1(inputs))
    print(part_2(inputs))
"""

TEMPLATE_TEST = """
from advent_of_code.day_{day}.solution import part_1, part_2


def test_part_1():
    pass

def test_part_2():
    pass
"""


def create(day: int):
    dir = f"advent_of_code/day_{day:02d}"
    test_file = f"tests/test_day_{day:02d}.py"
    if os.path.isdir(dir):
        shutil.rmtree(dir)
    if os.path.isfile(test_file):
        os.remove(test_file)

    os.mkdir(dir)
    open(f"{dir}/README.md", "w").close()
    open(f"{dir}/__init__.py", "w").close()
    with open(f"{dir}/inputs.txt", "w") as f:
        f.write(get_inputs(day))
    with open(f"{dir}/solution.py", "w") as f:
        f.write(TEMPLATE_SOLUTION.format(path=f"{dir}/inputs.txt").strip())
    with open(test_file, "w") as f:
        f.write(TEMPLATE_TEST.format(day=f"{day:02d}").strip())


def get_inputs(day: int):
    url = f"https://adventofcode.com/2024/day/{day}/input"
    inputs = requests.get(url, cookies={"session": str(SESSION)})
    return inputs.text


def parse_day() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int, help="The day to create.")
    args = parser.parse_args()
    return args.day


if __name__ == "__main__":
    day = parse_day()
    create(day)
