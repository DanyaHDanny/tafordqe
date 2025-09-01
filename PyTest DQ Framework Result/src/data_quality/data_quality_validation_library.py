import pandas as pd


class DataQualityLibrary:
    """
    A library of static methods for performing data quality checks on pandas DataFrames.

    This class is intended to be used in a PyTest-based testing framework to validate
    the quality of data in DataFrames. Each method performs a specific data quality
    check and uses assertions to ensure that the data meets the expected conditions.
    """

    @staticmethod
    def check_duplicates(df, column_names=None):
        """
        Check for duplicate rows in the DataFrame. If column_names is provided, check for duplicates in those columns.
        """
        duplicates = (
            df[df[column_names].duplicated(keep=False)]
            if column_names
            else df[df.duplicated(keep=False)]
        )
        assert duplicates.empty, f"Duplicates found:\n{duplicates}"

    @staticmethod
    def check_count(df1, df2):
        """
        Check if two DataFrames have the same number of rows.
        """
        count_diff = len(df1) - len(df2)
        assert count_diff == 0, (
            f"Row count mismatch: df1 has {len(df1)} rows, "
            f"df2 has {len(df2)} rows (difference: {count_diff})."
        )

    @staticmethod
    def check_data_completeness(df1, df2):
        """
        Verify that two DataFrames contain the same data (ignoring row order).
        """
        df1_sorted = df1.sort_values(by=df1.columns.tolist()).reset_index(drop=True)
        df2_sorted = df2.sort_values(by=df2.columns.tolist()).reset_index(drop=True)
        df_diff = pd.concat([df1_sorted, df2_sorted]).drop_duplicates(keep=False)
        assert df_diff.empty, f"Data completeness check failed. Differences:\n{df_diff}"

    @staticmethod
    def check_dataset_is_empty(df):
        """
        Check if the DataFrame is empty.
        """
        assert df.empty, f"Dataset is not empty. It contains {df.shape[0]} rows."

    @staticmethod
    def check_dataset_is_not_empty(df):
        """
        Check if the DataFrame is not empty.
        """
        assert not df.empty, "Dataset is empty."

    @staticmethod
    def check_not_null_values(df, column_names=None):
        """
        Check if specified columns in the DataFrame contain null values. If column_names is None, check all columns.
        """
        if column_names is None:
            column_names = df.columns.tolist()

        columns_with_nulls = [col for col in column_names if df[col].isnull().any()]
        assert not columns_with_nulls, (
            f"Null values found in column(s): {', '.join(columns_with_nulls)}"
        )
