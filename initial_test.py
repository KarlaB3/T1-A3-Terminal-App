#test output when users enter a selection on the welcome page
import pytest
from food_diary_main import initial_options, initial_selections

def initial_test_1():
    initial_options()
    initial_selections()
    input = "1"
    assert output == ["Open your diary by entering the diary name: "]

def initial_test_2():
    initial_options()
    initial_selections()
    input = "2"
    assert existing_confirmedoutput == ["Create a new diary. Please enter a diary name that is maximum 6 characters long: "]

def initial_test_3():
    initial_options()
    initial_selections()
    input = "x"
    assert output == ["What you've selected isn't recognised. Please try again."]

