import pandas as pd

DATA_PATH = "data/raw/application_train.csv"

def get_training_columns():
    df = pd.read_csv(DATA_PATH)
    return df.drop(columns=["TARGET"]).columns.tolist()
