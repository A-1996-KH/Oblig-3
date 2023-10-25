# test_is_leap_year.py
from main import is_leap_year

def test_leap_year_divisible_by_4_but_not_by_100():
    assert is_leap_year(2004) == True
    assert is_leap_year(2016) == True
    assert is_leap_year(2020) == False

def test_leap_year_divisible_by_400():
    assert is_leap_year(1600) == True
    assert is_leap_year(2000) == True
    assert is_leap_year(2400) == True

def test_non_leap_year_not_divisible_by_4():
    assert is_leap_year(2003) == False
    assert is_leap_year(2019) == False

def test_non_leap_year_divisible_by_100_but_not_by_400():
    assert is_leap_year(1700) == False
    assert is_leap_year(1800) == False
    assert is_leap_year(1900) == False
    assert is_leap_year(2100) == False