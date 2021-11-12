import pytest
from functions_to_test import Calculator


def test_add():
    assert Calculator.add(7, 12) == 19
    assert Calculator.add(0.78, 1.52) == 2.3
    with pytest.raises(TypeError):
        Calculator.add('1', 2)


def test_subtract():
    assert Calculator.subtract(8, 7.5) == 0.5
    assert Calculator.subtract(6.4, 2) == 4.4
    with pytest.raises(TypeError):
        Calculator.subtract('1', 2)


def test_multiply():
    assert Calculator.multiply(4, 2) == 8
    assert Calculator.multiply(80, 0.5) == 40
    assert Calculator.multiply('1', 2) == '11'
    with pytest.raises(TypeError):
        Calculator.multiply(None, 2)


def test_divide():
    assert Calculator.divide(36, 6) == 6
    assert Calculator.divide(3, 4) == 0.75
    with pytest.raises(TypeError):
        Calculator.divide('1', 2)
    with pytest.raises(ValueError):
        Calculator.divide(11, 0)
