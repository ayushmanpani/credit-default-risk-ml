from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any
import joblib
import pandas as pd
import json

app = FastAPI(title="Credit Default Risk API")

# Load model
model = joblib.load("model/credit_pipeline.pkl")

# Load feature names
with open("model/feature_names.json") as f:
    FEATURE_NAMES = json.load(f)

class CreditApplication(BaseModel):
    data: Dict[str, Any]

@app.get("/")
def health():
    return {"status": "running"}

@app.post("/predict")
def predict(application: CreditApplication):
    input_data = application.data

    # Check for missing features
    missing = [f for f in FEATURE_NAMES if f not in input_data]
    if missing:
        return {"error": f"Missing features: {missing}"}

    # Keep only expected columns
    filtered_input = {k: input_data[k] for k in FEATURE_NAMES}

    df = pd.DataFrame([filtered_input])

    proba = model.predict_proba(df)[0][1]

    return {
        "default_probability": float(proba),
        "risk_label": "HIGH" if proba > 0.5 else "LOW"
    }

@app.get("/model-info")
def model_info():
    return {
        "model_type": type(model).__name__,
        "feature_count": len(FEATURE_NAMES)
    }
