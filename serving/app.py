import mlflow
import mlflow.pyfunc
import pandas as pd
import mlflow.sklearn

from fastapi import FastAPI
from serving.schemas import CreditApplication
from serving.feature_template import get_training_columns
from serving.derived_features import add_derived_features


app = FastAPI(
    title="Credit Default Risk API",
    description="Predicts probability of loan default",
    version="1.0"
)

MODEL_NAME = "credit_default_xgboost"
EXPERIMENT_NAME = "credit_default_models"
RUN_NAME = "xgboost_v1"

@app.on_event("startup")
def load_model():
    global model, TRAIN_COLUMNS

    client = mlflow.tracking.MlflowClient()
    experiment = client.get_experiment_by_name(EXPERIMENT_NAME)

    runs = client.search_runs(
        experiment_ids=[experiment.experiment_id],
        filter_string=f"tags.mlflow.runName = '{RUN_NAME}'"
    )

    run_id = runs[0].info.run_id
    model_uri = f"runs:/{run_id}/model"

    model = mlflow.sklearn.load_model(model_uri)

    TRAIN_COLUMNS = get_training_columns()


@app.post("/predict")
def predict(application: CreditApplication):
    input_df = pd.DataFrame([application.dict()])

    full_df = pd.DataFrame(columns=TRAIN_COLUMNS)
    full_df.loc[0] = None

    for col in input_df.columns:
        if col in full_df.columns:
            full_df.at[0, col] = input_df.at[0, col]

    full_df = add_derived_features(full_df)
    
    probs = model.predict_proba(full_df)
    prob = float(probs[0][1])

    return {
        "default_probability": prob,
        "risk_label": "HIGH" if prob >= 0.5 else "LOW"
    }

