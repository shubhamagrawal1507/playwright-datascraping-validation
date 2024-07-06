import pandas as pd


def load_expected_data(file_path):
    return pd.read_csv(file_path)


def save_scraped_data(data, file_path):
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)


def load_scraped_data(file_path):
    return pd.read_csv(file_path)
