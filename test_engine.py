from pytest import mark


@mark.smoke
@mark.engine
def test_engine():
    assert True
