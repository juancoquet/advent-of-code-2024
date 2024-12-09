from rich import print

def part_1(inputs):
    pass


def part_2(inputs):
    pass


def parse_data(raw_data: str):
    pass


def _read_inputs():
    with open("advent_of_code/day_05/inputs.txt", "r") as f:
        raw_data = f.read().strip()
    return parse_data(raw_data)


if __name__ == "__main__":
    inputs = _read_inputs()
    print(part_1(inputs))
    print(part_2(inputs))