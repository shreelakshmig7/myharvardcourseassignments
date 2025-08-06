import pytest
from bank import value

def test_value_lower():
    assert value("hello") == 0
    assert value("hii") == 20
    assert value("What’s up") == 100

def test_value_upper():
    assert value("Hello") == 0
    assert value("Hii") == 20
    assert value("What’s up") == 100
