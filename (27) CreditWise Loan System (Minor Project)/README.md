# CreditWise Loan System 💳🤖

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat-square&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-Data-150458?style=flat-square&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/Status-Complete-2ecc71?style=flat-square"/>
</p>

<p align="center">
  Intelligent Machine Learning-based Loan Approval Prediction System
</p>

---
An intelligent Machine Learning-based loan approval prediction system that analyzes applicant data and predicts whether a loan should be approved or not using multiple classification algorithms.

Built as my **first end-to-end Machine Learning project**, this project demonstrates the complete ML workflow — from data preprocessing and EDA to model training, evaluation, and feature engineering.

---

# 🚀 Project Overview

The **CreditWise Loan System** is designed to help financial institutions make smarter and faster loan approval decisions using data-driven insights.

This project focuses on:

- Cleaning and preprocessing real-world financial data
- Handling missing values
- Performing Exploratory Data Analysis (EDA)
- Encoding categorical variables
- Feature scaling
- Training multiple ML models
- Comparing model performance
- Applying feature engineering for improved prediction understanding

---

# 🧠 Machine Learning Workflow

```text
Raw Dataset
    ↓
Data Cleaning
    ↓
Missing Value Handling
    ↓
EDA & Visualization
    ↓
Feature Encoding
    ↓
Correlation Analysis
    ↓
Train-Test Split
    ↓
Feature Scaling
    ↓
Model Training
    ↓
Performance Evaluation
    ↓
Feature Engineering
```

---

# 📊 Exploratory Data Analysis (EDA)

The project includes detailed visual analysis using:

- Pie Charts
- Histograms
- Boxplots
- Correlation Heatmaps
- Distribution Analysis
- Loan Approval Comparisons

## Key insights explored

✔ Loan approval distribution  
✔ Income pattern analysis  
✔ Credit score impact on approval  
✔ Debt-to-income ratio behavior  
✔ Outlier detection using boxplots  
✔ Relationship between applicant features and approval status  

---

# 🛠 Technologies & Libraries Used

## Python Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Jupyter Notebook

---

# ⚙️ Data Preprocessing Techniques

## ✅ Missing Value Handling

Used:

- Mean Imputation for numerical features
- Most Frequent Imputation for categorical features

---

## ✅ Feature Encoding

Implemented:

### Label Encoding
Used for:
- Education_Level
- Loan_Approved

### One-Hot Encoding
Used for:
- Employment_Status
- Marital_Status
- Loan_Purpose
- Property_Area
- Gender

---

## ✅ Feature Scaling

Applied:
- StandardScaler

This ensures all numerical features contribute equally to model learning.

---

# 📈 Models Implemented

## 1️⃣ Logistic Regression

A strong baseline classification model for binary prediction problems.

---

## 2️⃣ K-Nearest Neighbors (KNN)

Distance-based learning algorithm used for classification.

---

## 3️⃣ Gaussian Naive Bayes ⭐

Probabilistic classification model.

### 🏆 Best Performing Model

According to the notebook evaluation, **Naive Bayes achieved the best precision performance** for this dataset.

---

# 🔥 Feature Engineering

Additional engineered features were created for deeper experimentation:

```python
df["DTI_Ratio_sq"] = df["DTI_Ratio"] ** 2
df["Credit_Score_sq"] = df["Credit_Score"] ** 2
```

## Purpose

- Capture non-linear relationships
- Improve model understanding of financial behavior patterns

---

# 📌 Key Learning Outcomes

Through this project, I learned:

- End-to-end ML pipeline creation
- Real-world preprocessing techniques
- Data visualization for business insights
- Feature engineering concepts
- Classification model evaluation
- Model comparison strategies
- Importance of data scaling and encoding

---

# 🌟 Future Improvements

Planned future upgrades:

- Streamlit Web App Deployment
- Interactive Dashboard UI
- Hyperparameter Tuning
- Advanced Ensemble Models
- Real-time Loan Eligibility Prediction
- Model Export using Pickle/Joblib
- Cloud Deployment

---

# 📂 Project Structure

```text
CreditWise-Loan-System/
│
├── creditwise_loan.ipynb
├── loan_approval_data.csv
├── README.md
│
└── future_streamlit_app/
```

---

# 💡 Why This Project Matters

Loan approval systems are critical in the banking and finance sector.

This project demonstrates how Machine Learning can:

- Reduce manual verification effort
- Improve decision consistency
- Identify risky applications faster
- Assist financial institutions with predictive analytics

---

# 📸 Screenshots (Add Later)

You can later add:

- EDA Visualizations
- Heatmaps
- Model Accuracy Outputs
- Streamlit UI Preview

Example:

```md
![EDA](images/eda.png)
```

---

# 🔗 GitHub Repository

[CreditWise Loan System Repository](https://github.com/sayan629/AI_ML_python/tree/main/(27)%20CreditWise%20Loan%20System%20(Minor%20Project))

---

# 👨‍💻 Author

## Sayan

Passionate about:

- Machine Learning
- AI Development
- Data Science
- Real-world ML Applications

## LinkedIn

www.linkedin.com/in/sayanpal04

---

# ⭐ Support

If you like this project:

- Give it a ⭐ on GitHub
- Share feedback
- Connect with me on LinkedIn

---

# 🚀 “Turning Financial Data into Intelligent Decisions with Machine Learning.”
