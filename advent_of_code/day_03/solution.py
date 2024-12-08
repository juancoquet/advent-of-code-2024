import re
from rich import print


def part_1(inputs: str) -> int:
    regex = re.compile(r"mul\((?P<a>\d+),(?P<b>\d+)\)")
    mul_values = regex.findall(inputs)
    return sum(int(a) * int(b) for a, b in mul_values)


def part_2(inputs: str):
    pass


def _read_inputs() -> str:
    with open("advent_of_code/day_03/inputs.txt", "r") as f:
        return f.read().strip()


if __name__ == "__main__":
    inputs = _read_inputs()
    print(part_1(inputs))
    print(part_2(inputs))
