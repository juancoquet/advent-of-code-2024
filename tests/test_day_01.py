from advent_of_code.day_01.solution import part_1


def test_part_01():
    locations_a = [3, 4, 2, 1, 3, 3]
    locations_b = [4, 3, 5, 3, 9, 3]
    res = part_1(locations_a, locations_b)
    assert res == 11
