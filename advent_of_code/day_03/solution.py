from dataclasses import dataclass
from enum import Enum
import re
from typing import Match
from rich import print


class Operation(Enum):
    DO = (0,)
    DONT = (1,)
    MUL = (2,)


@dataclass
class Instruction:
    op: Operation
    re: Match


def part_1(inputs: str) -> int:
    regex = re.compile(r"mul\((?P<a>\d+),(?P<b>\d+)\)")
    mul_values = regex.findall(inputs)
    return sum(int(a) * int(b) for a, b in mul_values)


def part_2(inputs: str) -> int:
    do_regex = re.compile(r"do\(\)")
    dont_regex = re.compile(r"don't\(\)")
    mul_regex = re.compile(r"mul\((?P<a>\d+),(?P<b>\d+)\)")
    dos = [Instruction(op=Operation.DO, re=m) for m in do_regex.finditer(inputs)]
    donts = [Instruction(op=Operation.DONT, re=m) for m in dont_regex.finditer(inputs)]
    muls = [Instruction(op=Operation.MUL, re=m) for m in mul_regex.finditer(inputs)]
    instructions = sorted(dos + donts + muls, key=lambda inst: inst.re.start())

    do = True
    total = 0
    for inst in instructions:
        if inst.op == Operation.DO:
            do = True
        elif inst.op == Operation.DONT:
            do = False
        elif do:
            total += int(inst.re.group("a")) * int(inst.re.group("b"))

    return total


def _read_inputs() -> str:
    with open("advent_of_code/day_03/inputs.txt", "r") as f:
        return f.read().strip()


if __name__ == "__main__":
    inputs = _read_inputs()
    print(part_1(inputs))
    print(part_2(inputs))
