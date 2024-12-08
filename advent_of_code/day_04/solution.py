from rich import print


def part_1(inputs):
    pass


def part_2(inputs):
    pass


def parse_data(raw_data: str) -> list[list[str]]:
    return [[c for c in line.strip()] for line in raw_data.split("\n")]


def _read_inputs():
    with open("advent_of_code/day_04/inputs.txt", "r") as f:
        raw_data = f.read().strip()
    return parse_data(raw_data)


if __name__ == "__main__":
    inputs = _read_inputs()
    print(part_1(inputs))
    print(part_2(inputs))

