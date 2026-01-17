import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_auc_score, average_precision_score
import mlflow
import mlflow.sklearn

from preprocessing import (
    split_data,
    split_feature_types,
    build_preprocessor
)

DATA_PATH = "data/raw/application_train.csv"

def main():
    mlflow.set_experiment("credit_default_baseline")

    with mlflow.start_run(run_name="logistic_regression_baseline"):
        df = pd.read_csv(DATA_PATH)

        X_train, X_val, y_train, y_val = split_data(df)

        numeric_cols, categorical_cols = split_feature_types(df)

        preprocessor = build_preprocessor(numeric_cols, categorical_cols)

        model = LogisticRegression(
            max_iter=1000,
            class_weight="balanced"
        )

        pipeline = Pipeline(steps=[
            ("preprocessor", preprocessor),
            ("model", model)
        ])

        pipeline.fit(X_train, y_train)

        val_probs = pipeline.predict_proba(X_val)[:, 1]

        roc_auc = roc_auc_score(y_val, val_probs)
        pr_auc = average_precision_score(y_val, val_probs)

         # 🔹 Log params
        mlflow.log_param("model_type", "logistic_regression")
        mlflow.log_param("class_weight", "balanced")
        mlflow.log_param("max_iter", 1000)

        # 🔹 Log metrics
        mlflow.log_metric("roc_auc", roc_auc)
        mlflow.log_metric("pr_auc", pr_auc)

        # 🔹 Log model
        mlflow.sklearn.log_model(
            pipeline,
            artifact_path="model"
        )
        
        print(f"Baseline ROC-AUC: {roc_auc:.4f}")
        print(f"Baseline PR-AUC: {pr_auc:.4f}")

if __name__ == "__main__":
    main()
