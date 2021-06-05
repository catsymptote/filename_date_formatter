from app.add_date import *
from datetime import datetime


def test_get_date():
    date = datetime.now()
    formatted_date = get_date(date)
    date_str = str(date)

    assert type(formatted_date) is str
    assert len(formatted_date) == 12

    assert formatted_date[0] == '['
    assert formatted_date[5] == formatted_date[8] == '-'
    assert formatted_date[-1] == ']'

    assert formatted_date[1:5] == date_str[0:4]
    assert formatted_date[6:8] == date_str[5:7]
    assert formatted_date[9:11] == date_str[8:10]


def test_date_formatter():
    num1 = 1
    num2 = 4
    num3 = 10
    num4 = 27

    assert date_formatter(num1) == "01"
    assert date_formatter(num2) == "04"
    assert date_formatter(num3) == "10"
    assert date_formatter(num4) == "27"
