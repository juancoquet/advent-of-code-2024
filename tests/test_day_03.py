from advent_of_code.day_03.solution import part_1, part_2


def test_part_1():
    instructions = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    exp = 161
    res = part_1(instructions)
    assert res == exp

def test_part_2():
    instructions = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    exp = 48
    res = part_2(instructions)
    assert res == exp
