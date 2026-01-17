import pandas as pd

def get_missing_stats(df):
    missing_ratio = df.isna().mean()
    return missing_ratio.sort_values(ascending=False)

def split_feature_types(df, target_col="TARGET"):
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_cols = df.select_dtypes(include=["object"]).columns.tolist()

    if target_col in numeric_cols:
        numeric_cols.remove(target_col)

    return numeric_cols, categorical_cols

##building the pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

def build_preprocessor(numeric_cols, categorical_cols):
    numeric_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    categorical_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="constant", fill_value="Unknown")),
        ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_pipeline, numeric_cols),
            ("cat", categorical_pipeline, categorical_cols)
        ]
    )

    return preprocessor

from sklearn.model_selection import train_test_split
##perform a stratified split due to severe class imbalance
def split_data(df, target_col="TARGET", test_size=0.2, random_state=42):
    X = df.drop(columns=[target_col])
    y = df[target_col]

    return train_test_split(
        X, y,
        test_size=test_size,
        stratify=y,
        random_state=random_state
    )
