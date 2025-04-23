from dataclasses import dataclass
from typing import List, Tuple


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
class HDFSConfig:
    """
    A dataclass to store HDFS (Hadoop Distributed File System) configuration settings.

    Attributes:
        host (str): The base URL or hostname of the HDFS NameNode (e.g., "http://localhost:50070").
        user (str): The username to authenticate with HDFS.
        base_path (str): The base directory path in HDFS where data will be stored.
    """
    host: str
    user: str
    base_path: str


# Instance of PostgresConfig
postgres_config = PostgresConfig(
    user='myuser',
    password='mypassword',
    db='mydatabase',
    port=5434,
    host='localhost'
)

# Instance of GeneratorConfig
generator_config = GeneratorConfig(
    num_patients=30,
    start_date='2025-04-01',
    end_date='2025-04-02',
    date_format='%Y-%m-%d',
    facility_types=["Hospital", "Clinic", "Urgent Care", "Specialty Center"],
    visits_per_day=(7, 10)
)

# Instance of HDFSConfig
hdfs_config = HDFSConfig(
    host="http://localhost:50070",
    user="hdfs_user",
    base_path="/data"
)
