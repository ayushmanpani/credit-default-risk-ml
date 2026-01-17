import pandas as pd
import numpy as np

def add_derived_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["CREDIT_INCOME_RATIO"] = (
        df["AMT_CREDIT"] / df["AMT_INCOME_TOTAL"]
    )

    df["ANNUITY_INCOME_RATIO"] = (
        df["AMT_ANNUITY"] / df["AMT_INCOME_TOTAL"]
    )

    df["AGE_YEARS"] = -df["DAYS_BIRTH"] / 365

    df["EMPLOYMENT_YEARS"] = np.where(
        df["DAYS_EMPLOYED"] < 0,
        -df["DAYS_EMPLOYED"] / 365,
        np.nan
    )

    return df
