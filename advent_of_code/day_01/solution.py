def part_1(locations_a: list[int], locations_b: list[int]) -> int:
    return sum(abs(a - b) for a, b in zip(sorted(locations_a), sorted(locations_b)))
