LEAKAGE_KEYWORDS = [
    "PAYMENT",
    "TERMINATION",
    "UPDATED",
    "INSTALLMENT"
]

def filter_leakage_columns(columns):
    safe_cols = []
    removed_cols = []

    for col in columns:
        if any(key in col.upper() for key in LEAKAGE_KEYWORDS):
            removed_cols.append(col)
        else:
            safe_cols.append(col)

    return safe_cols, removed_cols
