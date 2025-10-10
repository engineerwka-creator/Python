#test_calculator.py

def add(a, b):
    return a + b

def test_add():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

