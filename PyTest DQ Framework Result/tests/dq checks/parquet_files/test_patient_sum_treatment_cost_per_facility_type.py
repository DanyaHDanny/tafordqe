"""
Description: Data Quality checks ...
Requirement(s): TICKET-1234
Author(s): Name Surname
"""

import pytest


@pytest.fixture(scope='module')
def target_data(db_connection):
    target_query = """
    SELECT
        f.facility_type,
        CONCAT(p.first_name, ' ', p.last_name) AS full_name,
        SUM(v.treatment_cost) AS sum_treatment_cost
    FROM
        visits v
    JOIN facilities f 
        ON f.id = v.facility_id
    JOIN patients p
        ON p.id = v.patient_id
    GROUP BY
        f.facility_type,
        full_name; 
    """
    target_data = db_connection.get_data_sql(target_query)
    return target_data


@pytest.fixture(scope='module')
def source_data(parquet_reader):
    target_path = '/parquet_data/patient_sum_treatment_cost_per_facility_type'
    target_data = parquet_reader.process(target_path, include_subfolders=True)
    return target_data


@pytest.mark.example
def test_check_dataset_is_not_empty(target_data, data_quality_library):
    data_quality_library.check_dataset_is_not_empty(target_data)


@pytest.mark.example
def test_check_dataset_is_empty(target_data, data_quality_library):
    data_quality_library.check_dataset_is_empty(target_data)


@pytest.mark.example
def test_check_data_completeness(source_data, target_data, data_quality_library):
    data_quality_library.check_data_completeness(source_data, target_data)


@pytest.mark.example
def test_check_count(source_data, target_data, data_quality_library):
    data_quality_library.check_count(source_data, target_data)


@pytest.mark.example
def test_check_uniqueness(target_data, data_quality_library):
    data_quality_library.check_duplicates(target_data)


@pytest.mark.example
def test_check_not_null_values(target_data, data_quality_library):
    data_quality_library.check_not_null_values(target_data, ['facility_name',
                                                             'visit_date',
                                                             'min_time_spent'])
