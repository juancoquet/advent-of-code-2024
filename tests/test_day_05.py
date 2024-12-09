from advent_of_code.day_05.solution import InstructionSet, Rule, parse_data, part_1, part_2


def test_part_1():
    rules, instructions = get_test_data()
    exp = 143
    res = part_1(rules, instructions)
    assert res == exp


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


def get_test_data() -> tuple[list[Rule], list[InstructionSet]]:
    rules = [
        Rule(x=47, y=53),
        Rule(x=97, y=13),
        Rule(x=97, y=61),
        Rule(x=97, y=47),
        Rule(x=75, y=29),
        Rule(x=61, y=13),
        Rule(x=75, y=53),
        Rule(x=29, y=13),
        Rule(x=97, y=29),
        Rule(x=53, y=29),
        Rule(x=61, y=53),
        Rule(x=97, y=53),
        Rule(x=61, y=29),
        Rule(x=47, y=13),
        Rule(x=75, y=47),
        Rule(x=97, y=75),
        Rule(x=47, y=61),
        Rule(x=75, y=61),
        Rule(x=47, y=29),
        Rule(x=75, y=13),
        Rule(x=53, y=13),
    ]
    instructions = [
        InstructionSet([75, 47, 61, 53, 29]),
        InstructionSet([97, 61, 53, 29, 13]),
        InstructionSet([75, 29, 13]),
        InstructionSet([75, 97, 47, 61, 53]),
        InstructionSet([61, 13, 29]),
        InstructionSet([97, 13, 75, 29, 47]),
    ]
    return rules, instructions
