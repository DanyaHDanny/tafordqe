import os
import pandas as pd
from typing import List, Optional

# TODO: not best approach, better to read directly using Pandas, where partation = column
class ParquetReader:
    """
    A class to read data from Parquet files stored in folders with the same structure
    into Pandas DataFrames.
    """

    def __init__(self, folder_path: Optional[str] = None, file_extension: str = ".parquet"):
        """
        Initialize the ParquetReader.

        :param folder_path: The root folder path containing Parquet files. Can be set later using the `process` method.
        :param file_extension: The file extension for Parquet files (default is ".parquet").
        """
        self.folder_path = folder_path
        self.file_extension = file_extension

    def set_folder_path(self, folder_path: str):
        """
        Set the folder path for the ParquetReader.

        :param folder_path: The root folder path containing Parquet files.
        """
        self.folder_path = folder_path

    def _get_parquet_files(self, folder: str) -> List[str]:
        """
        Get a list of Parquet files in a specific folder.

        :param folder: The folder to search for Parquet files.
        :return: A list of Parquet file paths.
        """
        return [
            os.path.join(folder, file)
            for file in os.listdir(folder)
            if file.endswith(self.file_extension)
        ]

    def read_parquet_file(self, file_path: str, columns: Optional[List[str]] = None) -> pd.DataFrame:
        """
        Read a single Parquet file into a Pandas DataFrame.

        :param file_path: The path to the Parquet file.
        :param columns: Optional list of columns to read from the file.
        :return: A Pandas DataFrame containing the data.
        """
        try:
            return pd.read_parquet(file_path, columns=columns)
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
            return pd.DataFrame()

    def read_folder(self, columns: Optional[List[str]] = None) -> pd.DataFrame:
        """
        Read all Parquet files in the root folder into a single Pandas DataFrame.

        :param columns: Optional list of columns to read from the files.
        :return: A Pandas DataFrame containing the combined data from all files in the folder.
        """
        if not self.folder_path:
            raise ValueError("Folder path is not set. Use the `process` method or set `folder_path` directly.")

        all_files = self._get_parquet_files(self.folder_path)
        dataframes = []

        for file_path in all_files:
            df = self.read_parquet_file(file_path, columns=columns)
            if not df.empty:
                dataframes.append(df)

        if dataframes:
            return pd.concat(dataframes, ignore_index=True)
        else:
            return pd.DataFrame()

    def read_subfolders(self, columns: Optional[List[str]] = None) -> pd.DataFrame:
        """
        Read all Parquet files from the root folder and its subfolders into a single DataFrame.

        :param columns: Optional list of columns to read from the files.
        :return: A Pandas DataFrame containing the combined data from all files in the folder hierarchy.
        """
        if not self.folder_path:
            raise ValueError("Folder path is not set. Use the `process` method or set `folder_path` directly.")

        dataframes = []

        for root, _, files in os.walk(self.folder_path):
            parquet_files = [os.path.join(root, file) for file in files if file.endswith(self.file_extension)]
            for file_path in parquet_files:
                df = self.read_parquet_file(file_path, columns=columns)
                if not df.empty:
                    dataframes.append(df)

        if dataframes:
            return pd.concat(dataframes, ignore_index=True)
        else:
            return pd.DataFrame()

    def process(self, folder_path: str, columns: Optional[List[str]] = None, include_subfolders: bool = False) -> pd.DataFrame:
        """
        Process Parquet files in the specified folder (and optionally its subfolders) into a Pandas DataFrame.

        :param folder_path: The folder path to process.
        :param columns: Optional list of columns to read from the files.
        :param include_subfolders: Whether to include files in subfolders.
        :return: A Pandas DataFrame containing the combined data from the specified folder.
        """
        self.set_folder_path(folder_path)

        if include_subfolders:
            return self.read_subfolders(columns=columns)
        else:
            return self.read_folder(columns=columns)


# Example usage:
if __name__ == "__main__":
    # Create an instance of ParquetReader without specifying a folder path initially.
    reader = ParquetReader()

    # Process the first folder.
    folder_path_1 = "/parquet_data/facility_name_min_time_spent_per_visit_date"
    df1 = reader.process(folder_path_1, include_subfolders=True)
    print("Data from first folder:")
    print(df1)