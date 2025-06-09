import pytest
from app.operations import addition, subtraction, multiplication, division

def test_addition():
    assert addition(2, 3) == 5

def test_subtraction():
    assert subtraction(5, 3) == 2

def test_multiplication():
    assert multiplication(2, 3) == 6

def test_division():
    assert division(6, 3) == 2
   
def test_division_by_zero():
    """Test division by zero."""
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        division(1, 0)
