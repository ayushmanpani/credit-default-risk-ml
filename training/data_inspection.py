import pandas as pd

DATA_PATH = "data/raw/application_train.csv"

df = pd.read_csv(DATA_PATH)

print("Shape:", df.shape)
#print("\nColumns:\n", df.columns.tolist())
#print("\nTarget distribution:")  
#print(df["TARGET"].value_counts(normalize=True)) #0- 92%  1- 8%. severe classs imbalance.

# Missing values
#missing = df.isna().mean().sort_values(ascending=False) 
#print("\nTop 15 columns with missing values:")
#print(missing.head(15))  #upto 69% missing rates, very high

# Basic statistics
#print("\nBasic numeric stats:")
#print(df.describe().T.head(10)) #features have a wide range. no obvious corruption.

from feature_validation import validate_feature_coverage

result = validate_feature_coverage(df.columns.tolist())

print("\nLeakage-removed columns:")
print(result["leakage_removed"][:10])

print("\nUngrouped (but usable) columns:")
print(result["ungrouped_columns"][:30])
print(f"Total ungrouped: {len(result['ungrouped_columns'])}")
