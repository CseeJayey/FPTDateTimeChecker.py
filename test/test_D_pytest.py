import pytest
from app.DTCLib import days_in_month, is_valid_date

def test_days_in_month_valid_input():
    assert days_in_month(2023, 9) == 30
    assert days_in_month(1960, 1) == 31

def test_days_in_month_valid_input_leapyear():
    assert days_in_month(2020, 2) == 29
    assert days_in_month(2000, 2) == 29

def test_days_in_month_valid_input_nonleapyear():
    assert days_in_month(2022, 2) == 28
    assert days_in_month(1500, 2) == 28

def test_days_in_month_invalid_input_month():
    with pytest.raises(ValueError):
        days_in_month(2023, 0)
    with pytest.raises(ValueError):
        days_in_month(2023, 13)

def test_is_valid_date_valid_date():
    assert is_valid_date(2023, 9, 19)
    assert is_valid_date(2020, 2, 29)

def test_is_valid_date_invalid_date():
    assert not is_valid_date(2023, 2, 30)
    assert not is_valid_date(2023, -1, 0)

def test_is_valid_date_out_of_range_year():
    assert not is_valid_date(10000, 9, 19)
    assert not is_valid_date(-10000, 9, 19)

def test_is_valid_date_out_of_range_month():
    assert not is_valid_date(2023, 13, 19)
    assert not is_valid_date(2023, 0, 19)

def test_is_valid_date_out_of_range_day():
    assert not is_valid_date(2023, 9, 32)
    assert not is_valid_date(2023, 9, 0)

def test_is_valid_date_valid_leapyear():
    assert is_valid_date(2000, 2, 29)

def test_is_valid_date_invalid_leapyear():
    assert not is_valid_date(2023, 2, 29)

def test_is_valid_date_non_numeric_input():
    with pytest.raises(ValueError):
        is_valid_date("2032a", "9", "19")
