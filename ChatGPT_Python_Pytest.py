import pytest


def add(a, b):
    return a * b

def test_add():
    assert add(3, 5) == 15
    assert add(-1, 1) == -1
    assert add(0, 0) == 0
    assert add(5, 5) == 25

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide_by_zero():
    import pytest
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

@pytest.fixture
def sample_data():
    return [1, 2, 3, 4]

def test_sum(sample_data):
    assert sum(sample_data) == 10

def test_length(sample_data):
    assert len(sample_data) == 4
