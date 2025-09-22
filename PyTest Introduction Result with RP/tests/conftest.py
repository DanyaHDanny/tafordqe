import pytest
import pandas as pd


# Fixture to read the CSV file
@pytest.fixture(scope='session')
def read_csv_file():
    def _read_csv_file(path_to_file):
        return pd.read_csv(path_to_file)

    return _read_csv_file


# Fixture to validate the schema of the file
@pytest.fixture(scope='session')
def validate_schema():
    def _validate_schema(actual_schema, expected_schema):
        return actual_schema == expected_schema

    return _validate_schema


# Pytest hook to mark unmarked tests with a custom mark
def pytest_collection_modifyitems(items):
    for item in items:
        if not item.own_markers:
            item.add_marker(pytest.mark.unmarked)
