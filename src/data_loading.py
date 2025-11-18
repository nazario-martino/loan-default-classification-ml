import os
import pandas as pd

def load_data(raw_data_path="data/raw/",file_name="application_train.csv"):
    """
    Load the specified dataset from the specified raw data directory.

    Parameters
    ----------
    raw_data_path : str
        Path to the folder containing the raw CSV files.
    file_name : str
        Name of the CSV file to load.

    Returns
    -------
    pd.DataFrame
        The specified dataframe.
    """

    file_path = os.path.join(raw_data_path, file_name)

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"File not found: {file_path}.\n"
            "Make sure you downloaded the dataset and placed all CSV files in data/raw/"
        )

    df = pd.read_csv(file_path)
    print("Data loaded successfully from: ", file_path)
    print(df.head())

    return df