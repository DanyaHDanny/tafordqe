from dataclasses import dataclass
from typing import List, Tuple
from datetime import datetime


@dataclass
class PostgresConfig:
    """
    A dataclass to store PostgreSQL database configuration settings.

    Attributes:
        user (str): The username for the PostgreSQL database.
        password (str): The password for the PostgreSQL database.
        db (str): The name of the database to connect to.
        port (int): The port number on which the PostgreSQL server is running.
        host (str): The hostname or IP address of the PostgreSQL server.
    """
    user: str
    password: str
    db: str
    port: int
    host: str


@dataclass
class GeneratorConfig:
    """
    A dataclass to store configuration settings for a data generation process.

    Attributes:
        num_patients (int): The number of patients to generate data for.
        start_date (str): The start date for the data generation period (formatted as a string).
        end_date (str): The end date for the data generation period (formatted as a string).
        date_format (str): The format of the date strings (e.g., '%Y-%m-%d').
        facility_types (List[str]): A list of facility types (e.g., "Hospital", "Clinic").
        visits_per_day (Tuple[int, int]): A tuple specifying the range (min, max) of visits per day.
    """
    num_patients: int
    start_date: str
    end_date: str
    date_format: str
    facility_types: List[str]
    visits_per_day: Tuple[int, int]


@dataclass
class ParquetStorageConfig:
    """
    Configuration class for Parquet storage.

    This class is used to define the configuration for storing data in Parquet format.

    Attributes:
        storage_path (str): The file system path where Parquet files will be stored.
    """
    storage_path: str


@dataclass
class LoadConfig:
    """
    LoadConfig is a configuration class used to store config related to data loading processes.

    Attributes:
        last_date (str): The last date for which data should be successfully loaded.
                         This is typically used to track the progress of incremental data loads.
                         The date should be in the format 'YYYY-MM-DD'.
    """
    date_scope: str


# Instance of LoadConfig
load_config = LoadConfig(
    date_scope=datetime.now().date().strftime('%Y-%m-%d')  # Example: '2025-01-01'
)

# Instance of PostgresConfig
postgres_config = PostgresConfig(
    user='myuser',
    password='mypassword',
    db='mydatabase',
    port=5432,  # 5434 localhost
    host='postgres'  # localhost
)

# Instance of GeneratorConfig
generator_config = GeneratorConfig(
    num_patients=30,
    start_date='2025-04-01',
    end_date='2025-05-01',
    date_format='%Y-%m-%d',
    facility_types=['Hospital', 'Clinic', 'Urgent Care', 'Specialty Center'],
    visits_per_day=(7, 10)
)

from dataclasses import dataclass

# Instance of ParquetStorageConfig
parquet_storage_config = ParquetStorageConfig(
    storage_path='tmp'
)
