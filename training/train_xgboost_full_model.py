import pandas as pd
import mlflow
import mlflow.sklearn

from xgboost import XGBClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_auc_score, average_precision_score

from training.preprocessing import (
    split_data,
    split_feature_types,
    build_preprocessor
)

from training.feature_groups import get_feature_set
from serving.derived_features import add_derived_features

DATA_PATH = "data/raw/application_train.csv"

def main():
    mlflow.set_experiment("credit_default_models")

    with mlflow.start_run(run_name="xgboost_full_model"):
        df = pd.read_csv(DATA_PATH)

        # Enable everything except historical tables
        FEATURES = get_feature_set(
            include_reference=True,
            include_external=True
        )

        # Derived features (internal only)
        df = add_derived_features(df)

        X_train, X_val, y_train, y_val = split_data(
            df,
            feature_cols=FEATURES
        )

        numeric_cols, categorical_cols = split_feature_types(
            df,
            feature_cols=FEATURES
        )

        preprocessor = build_preprocessor(numeric_cols, categorical_cols)

        model = XGBClassifier(
            n_estimators=300,
            max_depth=6,
            learning_rate=0.05,
            subsample=0.8,
            colsample_bytree=0.8,
            eval_metric="auc",
            scale_pos_weight=(y_train == 0).sum() / (y_train == 1).sum(),
            random_state=42,
            n_jobs=-1
        )

        pipeline = Pipeline(steps=[
            ("preprocessor", preprocessor),
            ("model", model)
        ])

        pipeline.fit(X_train, y_train)

        val_probs = pipeline.predict_proba(X_val)[:, 1]

        roc_auc = roc_auc_score(y_val, val_probs)
        pr_auc = average_precision_score(y_val, val_probs)

        mlflow.log_param("feature_group", "full_model")
        mlflow.log_metric("roc_auc", roc_auc)
        mlflow.log_metric("pr_auc", pr_auc)

        mlflow.sklearn.log_model(pipeline, artifact_path="model")

        print(f"Full model ROC-AUC: {roc_auc:.4f}")
        print(f"Full model PR-AUC: {pr_auc:.4f}")

if __name__ == "__main__":
    main()
