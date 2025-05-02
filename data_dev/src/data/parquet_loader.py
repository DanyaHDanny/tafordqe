from data_dev.queries import TRANSFORM_SQL
from data_dev.config import parquet_storage_config

import os


class LoadParquet:
    """
    A class to handle the process of loading data from a database, transforming it using a SQL query, 
    and saving it as a Parquet file.

    Attributes:
        connection_object: An object representing the database connection. 
                           It must have a `get_data_sql` method to execute SQL queries.
        storage_path: The file path where the Parquet file will be saved. 
                      This is retrieved from the `parquet_storage_config` configuration.
    """

    def __init__(self, connection_object):
        """
        Initializes the LoadParquet class with a database connection object.

        Args:
            connection_object: A database connection object that provides a `get_data_sql` method.
        """
        self.connection_object = connection_object
        self.storage_path = parquet_storage_config.storage_path

    def read_data(self):
        """
        Reads data from the database using the SQL query defined in `TRANSFORM_SQL`.

        Returns:
            pandas.DataFrame: A DataFrame containing the data retrieved from the database.
        """
        df = self.connection_object.get_data_sql(TRANSFORM_SQL)
        return df

    def to_parquet(self):
        """
        Reads data from the database, transforms it using the SQL query, and saves it as a Parquet file.

        The Parquet file is saved to the path specified in `self.storage_path`. The data is partitioned 
        by the 'visit_date' column, and any existing data matching the partition is deleted before saving.

        Raises:
            Exception: If there is an issue with reading data or saving the Parquet file.
        """
        df = self.read_data()
        print(f"Current working directory: {os.getcwd()}")
        os.makedirs(self.storage_path, exist_ok=True)
        df.to_parquet(
            self.storage_path,
            engine='pyarrow',
            partition_cols=['visit_date'],
            index=False,
            existing_data_behavior='delete_matching'
        )
