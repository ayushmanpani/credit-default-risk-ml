# evaluation/shap_plot.py
import numpy as np
import shap
import matplotlib.pyplot as plt
import mlflow
import mlflow.sklearn
import pandas as pd

mlflow.set_tracking_uri("http://localhost:5000")

DATA_PATH = "data/raw/application_train.csv"
EXPERIMENT_NAME = "credit_default_models"
RUN_NAME = "xgboost_v1"

SHAP_PATH = "evaluation/shap_values.npy"
X_PATH = "evaluation/X_processed.npy"


def get_feature_names(preprocessor, numeric_cols, categorical_cols):
    num_features = numeric_cols
    cat_encoder = preprocessor.named_transformers_["cat"].named_steps["encoder"]
    cat_features = cat_encoder.get_feature_names_out(categorical_cols)
    return list(num_features) + list(cat_features)


def load_pipeline():
    client = mlflow.tracking.MlflowClient()
    experiment = client.get_experiment_by_name(EXPERIMENT_NAME)
    runs = client.search_runs(
        experiment_ids=[experiment.experiment_id],
        filter_string=f"tags.mlflow.runName = '{RUN_NAME}'"
    )
    run_id = runs[0].info.run_id
    return mlflow.sklearn.load_model(f"runs:/{run_id}/model")


def main():
    # Load SHAP data
    shap_values = np.load(SHAP_PATH)
    X_processed = np.load(X_PATH)

    # Load pipeline to get feature names
    pipeline = load_pipeline()
    preprocessor = pipeline.named_steps["preprocessor"]

    df = pd.read_csv(DATA_PATH)
    X = df.drop(columns=["TARGET"])

    numeric_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_cols = X.select_dtypes(include=["object"]).columns.tolist()

    feature_names = get_feature_names(
        preprocessor,
        numeric_cols,
        categorical_cols
    )

    shap.summary_plot(
        shap_values,
        X_processed,
        feature_names=feature_names,
        max_display=15,
        show=False
    )

    plt.savefig("shap_global_summary.png", dpi=120)
    plt.close()

    print("Saved shap_global_summary.png")


if __name__ == "__main__":
    main()
