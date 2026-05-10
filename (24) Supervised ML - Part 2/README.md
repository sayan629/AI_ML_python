<div align="center">

# 🧠 Supervised Learning — Part 2

![ML Banner](https://img.shields.io/badge/Machine%20Learning-Supervised%20Learning-blueviolet?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Complete%20Notes-brightgreen?style=for-the-badge)
![Made with Love](https://img.shields.io/badge/Made%20with-❤️%20by%20Sayan-red?style=for-the-badge)

```
╔══════════════════════════════════════════════════════════════════╗
║         📚  Supervised Learning — In-Depth Notes & Guide        ║
║              Feature Engineering · Regularization · Logistic    ║
╚══════════════════════════════════════════════════════════════════╝
```

</div>

---

## 📋 Table of Contents

1. [Feature Engineering — Encoding](#1-feature-engineering--encoding)
2. [Dummy Variable Trap](#2-dummy-variable-trap)
3. [Other Feature Engineering Techniques](#3-other-feature-engineering-techniques)
4. [Overfitting](#4-overfitting)
5. [Underfitting](#5-underfitting)
6. [How to Fix Underfit & Overfit](#6-how-to-fix-underfit--overfit)
7. [Is Model Underfitting or Overfitting? → Code](#7-is-model-underfitting-or-overfitting--code)
8. [Regularization — Lasso Regression](#8-regularization--lasso-regression-l1)
9. [Regularization — Ridge Regression](#9-regularization--ridge-regression-l2)
10. [Lasso Regression — Implementation](#10-lasso-regression--implementation)
11. [Using LassoCV](#11-using-lassocv)
12. [ElasticNet Overview](#12-elasticnet-overview)
13. [Logistic Regression — Intuition](#13-logistic-regression--intuition)
14. [Logistic Regression — Cost Function](#14-logistic-regression--cost-function)
15. [Logistic Regression — Code](#15-logistic-regression--code)

---

## 🛠️ Tech Stack & Tools

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

</div>

---

## 1. 🔧 Feature Engineering — Encoding

> **Feature Engineering** = Transforming, creating, or selecting input variables to make our model perform better.

### Encoding Categorical Variables

**One Hot Encoding** creates separate binary columns for each category.

```
Smoker Column         One Hot Encoding
   Yes   →    Smoking-Yes: 1,  Smoking-No: 0
   No    →    Smoking-Yes: 0,  Smoking-No: 1
```

**Code Example:**
```python
X = insurance_data.drop(columns=["charges"])
y = insurance_data["charges"]
X = pd.get_dummies(X, columns=["region"], drop_first=False)
```

---

## 2. 🪤 Dummy Variable Trap

> Occurs when encoded features are **highly correlated (multicollinear)** with each other.

### What is Multicollinearity?
When features in a dataset are **highly correlated** with each other.

**Example:**
```
Region → A, B, C
Region_A + Region_B + Region_C = 1   ← multicollinearity!
```

This makes it difficult for the model to find the right coefficients (θ₁, θ₂, θ₃).

**Problems:**
- Inflated errors
- Unstable coefficients

### Solution
Drop one feature using `drop_first=True`:

```python
X = pd.get_dummies(X, columns=["region"], drop_first=True)
# Region_B + Region_C = 1  → if both = 0, user is in Region_A
```

> **Formula:** `Dummy Variables = n - 1`  *(where n = total number of category classes)*

---

## 3. 🔬 Other Feature Engineering Techniques

### 🔹 Create Useful Derived Features

Create new features from existing ones.

```
BMI Feature → Split into:
   < 18     → Underweight  (0)
   18–25    → Normal       (1)
   > 25     → Overweight   (2)
```

### 🔹 Interaction Features

Combine two or more features to capture their combined effect.

```python
X["age-smoker"] = X["age"] * X["smoker"]
X["study_hrs_attendance"] = X["study_hrs"] * X["attendance"]
```

> *Individually they matter, but together may affect outcomes more strongly.*

### 🔹 Scaling Numeric Features

Bring all numeric values into a similar range so one large-value feature doesn't dominate.

```
Before Scaling:    Age → 20–60,     Salary → 20,000–60,000
After Scaling:     Age → 0.2–0.6,   Salary → 0.1–0.9
```

**Two popular scaling techniques:**
- **Normalization** (Min-Max Scaling)
- **Standardization** (Z-Score Scaling)

### 🔹 Feature Selection

Choose the most important features and remove unnecessary ones.

```
Study Hrs → directly affects Score     → KEEP ✅
Fav Color → no relation with marks     → REMOVE ❌
```

---

## 4. 📈 Overfitting

> **Model is too complex** — performs very well on training data but poorly on test data.

```
Training Accuracy → 95% ↑
Test Accuracy     → 65% ↓
```

**Characteristics:**
- 🔴 **Low Bias** — small errors on training data
- 🔴 **High Variance** — very sensitive to small data changes; fits outliers too

```
Bias    = Error from wrong assumptions
Variance = Sensitivity to small data changes
```

> An overfit model passes through outliers → called **High Variance**.

---

## 5. 📉 Underfitting

> **Model is too simple** — performs poorly on both training and test data.

```
Training Accuracy → 75% ↓
Test Accuracy     → 65% ↓
```

**Characteristics:**
- 🔵 **High Bias** — large errors on training data
- 🔵 **Low Variance** — not sensitive to data changes

> Adding data barely shifts the line — model gives the same output → **Low Variance**.

### ⭐ What Does a Model Want?

```
✅ Low Bias + Low Variance = Optimal Model
   → Training and Testing both accuracy is good
```

---

## 6. 🔧 How to Fix Underfit & Overfit

```
                   Bias-Variance Tradeoff
                   
High ──────────────────────────────────────
Prediction         Underfitting  |  Overfitting
Error              High Bias     |  High Variance
                   Low Variance  |  Low Bias
                         ↓ Trade-off ↓
Low ───────────────────────────────────────
        Low            Model Complexity           High
```

| Fix Strategy       | Underfitting                       | Overfitting                        |
|--------------------|------------------------------------|------------------------------------|
| **Model Complexity** | Increase ↑ (more params, neurons) | Decrease ↓ (fewer params, layers) |
| **Regularization**  | Decrease regularization            | Increase regularization            |
| **Features**        | Add more features                  | Reduce number of features          |
| **Data**            | Adding data doesn't help           | Adding more data helps ✅          |

---

## 7. 🖥️ Is Model Underfitting or Overfitting? → Code

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

train_score = r2_score(y_train, model.predict(X_train))
test_score  = r2_score(y_test, model.predict(X_test))

print(f"Train Score: {train_score:.2f}")
print(f"Test Score:  {test_score:.2f}")

# Train >> Test  → Overfitting
# Both low       → Underfitting
# Both high      → Optimal ✅
```

---

## 8. 🔵 Regularization — Lasso Regression (L1)

> Regularization is used when **overfitting conditions** happen. We add a penalty so the cost function cannot become zero.

**Cost Function (Lasso):**

$$J(\theta) = \frac{1}{2m} \sum_{i=1}^{m}(h_\theta(x^{(i)}) - y^{(i)})^2 + \lambda \sum_{j=1}^{n}|\theta_j|$$

```
Cost = Error + λ · Penalty
         ↑
   Regularization Strength (how strong penalties we want)
```

**Note:**
- `θⱼ` = parameters, `j = 1 to n` (n features)
- `θ₀` (bias) is **not regularized**
- In sklearn, `λ` is called **`alpha`**

**Lasso Regression helps:**
1. ✅ Prevents overfitting
2. ✅ Performs **feature selection** (reduces unimportant feature coefficients to **exactly 0**)

> When `alpha = 0` in Lasso → equivalent to plain Linear Regression (not advised).

---

## 9. 🟠 Regularization — Ridge Regression (L2)

**Cost Function (Ridge):**

$$J(\theta) = \frac{1}{2m} \sum_{i=1}^{m}(h_\theta(x^{(i)}) - y^{(i)})^2 + \lambda \sum_{j=1}^{n}\theta_j^2$$

$$J(\theta) = \text{Error} + \lambda(\text{slope})^2$$

**Key behavior:**
- J(θ) value is always positive → minimizing it reduces slope
- **Goal:** minimize overall J(θ)
- As slope decreases → error increases → balance is found

**Ridge Regression helps:**
1. ✅ Prevents overfitting
2. ✅ Handles **multicollinearity** better than Lasso
3. ❌ Does **not** do feature selection (shrinks, never zeroes out)

```
In sklearn → α = alpha
Slope decrease → Error increase (tradeoff)
```

---

## 10. 💻 Lasso Regression — Implementation

```python
from sklearn.linear_model import Lasso, Ridge
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Lasso (L1)
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)
print("Lasso Coefficients:", lasso.coef_)

# Ridge (L2)
ridge = Ridge(alpha=0.1)
ridge.fit(X_train, y_train)
print("Ridge Coefficients:", ridge.coef_)
```

---

## 11. 🔄 Using LassoCV

> **LassoCV** performs **Cross Validation** to find the best `alpha` automatically.

### What is Cross Validation?
Data is split into multiple parts called **folds**.

```
[ Fold1 | Fold2 | Fold3 | Fold4 | Fold5 ]
   Test   Train   Train   Train   Train   → Iteration 1
   Train   Test   Train   Train   Train   → Iteration 2
   ...
```

Multiple iterations are performed, slightly changing training & testing data, so the calculated average model is the best-optimized model.

```python
from sklearn.linear_model import LassoCV

lasso_cv = LassoCV(cv=5)
lasso_cv.fit(X_train, y_train)

print("Best Alpha:", lasso_cv.alpha_)
print("Coefficients:", lasso_cv.coef_)
```

---

## 12. 🔗 ElasticNet Overview

> **ElasticNet** is a regression model that uses **both** Lasso (L1) and Ridge (L2) penalties.

**Cost Function:**

$$J(\theta) = \frac{1}{2m}\sum_{i=1}^{m}(h_\theta(x^{(i)}) - y^{(i)})^2 + \lambda\alpha\sum_{j=1}^{n}|\theta_j| + (1-\alpha)\lambda\sum_{j=1}^{n}\theta_j^2$$

```
                      ↑ Lasso          ↑ Ridge
```

### Why Use ElasticNet?

| Advantage | Description |
|-----------|-------------|
| 🔀 Combines Lasso + Ridge | Best of both worlds |
| ✂️ Feature Selection | Like Lasso — can zero out features |
| 🛡️ Multicollinearity | Like Ridge — handles correlated features |
| 📊 Useful when | Dataset has many correlated features |

```python
from sklearn.linear_model import ElasticNet

# X → L1 ratio
# X = 0  → Pure Ridge (L2)
# X = 1  → Pure Lasso (L1)

en = ElasticNet(alpha=0.1, l1_ratio=0.5)
en.fit(X_train, y_train)
```

---

## 13. 📊 Logistic Regression — Intuition

> Used for **Classification** (not regression despite the name!)

### Why Not Linear Regression for Classification?

Using temperature to predict Rain (0/1):

| Temp (°C) | Rain (y) |
|-----------|----------|
| 5  | 0 |
| 10 | 0 |
| 15 | 0 |
| 20 | 1 |
| 25 | 1 |
| 35 | 1 |

**Problems with Linear Regression here:**
- Values on best-fit line are **not probability values**
- `hθ(x) > 1` and `hθ(x) < 0` are possible
- Outliers can shift the regression line badly

### Solution: Squashing Function (Sigmoid)

We need a function that **squashes** values into bounded range **[0, 1]**.

```
In Logistic Regression → Sigmoid function is used
```

$$g(z) = \frac{1}{1 + e^{-z}}$$  *(where e = Euler's number ≈ 2.718)*

**Hypothesis Function for Logistic Regression:**

$$h_\theta(x) = g(\theta_0 + \theta_1 x_1) = \frac{1}{1 + e^{-(\theta_0 + \theta_1 x_1)}}$$

**Sigmoid Characteristics:**
```
z = 0  →  g(z) = 0.5
z > 0  →  g(z) > 0.5
z < 0  →  g(z) < 0.5
Range of Sigmoid: (0, 1)
```

**Matrix Form:**
$$h_\theta(x) = \frac{1}{1 + e^{-\theta^T x}}$$

where `θᵀx = θ₀ + θ₁x₁ + θ₂x₂ + ...`

---

## 14. 📐 Logistic Regression — Cost Function

### Why Not Use MSE with Sigmoid?

If we use standard MSE → **non-convex curve** with many local minima → gradient descent gets stuck.

### Log Loss / Binary Cross-Entropy Function

$$J(\hat{y}^{(i)}, y^i) = \begin{cases} -\log(\hat{y}^{(i)}) & \text{if } y^i = 1 \\ -\log(1 - \hat{y}^{(i)}) & \text{if } y^i = 0 \end{cases}$$

**Intuition:**
- Actual = 0, Model predicts 0.1 or 0.2 → small mistake → small penalty
- Actual = 0, Model predicts 0.9 → big mistake → **big penalty** 🚨
- Where error is big → penalty should increase → that's why this function is used

This function is also called:
- **Log Loss function**
- **Binary Cross Entropy function**

### Combined Cost Function:

$$\hat{j}(\hat{y}, y) = -y\log(\hat{y}) - (1-y)\log(1-\hat{y})$$

**Overall Cost Function:**

$$J(\theta) = -\frac{1}{m}\sum_{i=1}^{m}\left(y^{(i)}\log(\hat{y}^{(i)}) + (1-y)\log(1 - \hat{y}^{(i)})\right)$$

This gives a **convex curve** → gradient descent converges to global minimum ✅

**Gradient Descent Update Rule:**

$$\theta_j = \theta_j - \alpha \frac{\partial J(\theta)}{\partial \theta}$$

---

## 15. 💻 Logistic Regression — Code

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
```

---

## 📚 References & Further Reading

<div align="center">

| Resource | Link |
|----------|------|
| 📖 **Scikit-learn Documentation** | [sklearn.org](https://scikit-learn.org/stable/user_guide.html) |
| 📘 **Lasso Regression (sklearn)** | [sklearn Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html) |
| 📘 **Ridge Regression (sklearn)** | [sklearn Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html) |
| 📘 **ElasticNet (sklearn)** | [sklearn ElasticNet](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html) |
| 📘 **LassoCV (sklearn)** | [sklearn LassoCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html) |
| 📘 **Logistic Regression (sklearn)** | [sklearn LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) |
| 📗 **The Elements of Statistical Learning** | [Hastie, Tibshirani & Friedman — Free PDF](https://hastie.su.domains/ElemStatLearn/printings/ESLII_print12_toc.pdf) |
| 📗 **ESL Book (Official Page)** | [Stanford — ESL](https://hastie.su.domains/ElemStatLearn/) |

</div>

> 📖 **The Elements of Statistical Learning** by Hastie, Tibshirani & Friedman is the gold-standard textbook covering all topics above in rigorous mathematical depth — Chapters 3 (Linear Methods), 4 (Linear Classification), and 18 (High-Dimensional Problems) are especially relevant.

---

## 🗂️ Quick Cheat Sheet

```
┌────────────────────────────────────────────────────────────────┐
│                    REGULARIZATION SUMMARY                      │
├──────────────┬────────────────────┬────────────────────────────┤
│              │ Lasso (L1)         │ Ridge (L2)                 │
├──────────────┼────────────────────┼────────────────────────────┤
│ Penalty      │ λ·Σ|θⱼ|           │ λ·Σθⱼ²                    │
│ Feature Sel. │ ✅ Yes (zeros out) │ ❌ No (shrinks)           │
│ Multicollin. │ ⚠️ Moderate        │ ✅ Better                 │
│ Use When     │ Sparse features    │ All features matter        │
├──────────────┴────────────────────┴────────────────────────────┤
│ ElasticNet = Lasso + Ridge (best of both worlds)               │
└────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────┐
│                  BIAS-VARIANCE CHEAT SHEET                     │
├───────────────────┬──────────────────────────────────────────  │
│ Underfitting      │ High Bias, Low Variance                    │
│ Overfitting       │ Low Bias, High Variance                    │
│ Optimal Model     │ Low Bias, Low Variance ✅                  │
└───────────────────┴────────────────────────────────────────────┘
```

---

<div align="center">

---

### 🙋‍♂️ Made by

<a href="https://www.linkedin.com/in/sayanpal04?utm_source=share_via&utm_content=profile&utm_medium=member_android">
  <img src="https://img.shields.io/badge/Sayan%20Pal-Connect%20on%20LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn - Sayan Pal"/>
</a>

> *"The goal of Machine Learning is to make computers learn from data without being explicitly programmed."*

![Visitor](https://img.shields.io/badge/Keep%20Learning-🚀%20Never%20Stop-orange?style=for-the-badge)

</div>
