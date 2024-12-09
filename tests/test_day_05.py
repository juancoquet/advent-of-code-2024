from advent_of_code.day_05.solution import InstructionSet, Rule, parse_data, part_1, part_2


def test_part_1():
    pass


def test_part_2():
    pass


def test_parse_data():
    raw_data = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
    """.strip()

    rules, instructions = parse_data(raw_data)
    assert all(isinstance(r, Rule) for r in rules)
    assert all(isinstance(i, InstructionSet) for i in instructions)
    assert len(rules) == 21
    assert len(instructions) == 6
    assert rules[0].x == 47
    assert rules[0].y == 53
    assert rules[-1].x == 53
    assert rules[-1].y == 13
    assert instructions[0] == [75, 47, 61, 53, 29]
    assert instructions[-1] == [97, 13, 75, 29, 47]
