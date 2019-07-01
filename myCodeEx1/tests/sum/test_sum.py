from pytest import mark

import funcs


@mark.one
def test_sum_one():
    assert funcs.sum_one(5, 5) == 10
    assert funcs.sum_one(5) == 7


@mark.two
def test_sum_two():
    assert funcs.sum_two(1, 2, 3) == 6
