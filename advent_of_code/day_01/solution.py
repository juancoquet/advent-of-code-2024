from rich import print


def part_1(locations_a: list[int], locations_b: list[int]) -> int:
    return sum(abs(a - b) for a, b in zip(sorted(locations_a), sorted(locations_b)))


def part_2(locations_a: list[int], locations_b: list[int]) -> int:
    b_count: dict[int, int] = {}
    for b in locations_b:
        b_count[b] = b_count.get(b, 0) + 1
    return sum(a * b_count.get(a, 0) for a in locations_a)


def _read_inputs() -> tuple[list[int], list[int]]:
    with open("advent_of_code/day_01/inputs.txt", "r") as f:
        data = [[int(i) for i in line.split()] for line in f.readlines()]
    locations_a, locations_b = map(list, zip(*data))
    return locations_a, locations_b


if __name__ == "__main__":
    locations_a, locations_b = _read_inputs()
    print(part_1(locations_a, locations_b))
    print(part_2(locations_a, locations_b))
