# Credit Default Risk Prediction System (Production ML + MLOps)

An **end-to-end production-grade machine learning system** that predicts the probability of loan default using structured financial data.

This project emphasizes:

- Feature availability governance  
- Training-serving separation  
- Explainability for regulated domains  
- Experiment tracking and reproducibility  
- Deployable inference architecture  

> This system prioritizes production realism and system design over Kaggle-style optimization.

---

# 🌐 Live Deployment

**Live API (Swagger UI):**  
👉 https://credit-default-risk-ml.onrender.com/docs  

**Base URL:**  
👉 https://credit-default-risk-ml.onrender.com

---

# 🚀 Quick Test (Live API)

## Endpoint

## POST/predict


## Sample Input (All 85 Features)

```json
{
  "data": {
    "NAME_CONTRACT_TYPE": "Cash loans",
    "CODE_GENDER": "M",
    "FLAG_OWN_CAR": "N",
    "FLAG_OWN_REALTY": "Y",
    "CNT_CHILDREN": 0,
    "AMT_INCOME_TOTAL": 200000,
    "AMT_CREDIT": 500000,
    "AMT_GOODS_PRICE": 450000,
    "NAME_TYPE_SUITE": "Unaccompanied",
    "NAME_INCOME_TYPE": "Working",
    "NAME_EDUCATION_TYPE": "Higher education",
    "NAME_FAMILY_STATUS": "Married",
    "NAME_HOUSING_TYPE": "House / apartment",
    "DAYS_BIRTH": -12000,
    "DAYS_EMPLOYED": -2000,
    "OWN_CAR_AGE": 0,
    "FLAG_MOBIL": 1,
    "FLAG_EMP_PHONE": 1,
    "FLAG_WORK_PHONE": 0,
    "FLAG_CONT_MOBILE": 1,
    "FLAG_PHONE": 0,
    "FLAG_EMAIL": 0,
    "OCCUPATION_TYPE": "Laborers",
    "CNT_FAM_MEMBERS": 2,
    "DAYS_LAST_PHONE_CHANGE": -100,
    "AMT_ANNUITY": 25000,
    "WEEKDAY_APPR_PROCESS_START": "MONDAY",
    "HOUR_APPR_PROCESS_START": 10,
    "REG_REGION_NOT_LIVE_REGION": 0,
    "REG_REGION_NOT_WORK_REGION": 0,
    "LIVE_REGION_NOT_WORK_REGION": 0,
    "REG_CITY_NOT_LIVE_CITY": 0,
    "REG_CITY_NOT_WORK_CITY": 0,
    "LIVE_CITY_NOT_WORK_CITY": 0,
    "ORGANIZATION_TYPE": "Business Entity Type 3",
    "REGION_POPULATION_RELATIVE": 0.0188,
    "REGION_RATING_CLIENT": 2,
    "REGION_RATING_CLIENT_W_CITY": 2,
    "APARTMENTS_AVG": 0.092,
    "BASEMENTAREA_AVG": 0.088,
    "YEARS_BEGINEXPLUATATION_AVG": 0.987,
    "YEARS_BUILD_AVG": 0.796,
    "COMMONAREA_AVG": 0.014,
    "ELEVATORS_AVG": 0.08,
    "ENTRANCES_AVG": 0.069,
    "FLOORSMAX_AVG": 0.1667,
    "FLOORSMIN_AVG": 0.0833,
    "LANDAREA_AVG": 0.036,
    "LIVINGAPARTMENTS_AVG": 0.091,
    "LIVINGAREA_AVG": 0.073,
    "NONLIVINGAPARTMENTS_AVG": 0.0,
    "NONLIVINGAREA_AVG": 0.0,
    "APARTMENTS_MODE": 0.092,
    "BASEMENTAREA_MODE": 0.088,
    "YEARS_BEGINEXPLUATATION_MODE": 0.987,
    "YEARS_BUILD_MODE": 0.796,
    "COMMONAREA_MODE": 0.014,
    "ELEVATORS_MODE": 0.08,
    "ENTRANCES_MODE": 0.069,
    "FLOORSMAX_MODE": 0.1667,
    "FLOORSMIN_MODE": 0.0833,
    "LANDAREA_MODE": 0.036,
    "LIVINGAPARTMENTS_MODE": 0.091,
    "LIVINGAREA_MODE": 0.073,
    "NONLIVINGAPARTMENTS_MODE": 0.0,
    "NONLIVINGAREA_MODE": 0.0,
    "APARTMENTS_MEDI": 0.092,
    "BASEMENTAREA_MEDI": 0.088,
    "YEARS_BEGINEXPLUATATION_MEDI": 0.987,
    "YEARS_BUILD_MEDI": 0.796,
    "COMMONAREA_MEDI": 0.014,
    "ELEVATORS_MEDI": 0.08,
    "ENTRANCES_MEDI": 0.069,
    "FLOORSMAX_MEDI": 0.1667,
    "FLOORSMIN_MEDI": 0.0833,
    "LANDAREA_MEDI": 0.036,
    "LIVINGAPARTMENTS_MEDI": 0.091,
    "LIVINGAREA_MEDI": 0.073,
    "NONLIVINGAPARTMENTS_MEDI": 0.0,
    "NONLIVINGAREA_MEDI": 0.0,
    "FONDKAPREMONT_MODE": "not specified",
    "HOUSETYPE_MODE": "block of flats",
    "TOTALAREA_MODE": 0.05,
    "WALLSMATERIAL_MODE": "Panel",
    "EMERGENCYSTATE_MODE": "No"
  }
}
```

