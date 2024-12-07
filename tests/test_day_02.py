import pytest

from advent_of_code.day_02.solution import Report, parse_data, part_1


def test_part_1():
    reports = [
        Report([7, 6, 4, 2, 1]),
        Report([1, 2, 7, 8, 9]),
        Report([9, 7, 6, 2, 1]),
        Report([1, 3, 2, 4, 5]),
        Report([8, 6, 4, 4, 1]),
        Report([1, 3, 6, 7, 9]),
    ]
    exp = 2

    res = part_1(reports)
    assert res == exp


def test_report_cannot_be_empty():
    with pytest.raises(ValueError):
        Report([])


def test_is_safe_report_all_safe_ascending_is_true():
    report = Report([1, 2, 4, 7, 10])
    assert report.is_safe()


def test_is_safe_report_all_safe_descending_is_true():
    report = Report([10, 7, 4, 2, 1])
    assert report.is_safe()


def test_is_safe_report_no_ascent_or_descent_is_false():
    report = Report([1, 1, 1])
    assert not report.is_safe()


def test_is_safe_report_safe_ascent_then_safe_descent_is_false():
    report = Report([1, 2, 3, 2, 1])
    assert not report.is_safe()


def test_is_safe_report_safe_descent_then_safe_ascent_is_false():
    report = Report([3, 2, 1, 2, 3])
    assert not report.is_safe()


def test_parse_data():
    raw_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
    exp = [
        Report([7, 6, 4, 2, 1]),
        Report([1, 2, 7, 8, 9]),
        Report([9, 7, 6, 2, 1]),
        Report([1, 3, 2, 4, 5]),
        Report([8, 6, 4, 4, 1]),
        Report([1, 3, 6, 7, 9]),
    ]

    res = parse_data(raw_data)
    assert res == exp
