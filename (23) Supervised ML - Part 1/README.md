# 🤖 Supervised Learning (Part 1) — Machine Learning Notes

<div align="center">

![Supervised Learning Banner](https://img.shields.io/badge/Machine%20Learning-Supervised%20Learning-blue?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

```
  ___                                _               _   _               
 / __|_  _ _ __  ___ _ ___ _(_)___ ___ __| | | |_  _ __   _ _ _ _ _  __ _ 
 \__ \ || | '_ \/ -_) '_\ V / (_-</ -_) _` | | | '_/ -_) / _` | ' \/ _` |
 |___/\_,_| .__/\___|_|  \_/|_/__/\___\__,_| |_|_| \___| \__,_|_||_\__, |
           |_|                                                         |___/ 
```

*Comprehensive notes on Supervised Machine Learning — from concepts to code*

</div>

---

## 📚 Table of Contents

- [What is Supervised Learning?](#what-is-supervised-learning)
- [Types of Features](#types-of-features)
- [How It Works](#how-it-works)
- [Types of Problems](#types-of-problems)
- [Scikit-Learn](#scikit-learn)
- [Linear Regression (Deep Dive)](#linear-regression-deep-dive)
- [Cost Function](#cost-function)
- [Mathematical Proof — Three Cases](#mathematical-proof--three-cases)
- [Global Minima & Gradient Descent](#global-minima--gradient-descent)
- [Convergence Theorem & Learning Rate](#convergence-theorem--learning-rate)
- [Evaluation Metrics](#evaluation-metrics)
- [Summary](#summary)

---

## 🎯 What is Supervised Learning?

> Supervised Learning is a type of Machine Learning where the model is **trained on labeled data** — meaning both input features and correct output labels are provided.

```
Input (Features)  ──►  [ ML Model ]  ──►  Output (Prediction)
     X                                          ŷ
```

The model **learns the mapping** from inputs to outputs during training, then uses that learned mapping to predict outputs for new, unseen data.

---

## 🔑 Types of Features

```
                 ┌─────────────────────────────────┐
                 │           FEATURES               │
                 └────────────┬────────────────────┘
                              │
           ┌──────────────────┴──────────────────┐
           ▼                                     ▼
  📥 Independent (Input)              📤 Dependent (Output)
  ─────────────────────              ──────────────────────
  • Study Hours                      • Score / Grade
  • House Size                       • Price
  • Age, Temperature                 • Category
  • AQI, Stock Data                  • Prediction value
```

| Type | Also Called | Role |
|------|-------------|------|
| **Independent** | Input / Predictor / Feature | What we feed into the model |
| **Dependent** | Output / Target / Label | What we want to predict |

---

## ⚙️ How It Works (Step-by-Step)

```
 ┌─────────────────────────────────────────────────────────┐
 │  SUPERVISED LEARNING PIPELINE                           │
 │                                                         │
 │  Raw Data  ──►  Preprocess  ──►  Select Model           │
 │                    +                   │                │
 │              Feature Engg.      Train / Test            │
 │              (Encoding)               │                │
 │                                 Check Fit               │
 │                              (Underfit/Overfit)         │
 └─────────────────────────────────────────────────────────┘
```

| Step | Description |
|------|-------------|
| **① Data Preprocessing + Feature Engineering** | Clean data, handle missing values, encode categorical variables |
| **② Select Model** | Choose algorithm based on problem type (regression/classification) |
| **③ Train / Test Split** | Typically **80% training**, **20% testing** |
| **④ Underfit / Overfit** | Monitor model performance; tune accordingly |

```
Total Data (100%)
    │
    ├── 80% ──► Training Set   ──► Model Learns
    │
    └── 20% ──► Test Set       ──► Evaluate at 80% score → "Now test it!"
```

---

## 📊 Types of Problems

### 1️⃣ Regression — *Output is a Continuous Numerical Value*

```
Score (y)
  │          ●
  │       ●     ●
  │    ●
  │  ●
  └──────────────── Study Hrs (x)

  Best Fit Line:  y = mx + c   (Linear Regression)
```

**Examples:**
- 🌤️ Weather prediction (temperature)
- 🌫️ AQI (Air Quality Index)
- 📈 Stock price prediction
- 🎓 Score prediction
- 🚗 Car price prediction
- 🏠 House price prediction

---

### 2️⃣ Classification — *Output is a Category or Class*

```
Input  ──►  [ Classifier ]  ──►  Class Label
```

**Examples:**
- 📧 Spam / Non-Spam
- 🐱 Cat / Dog / Rabbit
- 🏥 Benign / Malignant tumor

#### How Many Types of Classification?

| Type | Description | Example |
|------|-------------|---------|
| **① Binary Classification** | Only 2 classes | Spam / Not Spam → `{0, 1}` |
| **② Multiclass Classification** | Multiple classes | Cat / Dog / Rabbit |
| **③ Multi-label Classification** | Multiple labels per sample | Movie: Avengers | Labels → `[Action, Adventure, Sci-Fi]` |

```
Binary     ──►  {0, 1}   (2 outputs)
Multiclass ──►  {0, 1, 2, ...}   (n outputs)
Multilabel ──►  {[1,0,1], [0,1,1], ...}  (multiple labels)
```

---

## 🔬 Scikit-Learn

> **Scikit-Learn** (sklearn) is an open-source ML library that supports both **Supervised** and **Unsupervised** Learning.

```python
import sklearn
```

### ✅ Why Use Scikit-Learn?

| Reason | Details |
|--------|---------|
| 📖 Well Documented | Excellent official docs at [scikit-learn.org](https://scikit-learn.org) |
| 🎓 Easy to Learn | Beginner-friendly API |
| 🔗 Works well with NumPy & Pandas | Seamless integration |
| 👥 Professionals & Beginners | Used by both industry experts and students |

### 🧰 Key Algorithms in Scikit-Learn

```
Scikit-Learn Algorithms
│
├── Regression
│   └── Linear Regression
│
├── Classification
│   ├── Logistic Regression
│   ├── K-Nearest Neighbors (KNN)
│   ├── Decision Trees
│   ├── Naive Bayes
│   └── SVM (Support Vector Machine)
│
└── Both (R/C)
    ├── Decision Trees     ──► R/C
    ├── Naive Bayes        ──► C
    └── SVM                ──► R/C
```

---

## 📐 Linear Regression (Deep Dive)

### What is Linear Regression?

Linear Regression models the **relationship between an independent variable (X)** and a **dependent variable (Y)** using a straight line.

```
y = mx + c
```

In Machine Learning notation:

```
hθ(x) = θ₀ + θ₁x₁
         ▲       ▲
       bias   coefficient
     (intercept) (slope)
```

### Generalized Form (Multiple Features)

For `n` features: `x₁, x₂, x₃, ..., xn`

$$h_\theta(x) = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \cdots + \theta_n x_n$$

```
hθ(x) = θ₀ + θ₁x₁ + θ₂x₂ + ... + θₙxₙ
```

Where:
- `θ₀` = Bias / Intercept (1st parameter)
- `θ₁, θ₂, ..., θₙ` = Coefficients (1st, 2nd, ... parameters)
- `x₁, x₂, ..., xₙ` = Input features

### 📊 Example Dataset

| Study Hours (X) | Score (Y) |
|:-:|:-:|
| 1 | 50 |
| 2 | 55 |
| 3 | 65 |
| 4 | 75 |
| 5 | 90 |

```
Score (y)
 90 │                        ●
 75 │                  ●
 65 │            ●     
 55 │      ●                    Best Fit Line ──► y = mx + c
 50 │  ●                        Slope/Coefficient (m)
    └──────────────────────────────
    1    2    3    4    5    x (Study Hrs)
            ▲
        New input (x=2.5) → Predict new output
```

### 🔄 Workflow

```
Train Data ──► Train Model ──► Regressor (Hypothesis) ──► New Output (ŷ)
                                      ▲
                              New Data Input
```

---

## 📉 Cost Function

> The **Cost Function** measures how well the model's predictions match the actual data.

### Error for a Single Point

```
Error = Predicted Value − Actual Value
Errorᵢ = hθ(x⁽ⁱ⁾) − y⁽ⁱ⁾     for the i-th point
```

### Sum of Errors (Problem!)

$$\sum_{i=1}^{m} \left( h_\theta(x^{(i)}) - y^{(i)} \right)$$

⚠️ **Problem:** Sometimes positive + negative errors cancel out → Error = 0 → **Incorrect!**

### Solutions — Multiple Cost Function Options

| Option | Formula |
|--------|---------|
| Absolute Error | `|error|` |
| Squared Error | `error²` |
| Log of Error | `log(error)` |

### ✅ Mean Squared Error (MSE) — Used in Linear Regression

**For Mathematics:**
$$J(\theta) = \frac{1}{m} \sum_{i=1}^{m} \left( h_\theta(x^{(i)}) - y^{(i)} \right)^2$$

**For Machine Learning (with ½ for easy differentiation):**
$$\boxed{J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} \left( h_\theta(x^{(i)}) - y^{(i)} \right)^2}$$

> 💡 **Why divide by 2?** The `½` cancels with the `2` that appears when you take the derivative — making gradient descent calculations cleaner!

```
Error² is always positive ✓
Penalizes large errors more ✓  
Mathematically differentiable ✓
```

### 🔄 Process to Find Best Fit Line

```
Initialize θ₀, θ₁
       │
       ▼
   Calculate J(θ)
       │
       ▼
   Update θ₀, θ₁
       │
       ▼
   Check J(θ) ↓↓
       │
       ▼
   Update θ₀, θ₁
       │
       ⋮
       ▼
   Get BEST FIT LINE ✅
```

---

## 🧮 Mathematical Proof — Three Cases

**Dataset:** `(1,2), (2,4), (3,6)` → `m = 3` data points

**Best Fit Line:** `hθ(x) = θ₀ + θ₁x₁`

**Cost Function:** $J(\theta) = \frac{1}{2m} \sum_{i=1}^{m}(h_\theta(x^{(i)}) - y^{(i)})^2$

---

### Case 1: θ₀ = 0, θ₁ = 2 → `hθ(x) = 2x`

```
x=1: h(1) = 2    y=2   error = 0
x=2: h(2) = 4    y=4   error = 0
x=3: h(3) = 6    y=6   error = 0
```

$$J(\theta) = \frac{1}{2 \times 3}\left[(2-2)^2 + (4-4)^2 + (6-6)^2\right] = 0$$

> ✅ **θ₁ = 2, J(θ) = 0** → This IS the best fit line! Zero error!

---

### Case 2: θ₀ = 0, θ₁ = 1 → `hθ(x) = x`

```
x=1: h(1) = 1    y=2   error = -1
x=2: h(2) = 2    y=4   error = -2
x=3: h(3) = 3    y=6   error = -3
```

$$J(\theta) = \frac{1}{6}\left[(1-2)^2 + (2-4)^2 + (3-6)^2\right] = \frac{1}{6}(1 + 4 + 9) = \frac{14}{6} \approx 2.34$$

> **θ₁ = 1, J(θ) = 2.34**

---

### Case 3: θ₀ = 0, θ₁ = 3 → `hθ(x) = 3x`

```
x=1: h(1) = 3    y=2   error = 1
x=2: h(2) = 6    y=4   error = 2
x=3: h(3) = 9    y=6   error = 3
```

$$J(\theta) = \frac{1}{6}\left[(3-2)^2 + (6-4)^2 + (9-6)^2\right] = \frac{1}{6}(1 + 4 + 9) = 2.34$$

> **θ₁ = 3, J(θ) = 2.34**

---

### 📈 Cost Function Curve

```
J(θ)
  │    ●           ●
  │      ●       ●
  │        ●   ●
  │          ● ──── Global Minima (θ₁ = 2, J=0)
  └──────────────────────────────► θ₁
           1   2   3
               ▲
         BEST FIT LINE
```

> ⭐ **Conclusion:** To get the **Best Fit Line**, we need **minimum error** → **minimum cost function value** → found at **Global Minima** using **Gradient Descent**!

---

## 🏔️ Global Minima & Gradient Descent

### Global Minima

> The point on the cost function curve where `J(θ)` is at its **absolute minimum** — this gives us the best fit line.

```
J(θ)                       
  │  ╲               ╱     ← Local/Global minima exist
  │   ╲             ╱      
  │    ╲           ╱       
  │     ╲_________╱        
  │            ▲           
  │        Global Minima   
  └──────────────────────► θ
```

### Gradient Descent

> **Gradient Descent** is an iterative optimization algorithm used to **minimize the cost function** by adjusting model parameters in the direction of the **steepest descent** of the function's gradient.

```
🎯 Goal: Find θ values that minimize J(θ)
🔄 Method: Iteratively update θ using the gradient
```

### Convergence Theorem (Update Rule)

$$\boxed{\theta_k := \theta_k - \alpha \cdot \frac{\partial J(\theta)}{\partial \theta_k}}$$

Where:
- `θₖ` = current parameter value
- `α` (alpha) = **Learning Rate**
- `∂J(θ)/∂θₖ` = Gradient (slope of cost function)

### Understanding the Gradient

```
Gradient (GD) = slope of cost function
             = dx/dy
             = dJ(θ)/dθ
```

**Left side of curve** (slope = negative):
```
J(θ)│╲
    │  ╲  slope = -ve
    │   ╲
    │    ╲
    └─────────► θ₁

θ_new = θ_old - α × (-ve) → θ increases ✓ (moves right toward minima)
```

**Right side of curve** (slope = positive):
```
J(θ)│       ╱
    │     ╱  slope = +ve
    │   ╱
    └─────────► θ₁

θ_new = θ_old - α × (+ve) → θ decreases ✓ (moves left toward minima)
```

> Both cases move **toward the global minima**! ✅

---

## ⚡ Convergence Theorem & Learning Rate

### Learning Rate (α)

| α Value | Effect |
|---------|--------|
| **Too Small** | Slow training — takes many steps |
| **Too Large** | Divergence — may miss minima |
| **Just Right** | Converges to global minima efficiently ✅ |

```
α too small:   ──────────────────────────────►  (slow)
α just right:  ──────►  (efficient convergence)
α too large:   ↗↘↗↘  (oscillates / diverges)
```

### Gradient Descent Summary

```
① First: Initialize θ₀, θ₁ with random values
② Make prediction based on current parameters
③ Calculate Cost Function J(θ)
④ Use Convergence Theorem to update parameters
⑤ Repeat until J(θ) reaches global minima
```

---

## 📊 Evaluation Metrics

> **Evaluation Metrics** measure how good a model is at making predictions.

### 1. Mean Absolute Error (MAE)

$$\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$$

```python
from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_test, y_pred)
```

### 2. Mean Squared Error (MSE)

$$\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

```python
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, y_pred)
```

### 3. Root Mean Squared Error (RMSE)

$$\text{RMSE} = \sqrt{\text{MSE}}$$

```python
import numpy as np
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
```

> 💡 RMSE is in the **same units** as the target variable — easier to interpret!

---

### 4. R² Score (R-Squared)

$$R^2 = 1 - \frac{\sum(y_i - \hat{y}_i)^2}{\sum(y_i - \bar{y})^2} = 1 - \frac{\text{Residual Errors}}{\text{Total Variance}}$$

```python
from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_pred)
```

**Interpretation:**
| R² Value | Meaning |
|----------|---------|
| `0.7 – 0.8` | Good |
| `0.8 – 0.9` | Very Good |
| `0.9 – 1.0` | Excellent |
| `0` | Bad model |
| `1` | Perfect model |

- 📌 **Range:** 0 to 1
- 📌 **Also called:** R2 Score in Scikit-Learn
- 📌 **It explains:** the variance of data captured by the model

---

### 5. Adjusted R² Score

$$\text{Adj. } R^2 = 1 - \frac{(1-R^2)(n-1)}{n-p-1}$$

Where:
- `n` = number of rows (observations)
- `p` = number of features
- `R²` = R-squared value

```python
# Manual calculation
n = len(y_test)
p = X_test.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
```

### 🤔 Why Do We Need Adjusted R²?

> **R² always increases** when you add more features — even if those features are **useless**!

**Example:**
```
Before:
  X = [study_hrs → scores(y)]
  R² = 0.8,  Adj R² = 0.78

After adding a useless feature (fav. color):
  R² = 0.85  ↑ (misleading!)
  Adj R² = 0.75  ↓ (correct signal!)
```

> ✅ **Adjusted R²** **penalizes** unnecessary features — it only increases if the new feature **actually improves** the model. Use it to decide whether to keep or eliminate a feature!

---

### 📋 Metrics Comparison Table

| Metric | Formula | Range | Best Value | Sensitive to Outliers |
|--------|---------|-------|------------|----------------------|
| MAE | Avg of `\|errors\|` | [0, ∞) | 0 | Less |
| MSE | Avg of `errors²` | [0, ∞) | 0 | More |
| RMSE | √MSE | [0, ∞) | 0 | More |
| R² | 1 - SS_res/SS_tot | (-∞, 1] | 1 | Moderate |
| Adj R² | Penalized R² | (-∞, 1] | 1 | Moderate |

---

## 📝 Summary

```
┌─────────────────────────────────────────────────────────────┐
│             SUPERVISED LEARNING — COMPLETE FLOW             │
│                                                             │
│  Data ──► Preprocess ──► Select Model ──► Train/Test        │
│                                │                            │
│                         Linear Regression                   │
│                         hθ(x) = θ₀ + θ₁x                   │
│                                │                            │
│                        Cost Function J(θ)                   │
│                     J(θ) = 1/2m Σ(hθ(xⁱ)-yⁱ)²             │
│                                │                            │
│                       Gradient Descent                      │
│                    θ := θ - α·∂J(θ)/∂θ                     │
│                                │                            │
│                        Global Minima                        │
│                       Best Fit Line ✅                       │
│                                │                            │
│                    Evaluate with Metrics                    │
│                   MAE / MSE / RMSE / R²                     │
└─────────────────────────────────────────────────────────────┘
```

### Gradient Descent Process (Step-by-Step)

1. **Initialize** θ₀, θ₁ with random values
2. **Make predictions** based on current θ
3. **Calculate** Cost Function J(θ)
4. **Apply Convergence Theorem** to update θ₀, θ₁
5. **Repeat** until J(θ) reaches global minima → **Best Fit Line!** 🎯

### Encoding Reminder

```python
# Binary encoding example
Smoker:  Yes → 1,  No → 0
Sex:   Female → 1, Male → 0

# Train/Test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

---

## 📚 References

- 📘 **Book:** *The Elements of Statistical Learning* – Hastie, Tibshirani, Friedman
- 🌐 **Scikit-Learn Docs:** [scikit-learn.org/stable/supervised_learning.html](https://scikit-learn.org/stable/supervised_learning.html)

---

<div align="center">

## 🌟 Algorithms Covered in Supervised Learning

| Algorithm | Type | Import |
|-----------|------|--------|
| Linear Regression | Regression | `from sklearn.linear_model import LinearRegression` |
| Logistic Regression | Classification | `from sklearn.linear_model import LogisticRegression` |
| K-Nearest Neighbors | Both | `from sklearn.neighbors import KNeighborsClassifier` |
| Decision Trees | Both | `from sklearn.tree import DecisionTreeClassifier` |
| Support Vector Machine | Both | `from sklearn.svm import SVC` |
| Naive Bayes | Classification | `from sklearn.naive_bayes import GaussianNB` |

---

```
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║           Made with ❤️ by  Sayan                         ║
║                                                          ║
║      "The goal of ML is to learn from data and           ║
║       make predictions on unseen examples."              ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
```

![Footer](https://img.shields.io/badge/Made%20by-Sayan-purple?style=for-the-badge)
![ML](https://img.shields.io/badge/Topic-Machine%20Learning-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

</div>
