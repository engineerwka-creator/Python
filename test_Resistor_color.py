import pytest
import Resistor_color

def test_Resistor_color():
    color_value = Resistor_color.get_color_value("grey")
    assert color_value == 8

def test_resistor_color_dict():
    color_value = Resistor_color.get_color_value_dict("grey")
    assert color_value == 8
