import pytest
import Dictionary_set

def test_isIsogram():
    isogram = Dictionary_set.isIsogram ( "kolesław" )
    assert isogram == True


def test_Not_isIsogram():
    isogram = Dictionary_set.isIsogram ( "kolory" )
    assert isogram == F

def test_Isoggram_special_ch():
    isogram = Dictionary_set.isIsogram("six-year-old")
    assert isogram == true