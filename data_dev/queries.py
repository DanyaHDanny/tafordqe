# SRC LAYER


CREATE_SRC_GENERATED_FACILITIES_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS src_generated_facilities (
    facility_id SERIAL PRIMARY KEY, -- Auto-incrementing primary key
    facility_name VARCHAR(100) NOT NULL, -- Name of the facility
    facility_type VARCHAR(50) NOT NULL, -- Type of the facility (e.g., Hospital, Clinic)
    address TEXT NOT NULL, -- Address of the facility
    city VARCHAR(50) NOT NULL, -- City where the facility is located
    state VARCHAR(50) NOT NULL -- State where the facility is located
);
"""

CREATE_SRC_GENERATED_PATIENTS_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS src_generated_patients (
    patient_id SERIAL PRIMARY KEY, -- Auto-incrementing primary key
    first_name VARCHAR(50) NOT NULL, -- First name of the patient
    last_name VARCHAR(50) NOT NULL, -- Last name of the patient
    date_of_birth DATE NOT NULL, -- Date of birth of the patient
    address TEXT NOT NULL -- Address of the patient
);
"""

CREATE_SRC_GENERATED_VISITS_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS src_generated_visits (
    patient_id INT NOT NULL, -- Foreign key referencing the patients table
    facility_id INT NOT NULL, -- Foreign key referencing the facilities table
    date DATE NOT NULL, -- Date of the visit
    treatment_cost NUMERIC(10, 2) NOT NULL, -- Cost of the treatment
    duration_minutes INT NOT NULL -- Duration of the visit in minutes
);
"""

INSERT_SRC_GENERATED_FACILITIES_QUERY = """
INSERT INTO src_generated_facilities (facility_id, facility_name, facility_type, address, city, state)
VALUES (%(facility_id)s, %(facility_name)s, %(facility_type)s, %(address)s, %(city)s, %(state)s)
"""

INSERT_SRC_GENERATED_PATIENTS_QUERY = """
INSERT INTO src_generated_patients (patient_id, first_name, last_name, date_of_birth, address)
VALUES (%(patient_id)s, %(first_name)s, %(last_name)s, %(date_of_birth)s, %(address)s)
"""

INSERT_SRC_GENERATED_VISITS_QUERY = """
INSERT INTO src_generated_visits (patient_id, facility_id, date, treatment_cost, duration_minutes)
VALUES (%(patient_id)s, %(facility_id)s, %(date)s, %(treatment_cost)s, %(duration_minutes)s)
"""

# 3NF LAYER


INSERT_FACILITIES_QUERY = """
INSERT INTO facilities (facility_name, facility_type, address, city, state)
VALUES (%(last_run)s, %(last_run)s, %(last_run)s, %(last_run)s, %(last_run)s)
ON DUPLICATE KEY UPDATE
   facility_name = VALUES(facility_name),
   facility_type = VALUES(facility_type),
   address = VALUES(address),
   city = VALUES(city),
   state = VALUES(state);
"""

CREATE_GENERATED_PATIENTS_TABLE_QUERY123 = """
CREATE TABLE IF NOT EXISTS generated_patients (
    patient_id SERIAL PRIMARY KEY, -- Auto-incrementing primary key
    first_name VARCHAR(50) NOT NULL, -- First name of the patient
    last_name VARCHAR(50) NOT NULL, -- Last name of the patient
    date_of_birth DATE NOT NULL, -- Date of birth of the patient
    address TEXT NOT NULL -- Address of the patient
);
"""

CREATE_GENERATED_FACILITIES_TABLE_QUERY123 = """
CREATE TABLE IF NOT EXISTS generated_facilities (
    facility_id SERIAL PRIMARY KEY, -- Auto-incrementing primary key
    facility_name VARCHAR(100) NOT NULL, -- Name of the facility
    facility_type VARCHAR(50) NOT NULL, -- Type of the facility (e.g., Hospital, Clinic)
    address TEXT NOT NULL, -- Address of the facility
    city VARCHAR(50) NOT NULL, -- City where the facility is located
    state VARCHAR(50) NOT NULL -- State where the facility is located
);
"""

CREATE_GENERATED_VISITS_TABLE_QUERY123 = """
CREATE TABLE IF NOT EXISTS generated_visits (
    visit_id SERIAL PRIMARY KEY, -- Auto-incrementing primary key
    patient_id INT NOT NULL, -- Foreign key referencing the patients table
    facility_id INT NOT NULL, -- Foreign key referencing the facilities table
    time_id DATE NOT NULL, -- Date of the visit
    visit_reason VARCHAR(50) NOT NULL, -- Reason for the visit
    treatment_cost NUMERIC(10, 2) NOT NULL, -- Cost of the treatment
    duration_minutes INT NOT NULL, -- Duration of the visit in minutes
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (facility_id) REFERENCES facilities(facility_id) ON DELETE CASCADE
);
"""
