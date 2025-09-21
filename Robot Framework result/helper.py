from selenium.webdriver.common.by import By
import pandas as pd
import os


def table_read_data(element):
    """
    Reads a table web element and returns a pandas DataFrame
    keyed by column header.
    """
    columns = element.find_elements(By.CLASS_NAME, "y-column")
    table_dict = {}
    for column in columns:
        header = column.find_element(By.ID, "header").text.strip()
        cells = [
            cell.text.strip()
            for cell in column.find_elements(By.CLASS_NAME, "cell-text")
            if cell.text.strip() != header
        ]
        table_dict[header] = cells
    return pd.DataFrame(table_dict)


def read_parquet_data(folder_path, filter_date=None):
    """
    Reads partitioned parquet dataset from a folder.
    Automatically detects subfolder partitions.
    Optionally filters by visit_date.
    """
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder does not exist: {folder_path}")

    # Pandas can read partitioned Parquet directly
    df = pd.read_parquet(folder_path)
    col = ['partition_date']
    df = df.drop(columns=col)

    if filter_date is not None:
        if "visit_date" not in df.columns:
            raise ValueError("visit_date column not found in the Parquet data")
        df = df[df["visit_date"] >= filter_date]

    return df


def compare_dataframes(df1, df2):
    """
    Compare DataFrames by values. Returns (match_bool, differences_as_string)
    """
    df1 = df1.sort_values(by=df1.columns.tolist()).reset_index(drop=True)
    df2 = df2.sort_values(by=df2.columns.tolist()).reset_index(drop=True)
    try:
        df1.equals(df2)
        return True, ""
    except AssertionError as e:
        # Differences will be described in the AssertionError message
        return False, str(e)