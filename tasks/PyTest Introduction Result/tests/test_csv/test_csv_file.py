import pytest
import re


def test_file_not_empty(read_csv_file):
    path_to_file = "src/data/data.csv"
    df = read_csv_file(path_to_file)
    assert not df.empty, "The CSV file is empty!"


@pytest.mark.validate_csv
@pytest.mark.xfail
def test_duplicates(read_csv_file):
    path_to_file = "src/data/data.csv"
    df = read_csv_file(path_to_file)
    assert df.duplicated().sum() == 0, "CSV file contains duplicate rows"


@pytest.mark.validate_csv
def test_validate_schema(read_csv_file, validate_schema):
    path_to_file = "src/data/data.csv"
    df = read_csv_file(path_to_file)
    expected_schema = ["id", "name", "age", "email", "is_active"]
    assert validate_schema(list(df.columns), expected_schema), "Schema validation failed"


@pytest.mark.validate_csv
@pytest.mark.skip
def test_age_column_valid(read_csv_file):
    path_to_file = "src/data/data.csv"
    df = read_csv_file(path_to_file)
    assert df['age'].between(0, 100).all(), "Age column contains invalid values"


@pytest.mark.validate_csv
def test_email_column_valid(read_csv_file):
    path_to_file = "src/data/data.csv"
    df = read_csv_file(path_to_file)
    email_regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    assert df['email'].apply(
        lambda x: bool(re.match(email_regex, str(x)))).all(), "Email column contains invalid email addresses"


@pytest.mark.parametrize("id, is_active", [
    (1, False),
    (2, True)
])
def test_active_players(read_csv_file, id, is_active):
    path_to_file = "src/data/data.csv"
    df = read_csv_file(path_to_file)
    player_row = df[df['id'] == id]
    actual_is_active = player_row['is_active'].iloc[0]
    assert actual_is_active == is_active, f"Expected is_active = {is_active} for id = {id}, but got {actual_is_active}"


def test_active_player(read_csv_file):
    id = 2
    is_active = False
    path_to_file = "src/data/data.csv"
    df = read_csv_file(path_to_file)
    player_row = df[df['id'] == id]
    actual_is_active = player_row['is_active'].iloc[0]
    assert actual_is_active == is_active, f"Expected is_active = {is_active} for id = {id}, but got {actual_is_active}"
