# Credit Default Risk Prediction System (End-to-End ML + MLOps)

An **end-to-end machine learning system** that predicts the probability of loan default using structured financial data.  
The project is designed with **real-world constraints**, **explainability**, and **MLOps best practices** in mind.

> This project intentionally focuses on **production realism**, not Kaggle-only optimizations.

---

## 🎯 Problem Statement

Given a loan application, predict the **probability that a customer will default** on their loan.

This is a **core risk modeling problem** used in:
- Banking
- NBFCs
- Fintech credit platforms

The dataset exhibits **severe class imbalance**, making accuracy an unreliable metric and requiring careful evaluation.

---

## 🧠 Key Objectives

- Build a **realistic credit-risk model** using structured data
- Establish a strong **baseline** and improve it incrementally
- Ensure **explainability** for regulated decision-making
- Track experiments and models using **MLflow**
- Serve predictions via a **FastAPI** inference service
- Design the system with **feature availability and drift monitoring** in mind


---

## 📊 Dataset

**Home Credit Default Risk Dataset**

- `application_train.csv` (primary table)
- One row = one loan application
- Target variable:
  - `TARGET = 1` → Default
  - `TARGET = 0` → No default

Other dataset files (bureau, installments, POS, etc.) contain **historical credit behavior** and are used **offline only**.

---

## 🧠 Feature Governance (Very Important)

Features are explicitly categorized by **availability at inference time**.

### ✅ A. Real-Time Application Features (Used)
Examples:
- Income, credit amount, annuity
- Age, employment duration
- Ownership flags

These are supplied by the client at request time.

---

### ✅ B. Derived Online Features (Used)

Computed **inside the service**, not provided by the client:

- Credit-to-income ratio
- Annuity-to-income ratio
- Age (years)
- Employment duration (years)

> Derived features are computed centrally to ensure **determinism and tamper resistance**.

---

### ❌ C. Historical / Offline Features (Excluded at Inference)

From files such as:
- `bureau.csv`
- `installments_payments.csv`
- `POS_CASH_balance.csv`

These require historical data aggregation and would be served via a **feature store** in production.

> They are intentionally excluded here to avoid leakage and unrealistic assumptions.

---

## 🤖 Models

### Baseline
- **Logistic Regression**
- Class-weighted loss to handle imbalance

### Final Model
- **XGBoost (Gradient Boosted Trees)**
- Better performance on tabular financial data
- Strong compatibility with SHAP explainability

---

## 📈 Evaluation Metrics

Due to class imbalance, the following metrics are used:

- **ROC-AUC** — ranking quality
- **PR-AUC** — minority-class sensitivity

Accuracy is intentionally **not used** as a primary metric.

---

## 🔍 Explainability (SHAP)

- **Global explanations** identify portfolio-level risk drivers
- **Local explanations** justify individual loan decisions
- SHAP computation and plotting are separated for **compute efficiency**

Explainability artifacts are logged via MLflow.

---

## 🧪 Experiment Tracking (MLOps)

- All models are tracked using **MLflow**
- Logged artifacts include:
  - Parameters
  - Metrics
  - Full preprocessing + model pipelines
- Enables reproducibility and safe iteration

---

## 🚀 Model Serving

- Model is served via **FastAPI**
- Preprocessing and derived features are applied at inference
- SHAP is intentionally excluded from real-time serving to reduce latency

Example endpoint:

# POST /predict

Returns:
- Default probability
- Risk label (HIGH / LOW)

---

## 📉 Monitoring & Drift Detection

- Implemented lightweight **Population Stability Index (PSI)** checks
- Designed to detect drift in key numeric and derived features
- In production, these checks would run on a **scheduled basis** (cron / Airflow)

---

## 🧠 Design Philosophy

This project prioritizes:
- Production realism
- Explainability
- Feature availability constraints
- Incremental model improvement

Over:
- Kaggle-only optimizations
- Unrealistic feature joins
- One-off scripts

---

## 📌 Future Extensions

- Add aggregated historical features via a feature store
- Probability calibration (Platt / Isotonic)
- Automated retraining triggers
- Model registry–based promotion

---

## 🧑‍💼 Author

Built as a **ML engineering project** demonstrating:
- Core ML fundamentals
- MLOps thinking
- System design for regulated domains
