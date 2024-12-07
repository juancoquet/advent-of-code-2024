def part_1(reports: list[list[int]]) -> int:
    return -1


def parse_data(raw_data: str) -> list[list[int]]:
    return [[int(c) for c in line.split()] for line in raw_data.split("\n")]
