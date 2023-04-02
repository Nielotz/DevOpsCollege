import pytest
from calculator import sub, multiply, divide, average

def test_sub():
    assert sub(5, 2) == 3
    assert sub(2, 5) == -3
    assert sub(0, 0) == 0

def test_multiply():
    assert multiply(5, 2) == 10
    assert multiply(2, 5) == 10
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(5, 2) == 2.5
    assert divide(2, 5) == 0.4
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

def test_average():
    assert average([1, 2, 3]) == 2
    assert average([2, 4, 6, 8]) == 5
    assert average([0, 0, 0, 0]) == 0
