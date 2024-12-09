from dataclasses import dataclass
from rich import print


@dataclass
class Rule:
    x: int
    y: int


class InstructionSet(list[int]):
    pass


def part_1(inputs):
    pass


def part_2(inputs):
    pass


def parse_data(raw_data: str) -> tuple[list[Rule], list[InstructionSet]]:
    rules_str, inst_str = raw_data.split("\n\n")
    rules = [Rule(*map(int, rule.split("|"))) for rule in rules_str.split("\n")]
    instructions = [InstructionSet(map(int, inst.split(","))) for inst in inst_str.split("\n")]
    return rules, instructions


def _read_inputs():
    with open("advent_of_code/day_05/inputs.txt", "r") as f:
        raw_data = f.read().strip()
    return parse_data(raw_data)


if __name__ == "__main__":
    inputs = _read_inputs()
    print(part_1(inputs))
    print(part_2(inputs))
