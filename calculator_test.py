import pytest
from calculator import sub, mul, div, avg

def test_sub():
    assert sub(5, 2) == 3
    assert sub(2, 5) == -3
    assert sub(0, 0) == 0

def test_mul():
    assert mul(5, 2) == 10
    assert mul(2, 5) == 10
    assert mul(0, 5) == 0

def test_div():
    assert div(5, 2) == 2.5
    assert div(2, 5) == 0.4
    with pytest.raises(ZeroDivisionError):
        div(5, 0)

def test_avg():
    assert avg([1, 2, 3]) == 2
    assert avg([2, 4, 6, 8]) == 5
    assert avg([0, 0, 0, 0]) == 0
