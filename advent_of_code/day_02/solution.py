from rich import print

from itertools import pairwise


class Report(list[int]):
    def __init__(self, vector: list[int]):
        if len(vector) < 2:
            raise ValueError("Report must have at least two levels.")
        self.is_ascending = _is_ascending(vector[0], vector[1])
        super().__init__(vector)

    def is_safe(self) -> bool:
        for left, right in pairwise(self):
            if not _is_safe_jump(left, right) or not self.is_ascending == _is_ascending(left, right):
                return False
        return True

    def is_safe_dampened(self) -> bool:
        for left, right in pairwise(self):
            if not _is_safe_jump(left, right) or not self.is_ascending == _is_ascending(left, right):
                return any(Report(self[:i] + self[i + 1 :]).is_safe() for i, _ in enumerate(self))
        return True


def part_1(reports: list[Report]) -> int:
    return sum(report.is_safe() for report in reports)


def part_2(reports: list[Report]) -> int:
    return sum(report.is_safe_dampened() for report in reports)


def parse_data(raw_data: str) -> list[Report]:
    return [Report([int(c) for c in line.split()]) for line in raw_data.split("\n")]


def _is_ascending(a: int, b: int) -> bool:
    return a < b


def _is_safe_jump(a: int, b: int) -> bool:
    return 0 < abs(a - b) <= 3


def _read_inputs() -> list[Report]:
    with open("advent_of_code/day_02/inputs.txt", "r") as f:
        raw_data = f.read().strip()
    return parse_data(raw_data)


if __name__ == "__main__":
    inputs = _read_inputs()
    print(part_1(inputs))
    print(part_2(inputs))
