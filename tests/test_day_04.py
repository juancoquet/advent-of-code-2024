from advent_of_code.day_04.solution import parse_data, part_1, part_2


def test_part_1():
    inputs = [
        ["M", "M", "M", "S", "X", "X", "M", "A", "S", "M"],
        ["M", "S", "A", "M", "X", "M", "S", "M", "S", "A"],
        ["A", "M", "X", "S", "X", "M", "A", "A", "M", "M"],
        ["M", "S", "A", "M", "A", "S", "M", "S", "M", "X"],
        ["X", "M", "A", "S", "A", "M", "X", "A", "M", "M"],
        ["X", "X", "A", "M", "M", "X", "X", "A", "M", "A"],
        ["S", "M", "S", "M", "S", "A", "S", "X", "S", "S"],
        ["S", "A", "X", "A", "M", "A", "S", "A", "A", "A"],
        ["M", "A", "M", "M", "M", "X", "M", "M", "M", "M"],
        ["M", "X", "M", "X", "A", "X", "M", "A", "S", "X"],
    ]
    exp = 18
    res = part_1(inputs)
    assert res == exp


def test_part_2():
    pass


def test_parse_data():
    raw_data = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
    """.strip()
    exp = [
        ["M", "M", "M", "S", "X", "X", "M", "A", "S", "M"],
        ["M", "S", "A", "M", "X", "M", "S", "M", "S", "A"],
        ["A", "M", "X", "S", "X", "M", "A", "A", "M", "M"],
        ["M", "S", "A", "M", "A", "S", "M", "S", "M", "X"],
        ["X", "M", "A", "S", "A", "M", "X", "A", "M", "M"],
        ["X", "X", "A", "M", "M", "X", "X", "A", "M", "A"],
        ["S", "M", "S", "M", "S", "A", "S", "X", "S", "S"],
        ["S", "A", "X", "A", "M", "A", "S", "A", "A", "A"],
        ["M", "A", "M", "M", "M", "X", "M", "M", "M", "M"],
        ["M", "X", "M", "X", "A", "X", "M", "A", "S", "X"],
    ]
    res = parse_data(raw_data)
    assert res == exp
