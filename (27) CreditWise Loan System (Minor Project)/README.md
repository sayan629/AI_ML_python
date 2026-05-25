<!-- BANNER -->
<p align="center">
  <img src="banner.svg" alt="CreditWise Loan Approval Predictor" width="100%"/>
</p>

<h1 align="center">CreditWise — Loan Approval Predictor</h1>

<p align="center">
  A machine learning project that predicts whether a loan application should be approved or rejected,<br/>
  comparing three classification algorithms on real-world-style financial data.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat-square&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-Data-150458?style=flat-square&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/Status-Complete-2ecc71?style=flat-square"/>
</p>

---

## Overview

**CreditWise** is my first end-to-end machine learning project. It takes a dataset of 1,000 loan applications — each described by 20 features including income, credit score, DTI ratio, savings, and more — and trains three classifiers to predict loan approval (`Yes` / `No`).

The goal was to build a clean ML pipeline from scratch: loading raw data, handling missing values, encoding categoricals, scaling features, training models, and comparing their performance side by side.

---

## Dataset

| Property | Value |
|---|---|
| Source file | `loan_approval_data.csv` |
| Total records | 1,000 |
| Usable records (after NaN drop) | 950 |
| Features | 20 |
| Target column | `Loan_Approved` |

### Feature Summary

**Numerical:** Applicant Income, Coapplicant Income, Age, Dependents, Credit Score, Existing Loans, DTI Ratio, Savings, Collateral Value, Loan Amount, Loan Term

**Categorical:** Employment Status, Marital Status, Loan Purpose, Property Area, Education Level, Gender, Employer Category

---

## ML Pipeline

```
Raw CSV
  └── Exploratory Data Analysis (shape, info, describe, nulls)
        └── Missing Value Imputation (SimpleImputer — mean / most frequent)
              └── Feature Engineering (DTI_Ratio_sq, Credit_Score_sq)
                    └── Encoding (LabelEncoder + OneHotEncoder)
                          └── Train / Test Split (80 / 20)
                                └── Standard Scaling (StandardScaler)
                                      └── Model Training & Evaluation
```

---

## Models & Results

Three classifiers were trained and evaluated on the same test set:

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---|---|---|---|
| Logistic Regression | 87.5% | 79.0% | 80.3% | 79.7% |
| **Naive Bayes** | **86.5%** | **78.3%** | **77.0%** | **77.7%** |
| K-Nearest Neighbours (k=5) | 75.5% | 62.0% | 50.8% | 55.9% |

> **Best Model: Naive Bayes** — chosen for its strong precision, meaning fewer false approvals. In a loan approval context, minimising false positives (approving risky applicants) is critical, making Naive Bayes the most reliable choice.

### Confusion Matrix Snapshot (Logistic Regression)

```
                Predicted No   Predicted Yes
Actual No           126             13
Actual Yes           12             49
```

---

## Tech Stack

- **Python 3.13**
- **Pandas** — data loading & manipulation
- **NumPy** — numerical operations
- **Matplotlib / Seaborn** — data visualisation
- **scikit-learn** — full ML pipeline (imputation, encoding, scaling, models, metrics)

---

## Project Structure

```
creditwise-loan-approval/
│
├── creditwise_loan.ipynb       # Main notebook (EDA → modelling → evaluation)
├── loan_approval_data.csv      # Dataset
└── README.md                   # You are here
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/sayan629/creditwise-loan-approval.git
cd creditwise-loan-approval
```

### 2. Install dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

### 3. Launch the notebook

```bash
jupyter notebook creditwise_loan.ipynb
```

---

## Key Learnings

This being my first ML project, here's what I practised hands-on:

- Handling real-world messy data (missing values across all 20 columns)
- The difference between label encoding and one-hot encoding — and when to use each
- Why feature scaling matters for distance-based models like KNN
- Feature engineering: creating polynomial features (`DTI_Ratio_sq`, `Credit_Score_sq`) to help linear models capture non-linearity
- Reading and interpreting a confusion matrix beyond just accuracy

---

## Future Improvements

- [ ] Try ensemble methods (Random Forest, XGBoost)
- [ ] Hyperparameter tuning with GridSearchCV
- [ ] Add ROC-AUC curve comparison
- [ ] Deploy a simple prediction form using Streamlit

---

## Author

Made with curiosity by **Sayan** — feel free to connect on [LinkedIn](https://www.linkedin.com/in/sayanpal04) or check out my other projects.

---

<p align="center">
  <sub>First ML project · Built with Python & scikit-learn</sub>
</p>
