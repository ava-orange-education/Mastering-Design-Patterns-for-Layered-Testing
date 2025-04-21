import math
import pytest

def calculate_square_root(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(x)

def test_calculate_square_root_valid_input():
    assert calculate_square_root(4) == 2.0
    assert calculate_square_root(0) == 0.0

def test_calculate_square_root_invalid_input():
    with pytest.raises(ValueError) as excinfo:
        calculate_square_root(-1)
    assert str(excinfo.value) == "Cannot calculate square root of a negative number"