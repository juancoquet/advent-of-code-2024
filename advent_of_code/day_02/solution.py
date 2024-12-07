from rich import print


class Report(list[int]):
    def __init__(self, vector: list[int]):
        if not vector:
            raise ValueError("Report cannot be empty")
        super().__init__(vector)

    def is_safe(self) -> bool:
        ascending = False
        for i in range(1, len(self)):
            left, right = self[i - 1], self[i]
            if i == 1:
                ascending = is_ascending(left, right)
            if not is_safe_jump(left, right) or not ascending == is_ascending(left, right):
                return False
        return True


def part_1(reports: list[Report]) -> int:
    return sum(report.is_safe() for report in reports)


def is_ascending(a: int, b: int) -> bool:
    return a < b


def is_safe_jump(a: int, b: int) -> bool:
    return 0 < abs(a - b) <= 3


def read_inputs() -> list[Report]:
    with open("advent_of_code/day_02/inputs.txt", "r") as f:
        raw_data = f.read().strip()
    return parse_data(raw_data)


def parse_data(raw_data: str) -> list[Report]:
    return [Report([int(c) for c in line.split()]) for line in raw_data.split("\n")]


if __name__ == "__main__":
    inputs = read_inputs()
    print(inputs)
    print(part_1(inputs))
