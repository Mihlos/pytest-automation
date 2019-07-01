from pytest import mark

import funcs


@mark.one
def test_product_one():
    assert funcs.prod_one(x=5, y=5) == 25


@mark.two
def test_product_two():
    assert funcs.prod_two(2, 2, 2) == 8
