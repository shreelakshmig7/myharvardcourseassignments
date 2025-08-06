import pytest
from twttr import shorten

def test_shorten_lower():
    assert shorten("hello") == "hll"
    assert shorten("test") == "tst"
    assert shorten("aeiou") == ""
    assert shorten("fly") == "fly"
    assert shorten("test1") == "tst1"
    assert shorten("test.") == "tst."


def test_shorten_upper():
    assert shorten("hEllO") == "hll"
    assert shorten("tEst") == "tst"
    assert shorten("aeioU") == ""
    assert shorten("FLY") == "FLY"
    assert shorten("TEST1") == "TST1"
    assert shorten("TEST.") == "TST."
