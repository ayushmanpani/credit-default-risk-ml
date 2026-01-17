# evaluation/shap_compute.py
import numpy as np
import pandas as pd
import shap
import mlflow
import mlflow.sklearn

mlflow.set_tracking_uri("http://localhost:5000")

DATA_PATH = "data/raw/application_train.csv"
EXPERIMENT_NAME = "credit_default_models"
RUN_NAME = "xgboost_v1"

SHAP_SAMPLE_SIZE = 2000

OUT_SHAP = "evaluation/shap_values.npy"
OUT_X = "evaluation/X_processed.npy"


def load_pipeline():
    client = mlflow.tracking.MlflowClient()
    experiment = client.get_experiment_by_name(EXPERIMENT_NAME)

    runs = client.search_runs(
        experiment_ids=[experiment.experiment_id],
        filter_string=f"tags.mlflow.runName = '{RUN_NAME}'"
    )

    run_id = runs[0].info.run_id
    model_uri = f"runs:/{run_id}/model"

    return mlflow.sklearn.load_model(model_uri)


def main():
    df = pd.read_csv(DATA_PATH)
    X = df.drop(columns=["TARGET"])

    pipeline = load_pipeline()
    preprocessor = pipeline.named_steps["preprocessor"]
    model = pipeline.named_steps["model"]

    X_sample = X.sample(n=SHAP_SAMPLE_SIZE, random_state=42)
    X_processed = preprocessor.transform(X_sample)

    explainer = shap.TreeExplainer(
        model,
        feature_perturbation="tree_path_dependent"
    )

    shap_values = explainer.shap_values(X_processed)

    print("SHAP computed:", shap_values.shape)

    # Persist outputs for plotting
    np.save(OUT_SHAP, shap_values)
    np.save(OUT_X, X_processed)

    with mlflow.start_run(run_name="xgboost_shap_compute"):
        mlflow.log_param("shap_sample_size", SHAP_SAMPLE_SIZE)
        mlflow.log_artifact(OUT_SHAP)
        mlflow.log_artifact(OUT_X)


if __name__ == "__main__":
    main()
