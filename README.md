# Credit Default Risk Prediction System (End-to-End ML + MLOps)

An **end-to-end machine learning system** that predicts the probability of loan default using structured financial data.
The project is designed with **real-world constraints**, **feature availability governance**, **explainability**, and **MLOps best practices**.

> This project intentionally prioritizes **production realism and system design** over Kaggle-only optimizations.

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
- Explicitly govern **which features are available at inference**
- Study **model dependence on external credit signals**
- Ensure **explainability** for regulated decision-making
- Track experiments and models using **MLflow**
- Serve predictions via a **FastAPI** inference service
- Design the system with **drift monitoring and retraining readiness**

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

## 🧠 Feature Governance (Core Design Principle)

Features are **explicitly categorized** by availability and origin.

### ✅ A. Application-Time Features (Used)

- Client-provided:
  - Income, credit amount, family status, education, housing
  - Contact and document flags
- Internal system:
  - Annuity, application timing, organization type
- Static third-party reference:
  - Region ratings
  - Housing and property attributes

These features are assumed to be **available at underwriting time**, either directly from the applicant or resolved upstream.

---

### ✅ B. Derived Online Features (Internal Only)

Computed **inside the service**, never provided by the client:

- Credit-to-income ratio
- Annuity-to-income ratio
- Income per household member
- Employment-to-age ratio

> Derived features are computed centrally to ensure **determinism and tamper resistance**.

---

### ❌ C. Historical / Post-Decision Features (Excluded)

From files such as:
- `bureau.csv`
- `installments_payments.csv`
- `POS_CASH_balance.csv`

These require historical aggregation and would be served via a **feature store** in production.

---

## 🔬 External Credit Signal Ablation (Key Contribution)

To understand **where predictive power comes from**, a structured ablation study was performed.

### Ablation Models

| Model | Features Used | Purpose |
|-----|--------------|--------|
| Application-only | Core + internal + reference | Measures intrinsic application signal |
| External-only | EXT_SOURCE + social-circle aggregates | Measures bureau signal dominance |
| Full model | All above | Measures maximum achievable performance |

### Key Insight

> External credit signals contribute a **majority of predictive power**, while application-time features provide complementary context.

This dependency is **explicitly measured and documented**, rather than hidden.

---

## 🤖 Models

### Baseline
- **Logistic Regression**
- Class-weighted loss to handle imbalance

### Final Model
- **XGBoost (Gradient Boosted Trees)**
- Strong performance on tabular financial data
- Compatible with SHAP-based explainability

---

## 📈 Evaluation Metrics

Due to class imbalance:
- **ROC-AUC** — ranking quality
- **PR-AUC** — minority-class sensitivity

Accuracy is intentionally **not used** as a primary metric.

---

## 🔍 Explainability (SHAP)

- Global explanations identify portfolio-level risk drivers
- Local explanations justify individual loan decisions
- SHAP computation is performed **offline** to avoid inference latency

Artifacts are logged via MLflow.

---

## 🧪 Experiment Tracking (MLOps)

- All experiments tracked using **MLflow**
- Logged artifacts:
  - Parameters
  - Metrics
  - Full preprocessing + model pipeline
- Enables reproducibility and controlled iteration

---

## 🚀 Model Serving

- Model is served via **FastAPI**
- Inference pipeline:
  - Raw features
  - Derived feature layer
  - Trained MLflow model
- The deployed API serves the **full underwriting model**, assuming external credit signals are resolved upstream

**Endpoint**

### POST /predict

Returns:
- Default probability
- Risk label (HIGH / LOW)

---

## 📉 Monitoring & Drift Detection

- Implemented **Population Stability Index (PSI)** checks
- Designed for scheduled execution (cron / Airflow)
- Supports data drift and feature drift detection

---

## 🧠 Design Philosophy

This project prioritizes:
- Feature availability realism
- Explicit dependency analysis
- Explainability in regulated domains
- Incremental, measurable improvements

Over:
- Blind metric maximization
- Unrealistic feature assumptions
- One-off scripts

---

## 📌 Future Extensions

- Feature store integration for historical aggregates
- Probability calibration (Platt / Isotonic)
- Automated retraining triggers
- Model registry–based promotion

---

## 🧑‍💼 Author

Built as a **ML engineering project** demonstrating:
- Core ML fundamentals
- Feature governance
- MLOps thinking
- System design for real-world credit risk
