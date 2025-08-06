import pytest
from plates import is_valid

def test_valid_len():
    assert is_valid("CS50") == True
    assert is_valid("TEST50") == True
    assert is_valid("TEST501") == False
    assert is_valid("C") == False

def test_valid_apha():
    assert is_valid("CS") == True
    assert is_valid("HELLO") == True
    assert is_valid("HII") == True

def test_valid_num():
    assert is_valid("50") == False
    assert is_valid("123456") == False
    assert is_valid("085") == False

def test_valid_apha_num():
    assert is_valid("CS50") == True
    assert is_valid("HELLO1") == True
    assert is_valid("CS05") == False

def test_valid_apha_num_order():
    assert is_valid("TES5T") == False
    assert is_valid("TEST25") == True
    assert is_valid("SH4358") == True
    assert is_valid("SH5048") == True

def test_valid_punc():
    assert is_valid("HII,CS") == False
