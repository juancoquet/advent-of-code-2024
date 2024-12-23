from dataclasses import dataclass

from rich import print


@dataclass
class Rule:
    x: int
    y: int


class InstructionSet(list[int]):
    pass


def part_1(rules: list[Rule], instructions: list[InstructionSet]) -> int:
    # an instruction set is valid if none of the numbers appear in an order that violates a rule
    valid_mids: list[int] = []
    for inst in instructions:
        relevant_rules = [r for r in rules if r.x in inst and r.y in inst]
        is_valid = True

        for rule in relevant_rules:
            if not _is_valid_instruction(inst, rule):
                is_valid = False

        if is_valid:
            mid = inst[len(inst) // 2]
            valid_mids.append(mid)

    return sum(valid_mids)


def part_2(rules: list[Rule], instructions: list[InstructionSet]) -> int:
    valid_mids: list[int] = []
    for inst in instructions:
        relevant_rules = sorted(
            [r for r in rules if r.x in inst and r.y in inst], key=lambda r: inst.index(r.x)
        )
        if all(_is_valid_instruction(inst, rule) for rule in relevant_rules):
            continue

        for rule in relevant_rules:
            if (x := inst.index(rule.x)) >= (y := inst.index(rule.y)):
                out_of_place = inst.pop(x)
                pre, post = inst[:y], inst[y:]
                inst = pre + [out_of_place] + post

        mid = inst[len(inst) // 2]
        valid_mids.append(mid)

    return sum(valid_mids)


def _is_valid_instruction(instruction: InstructionSet, rule: Rule) -> bool:
    return instruction.index(rule.x) < instruction.index(rule.y)


def parse_data(raw_data: str) -> tuple[list[Rule], list[InstructionSet]]:
    rules_str, inst_str = raw_data.split("\n\n")
    rules = [Rule(*map(int, rule.split("|"))) for rule in rules_str.split("\n")]
    instructions = [InstructionSet(map(int, inst.split(","))) for inst in inst_str.split("\n")]
    return rules, instructions


def _read_inputs() -> tuple[list[Rule], list[InstructionSet]]:
    with open("advent_of_code/day_05/inputs.txt", "r") as f:
        raw_data = f.read().strip()
    return parse_data(raw_data)


if __name__ == "__main__":
    rules, instructions = _read_inputs()
    print(part_1(rules, instructions))
    print(part_2(rules, instructions))
