# Testing expected data in .csv diary file using a test file 'test_diary.csv'
import pytest
import pandas as pd
import datatest as dt

@pytest.fixture(scope='module')
@dt.working_directory(__file__)
def df():
    return pd.read_csv('test_diary.csv')

# Test to validate expected columns in diary .csv file
def test_columns(df):
    dt.validate(df.columns, {'date', 'breakfast', 'lunch', 'dinner', 'snack'})

