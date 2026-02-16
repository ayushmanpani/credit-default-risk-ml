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
👉 https://your-render-url.onrender.com/docs  

**Base URL:**  
👉 https://your-render-url.onrender.com  

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

\section*{Additional Endpoint}

\subsection*{GET /model-info}

Returns metadata about the deployed model.

\begin{verbatim}
{
  "model_type": "Pipeline",
  "feature_count": 85
}
\end{verbatim}

This endpoint exposes basic model information without revealing internal artifacts.

---

\section*{Model Performance}

\begin{tabular}{|c|c|}
\hline
Metric & Value \\
\hline
ROC-AUC & 0.76 \\
PR-AUC & 0.25 \\
\hline
\end{tabular}

\vspace{0.5cm}

Application-time deployable model:

\begin{itemize}
\item ROC-AUC $\approx$ 0.69
\item PR-AUC $\approx$ 0.17
\end{itemize}

---

\section*{Experiment Tracking (MLOps)}

\begin{itemize}
\item All experiments tracked using MLflow
\item Logged artifacts:
  \begin{itemize}
  \item Parameters
  \item Metrics
  \item Full preprocessing + model pipeline
  \end{itemize}
\item Enables reproducibility and controlled iteration
\end{itemize}

---

\section*{Monitoring \& Drift Detection}

\begin{itemize}
\item Implemented Population Stability Index (PSI) checks
\item Designed for scheduled execution (cron / Airflow)
\item Supports feature drift and data drift detection
\end{itemize}

---

\section*{Local Development}

\begin{verbatim}
cd inference
pip install -r requirements.txt
uvicorn app:app --reload
\end{verbatim}

Swagger UI will be available at:

\begin{verbatim}
http://127.0.0.1:8000/docs
\end{verbatim}

---

\section*{Continuous Deployment}

This project is deployed on Render.

Whenever changes are pushed:

\begin{verbatim}
git add .
git commit -m "Update inference API"
git push
\end{verbatim}

Render automatically:

\begin{itemize}
\item Pulls latest code
\item Rebuilds environment
\item Restarts the service
\end{itemize}

---

\section*{Production Endpoints Summary}

\subsection*{POST /predict}

Returns:

\begin{verbatim}
{
  "default_probability": 0.65,
  "risk_label": "HIGH"
}
\end{verbatim}

\subsection*{GET /model-info}

Returns model metadata.

\subsection*{GET /health}

Returns service status.

---

\section*{Design Philosophy}

This project prioritizes:

\begin{itemize}
\item Feature availability realism
\item Explicit dependency analysis
\item Explainability in regulated domains
\item Incremental, measurable improvements
\item Production-ready deployment
\end{itemize}

Over:

\begin{itemize}
\item Blind metric maximization
\item Unrealistic feature assumptions
\item One-off experimentation scripts
\end{itemize}

---

\section*{Author}

Built as a machine learning engineering project demonstrating:

\begin{itemize}
\item Core ML fundamentals
\item Feature governance
\item MLOps thinking
\item System design for real-world credit risk
\item Production inference deployment
\end{itemize}

