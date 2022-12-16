import pytest


def test_diary_display_1():
    diary = [{"date": "01-12-22", "breakfast": "eggs", "lunch": "salad", "dinner": "soup", "snack": "fruit"}]
    assert diary == ["01-12-22, eggs, salad, soup, fruit"]

def test_diary_display_2():
    diary = [{"date": "01-12-22", "breakfast": "eggs", "lunch": "salad", "dinner": "soup", "snack": "fruit"}]
    assert diary == ["date: 01-12-22, breakfast: eggs, lunch: salad, dinner: soup, snack: fruit"]