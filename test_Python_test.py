import pytest
import Python_test


def test_eqilateral():
    triangle_type = Python_test.triangle_type ( 3, 3, 3 )
    assert triangle_type == "Trójkąt Równoboczny"

def test_isosceles():
    triangle_type = Python_test.triangle_type ( 1, 3, 3 )
    assert triangle_type == "Trójkąt Równoramienny"

def test_scalene():
    triangle_type = Python_test.triangle_type ( 1, 2, 3 )
    assert triangle_type == "Trójkąt Różnoboczny"

def test_different():
    triangle_type = Python_test.triangle_type(1, 2, 0)
    assert triangle_type == "To nie trójkąt"
