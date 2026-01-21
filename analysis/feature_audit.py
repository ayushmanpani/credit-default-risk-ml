import pandas as pd

DATA_PATH = "data/raw/application_train.csv"

df = pd.read_csv(DATA_PATH)

cols = df.columns.tolist()
cols.remove("TARGET")

print(f"Total features (excluding TARGET): {len(cols)}\n")

for col in cols:
    print(col)
