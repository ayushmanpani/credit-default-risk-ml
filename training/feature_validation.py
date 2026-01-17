from feature_filtering import filter_leakage_columns
from feature_groups import FEATURE_GROUPS

def validate_feature_coverage(all_columns, target_col="TARGET"):
    # Remove target
    usable_cols = [c for c in all_columns if c != target_col]

    # Remove leakage columns
    safe_cols, removed_cols = filter_leakage_columns(usable_cols)

    # Flatten grouped features
    grouped_cols = set()
    for cols in FEATURE_GROUPS.values():
        grouped_cols.update(cols)

    # Identify ungrouped columns
    ungrouped = set(safe_cols) - grouped_cols

    return {
        "total_columns": len(all_columns),
        "usable_columns": len(safe_cols),
        "leakage_removed": removed_cols,
        "ungrouped_columns": sorted(list(ungrouped))
    }
