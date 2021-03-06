"""test day 1"""
from src.day1 import (
    get_data,
    count_increases,
    count_increases_by_window,
    count_increases_by_variable_window,
)


def test_get_data():
    expected = [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263,
    ]
    data = get_data("./data/day1_sample.txt")
    assert expected == data


def test_count_increases():
    data = get_data("./data/day1_sample.txt")
    assert count_increases(data) == 7


def test_count_increases_by_window():
    data = get_data("./data/day1_sample.txt")
    assert count_increases_by_window(data) == 5


def test_count_increases_by_variable_window():
    data = get_data("./data/day1_sample.txt")
    assert count_increases_by_variable_window(data, 3) == 5
    assert count_increases_by_variable_window(data, 1) == 7


def test_count_increases2():
    data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263, 264]
    assert count_increases(data) == 8