---

## 🔍 Additional Endpoint

### GET `/model-info`

Returns metadata about the deployed model.

**Example response:**

```json
{
  "model_type": "Pipeline",
  "feature_count": 85
}
```
This endpoint exposes basic model information without revealing internal artifacts.

---

## 📊 Model Performance

Due to severe class imbalance, evaluation focuses on ranking and minority-class sensitivity rather than raw accuracy.

| Model Variant                     | ROC-AUC | PR-AUC |
|-----------------------------------|---------|--------|
| Full Model (All Features)        | 0.76    | 0.25   |
| Application-Time Deployable Model| 0.69    | 0.17   |

### Metric Rationale

- **ROC-AUC** — Measures ranking quality across thresholds.
- **PR-AUC** — More informative for imbalanced classification problems.
- **Accuracy** is intentionally not used as a primary metric due to skewed class distribution.

> The deployable application-time model excludes historical bureau signals, resulting in slightly lower performance but realistic inference constraints.

---

## 🧪 Experiment Tracking (MLOps)

- All experiments tracked using **MLflow**
- Logged artifacts:
  - Hyperparameters  
  - Evaluation metrics (ROC-AUC, PR-AUC)  
  - Full preprocessing + model pipeline  
- Enables full reproducibility of training runs  
- Supports structured model comparison and controlled experimentation  
- Provides model versioning and traceability for audit-ready workflows  
- Allows separation of research models and deployable production models  

---

## 📉 Monitoring & Drift Detection

- Implemented **Population Stability Index (PSI)** for feature drift detection  
- Designed to run on scheduled intervals (cron / Airflow-ready structure)  
- Supports detection of:
  - Feature distribution drift  
  - Data distribution shifts  
  - Prediction stability degradation  
- Enables early identification of model performance decay  
- Retraining-ready architecture for production environments  

---

## 🛠 Local Development

Run the API locally:

```bash
cd inference
pip install -r requirements.txt
uvicorn app:app --reload
```

Swagger UI will be available at:
```
http://127.0.0.1:8000/docs
```

---

## 🔄 Continuous Deployment

This project is deployed on Render.

Whenever changes are pushed:
```bash
git add .
git commit -m "Update inference API"
git push
```

Render automatically:
  -Pulls the latest code
  -Rebuilds the environment
  -Restarts the service
No manual redeployment required.

---

## 🚀 Production Endpoints Summary

### POST `/predict`

Generates a default risk prediction based on the full 85-feature input payload.

**Response:**

```json
{
  "default_probability": 0.65,
  "risk_label": "HIGH"
}
```

-`default_probability` → Predicted probability of loan default
-`risk_label` → Binary risk classification (HIGH / LOW) based on threshold

### GET `/model-info`

Returns metadata about the deployed model.

**Response:**

```json
{
  "model_type": "Pipeline",
  "feature_count": 85
}
```

-`model_type` → Type of trained model artifact
-`feature_count` → Number of features expected at inference


### GET `/health`

model_type → Type of trained model artifact

feature_count → Number of features expected at inference

**Response:**

```json
{
  "status": "healthy"
}
```
Indicates that the API service is running and ready to serve predictions.

---

## 🧠 Design Philosophy

This project prioritizes:

- Feature availability realism  
- Explicit dependency analysis  
- Explainability in regulated domains  
- Incremental, measurable improvements  
- Training-serving separation  
- Production-ready deployment  

Over:

- Blind metric maximization  
- Unrealistic feature assumptions  
- One-off experimentation scripts  


---

## 🧑‍💼 Author

Built as a machine learning engineering project demonstrating:

- Core ML fundamentals  
- Feature governance and availability control  
- MLOps thinking and experiment tracking  
- Training-serving separation  
- Explainability for regulated financial systems  
- Production-ready cloud inference deployment  
- Realistic system design for credit risk modeling  



