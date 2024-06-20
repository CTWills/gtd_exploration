"""
This file contains functions that will clean the data used in main
"""
import pandas as pd


def create_date_column(df):
    """
    Creates a 'date' column from the 'iday', 'imonth', and 'iyear' columns
    in the df that is of datetime data type

    Parameters:
        df (pandas.core.frame.DataFrame): The pandas dataframe created by 
                                          reading in the csv

    Returns:
        A 'date' column is of data type datetime. If invalid dates are passed
        then the value for that row will be NaT.
    """
    df.rename(
        columns={"iday": "day", "imonth": "month", "iyear": "year"}, inplace=True)

    return pd.to_datetime(
        df[["year", "month", "day"]], errors="coerce")


if __name__ == "__main__":
    pass
