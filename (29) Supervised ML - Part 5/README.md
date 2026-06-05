# 🤖 Supervised Machine Learning — Part 5
### *A Complete Study Guide: SVM · Ensemble Learning · Random Forest*

<div align="center">

![ML Banner](https://img.shields.io/badge/Machine%20Learning-Supervised%20Part%205-blueviolet?style=for-the-badge&logo=python&logoColor=white)
![SVM](https://img.shields.io/badge/SVM-Support%20Vector%20Machine-ff6b6b?style=for-the-badge)
![Ensemble](https://img.shields.io/badge/Ensemble-Bagging%20%26%20Boosting-4ecdc4?style=for-the-badge)
![Status](https://img.shields.io/badge/Notes-Complete-brightgreen?style=for-the-badge)

</div>

---

## 📚 Table of Contents

| # | Topic | Category |
|---|-------|----------|
| 1 | [Introduction to SVM](#1-introduction-to-svm) | SVM |
| 2 | [SVM Classifier](#2-svm-classifier) | SVM |
| 3 | [Classification Hyperparameters](#3-classification-hyperparameters) | SVM |
| 4 | [Kernel in SVM](#4-kernel-in-svm) | SVM |
| 5 | [Common Kernel Types](#5-common-kernel-types) | SVM |
| 6 | [Common SVM Kernels](#6-common-svm-kernels) | SVM |
| 7 | [SVM Classifier (Code)](#7-svm-classifier-code) | SVM |
| 8 | [SVM Regressor (Intuition)](#8-svm-regressor-intuition) | SVM |
| 9 | [SVM Regressor (Code)](#9-svm-regressor-code) | SVM |
| 10 | [GridSearchCV for Hyperparameters](#10-gridsearchcv-for-hyperparameters) | SVM |
| 11 | [Linear SVR vs SVR](#11-linear-svr-vs-svr) | SVM |
| 12 | [Ensemble Learning](#12-ensemble-learning) | Ensemble |
| 13 | [What is Bagging?](#13-what-is-bagging) | Ensemble |
| 14 | [What is Boosting?](#14-what-is-boosting) | Ensemble |
| 15 | [Random Forest](#15-random-forest) | Ensemble |
| 16 | [Out of Bag (OOB)](#16-out-of-bag-oob) | Ensemble |
| 17 | [Random Forest (Implementation)](#17-random-forest-implementation) | Ensemble |
| 18 | [Decision Tree vs Random Forest](#18-decision-tree-vs-random-forest) | Ensemble |
| 19 | [Bagging Classifier & Regressor](#19-bagging-classifier--regressor) | Ensemble |

---

## 🧠 Support Vector Machine (SVM)

---

### 1. Introduction to SVM

> **Support Vector Machine (SVM)** is a powerful supervised ML algorithm used for both classification and regression.

```
            SVM
           /   \
         SVC    SVR
   (Support    (Support
    Vector      Vector
  Classifier)  Regressor)
```

**Key Concepts:**

| Term | Description |
|------|-------------|
| 🔵 **Decision Boundary** | Hyperplane: `wᵀx + b = 0` |
| 📐 **Margin** | Distance between the two margin hyperplanes |
| 📏 **Margin Hyperplane** | Equidistant & parallel to decision boundary |

**Characteristics of Margin Hyperplane:**
- ① Equidistant from Decision Boundary
- ② Parallel to each other

```
High Margin → Data perfectly linearly separable
Low Margin  → Data can have overlap, noise, or outliers
```

| Type | When Used |
|------|-----------|
| **Hard Margin SVM** | Classes are perfectly / clearly separable |
| **Soft Margin SVM** | Classes are NOT perfectly separable |

---

### 2. SVM Classifier

**Mathematical Formulation:**

Given equation: `2x - 3y + 2 = 0`

```
P₁(1,5): 2(1) - 3(5) + 2 = -15 < 0  →  Class 1 side
P₂(5,1): 2(5) - 3(1) + 2 = +9 > 0   →  Class 2 side
```

**Margin Hyperplane Equations:**

$$w^Tx + b = 1 \quad \text{(Margin Hyperplane 1)}$$
$$w^Tx + b = -1 \quad \text{(Margin Hyperplane 2)}$$

**Margin Formula:**

$$\text{margin} = \frac{2}{||w||}$$

where $||w|| = \sqrt{w_1^2 + w_2^2 + w_3^2 + \ldots}$ is the **Euclidean norm**.

**SVM Objective:**

$$\text{Maximize} \frac{2}{||w||} \implies \text{Minimize} \frac{||w||^2}{2}$$

---

### 3. Classification Hyperparameters

**Ideal SVM Equation (Hard Margin):**

$$\min_{(w,b)} \frac{||w||^2}{2}$$

**Constraint:**

$$y_i = \begin{cases} +1 & w^Tx + b \geq 1 \\ -1 & w^Tx + b \leq -1 \end{cases}$$

$$\boxed{y_i \cdot (w^T x_i + b) \geq 1}$$

**Soft Margin — Cost / Loss Function:**

$$\min_{(w,b)} \frac{||w||^2}{2} + C \cdot \sum_{i=1}^{n} \xi_i$$

> **ξ (Eta)** = Slack variable / Degree of violation (Sum of distances from misclassified points to the margin hyperplane)

```
C → Large  →  Fewer misclassifications   (Overfitting)
C → Small  →  Large misclassifications   (Underfitting)
```

**C Parameter (Hyperparameter Tuning):**

| C Value | Effect |
|---------|--------|
| 🔴 **High C** | Narrow margin, more variance (overfitting) |
| 🟢 **Low C** | Wider margin, more bias (underfitting) |

*Tested values: `[0.5, 1, 2, 3, 4, 5]`*

---

### 4. Kernel in SVM

> **Kernels** are functions that map data into a higher dimensional space, allowing SVMs to find non-linear patterns and separate complex data that isn't linearly separable in its original space.

```
1D → 2D
2D → 3D      Kernel Trick!
3D → 4D
```

**Example:** Data not separable in 1D becomes separable in 2D using kernel `y = x²`

```
1D (not separable):  o o o x x x x x o o o
       ↓  Kernel (y = x²)
2D (separable):  Clear boundary between classes!
       ↓  
3D (even more separable!)
```

> **Kernel Trick** = The process of applying a kernel function on the data.

---

### 5. Common Kernel Types

| Kernel | Formula | Best Use Case |
|--------|---------|---------------|
| **Linear** | `K(x,x') = xᵀx'` | Text classification, high-dim linearly separable data |
| **Polynomial** | `K(x,x') = (xᵀx' + θ)^d` | Image recognition, pattern analysis |
| **RBF (Gaussian)** | `K(x,x') = e^(-γ‖x-x'‖²)` | Complex non-linear problems (handwriting, medical) |
| **Sigmoid** | `K(x,x') = tanh(γ · xᵀx' + θ)` | Mimics neural networks, niche datasets |

> ⭐ **RBF is the default kernel in SVC!**

---

### 6. Common SVM Kernels

```python
from sklearn.svm import SVC

# Linear Kernel
svc_linear = SVC(kernel='linear', C=1.0)

# Polynomial Kernel
svc_poly = SVC(kernel='poly', degree=3, C=1.0)

# RBF Kernel (Default)
svc_rbf = SVC(kernel='rbf', C=1.0, gamma='scale')

# Sigmoid Kernel
svc_sigmoid = SVC(kernel='sigmoid', C=1.0)
```

---

### 7. SVM Classifier (Code)

```python
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Preprocessing
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

# Model
svc = SVC(kernel='rbf', C=2, gamma='scale')
svc.fit(X_train_scaled, y_train)

# Evaluation
y_pred = svc.predict(X_test_scaled)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
```

---

### 8. SVM Regressor (Intuition)

> **SVR (Support Vector Regressor)** uses an **ε-insensitive tube** (epsilon tube) around the regression line.

```
         ε tube (ε-insensitive zone)
    ___________________________
   /  ° °  °     °    °       \   ← wᵀx + b + ε
  /    °  °  °  °  °   °      \
 (         wᵀx + b              )
  \    °  °  °  °  °   °      /
   \___________________________/  ← wᵀx + b - ε
```

**Key:**
- `ε value` = Margin of tolerance
- Points **inside** the tube → No penalty
- Points **outside** → Penalized via slack variables

---

### 9. SVM Regressor (Code)

**Cost Function:**

$$\min_{(w,b)} \frac{||w||^2}{2}$$

**Constraint:** $|y_i - \hat{y}_i| \leq \varepsilon$  i.e.,  $|y_i - (w^T x_i + b)| \leq \varepsilon$

**With Slack Penalty:**

$$\min_{(w,b)} \frac{||w||^2}{2} + C \sum_{i=1}^{n} \xi_i \xi_i^*$$

$$|y_i - \hat{y}_i| \leq \varepsilon + \xi_i$$
$$|w^T x + b - y_i| \leq \varepsilon + \xi_i^*$$

```python
from sklearn.svm import SVR

svr = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=0.1)
svr.fit(X_train_scaled, y_train)
y_pred = svr.predict(X_test_scaled)
```

---

### 10. GridSearchCV for Hyperparameters

> **GridSearchCV** exhaustively searches the best hyperparameter combination using cross-validation.

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'C':      [1, 2, 5, 10, 50, 100],
    'kernel': ['rbf', 'linear']
}

grid_search = GridSearchCV(SVC(), param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train_scaled, y_train)

print("Best Params:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)

# Retrain best model
best_model = grid_search.best_estimator_
```

✅ Best parameters identified using **cross-validation**  
✅ Best model **retrained and evaluated**

---

### 11. Linear SVR vs SVR

| Feature | SVR | Linear SVR |
|---------|-----|------------|
| **Kernel Support** | Multiple kernels | Linear kernel only |
| **Speed** | Slower on large datasets | Faster & more scalable |
| **Data Type** | Non-linear data | High-dimensional linear data |
| **Visual** | Epsilon tube (curved) | Best fit line |

```
SVR with RBF Kernel          Linear SVR
     ε-tube (curved)          best fit line
    ~~~~~~~~~~~              /
   ~  · · · ·  ~            / · · · ·
  ~  · · · · ·  ~          / · ·  · ·
   ~~~~~~~~~~~             /
```

---

## 🌲 Ensemble Learning

---

### 12. Ensemble Learning

> An ML technique that **aggregates two or more learners** in order to produce better predictions.

```
  [weak]  ╮
  [weak]  ├──► [STRONG]  →  Strong Learner
  [weak]  ╯
```

**Two Main Techniques:**

| Technique | Goal | Method |
|-----------|------|--------|
| 🎒 **Bagging** | Reduce Variance | Parallel models |
| 🚀 **Boosting** | Reduce Bias | Sequential models |

```
Bagging:   → [m1] ─╮
           → [m2] ──┼─► Aggregate
           → [m3] ─╯

Boosting:  → [m1] → [m2] → [m3] → [m4] →
```

> Both Bagging & Boosting work for **Regression + Classification**!

---

### 13. What is Bagging?

> Uses **modified replicas** of a training dataset to train multiple base learners with the **same training algorithm**.

**Steps:**

```
Training Data → Bootstrap Samples → Learners → Ensemble Prediction
     [data]   ──► [sample1] ──► Learner1 ──► yes ╮
               ──► [sample2] ──► Learner2 ──► yes ─┼──► (+) Final
               ──► [sample3] ──► Learner3 ──► no  ╯
```

| Step | Description |
|------|-------------|
| **1. Data Sampling** | Bootstrap sampling **with replacement** |
| **2. Model Training** | Train each base learner independently |
| **3. Aggregation** | Classification → Majority voting; Regression → Mean/Average |

> ⭐ **Famous Algorithm in Bagging = Random Forest**  
> Goal: **Stability becomes increased** (Variance ↓)

---

### 14. What is Boosting?

> Each model **sequentially tries to correct** the mistakes of previous ones.

**Process:**

```
Training Data → Model1 ──► Incorrect predictions
                        ──► Correct predictions
Weighted Data → Model2 ──► Incorrect predictions (fewer)
                        ──► Correct predictions
...
Weighted Data → Model n ──► Final minimal errors
```

| Step | Description |
|------|-------------|
| **1. Sequential Training** | Each model learns from previous errors |
| **2. Weight Adjustment** | Misclassified samples get higher weights |

> Goal: **Accuracy should increase** (Bias ↓)

**Famous Boosting Algorithms:** AdaBoost, Gradient Boosting, XGBoost, LightGBM

---

### 15. Random Forest

> A **Bagging Ensemble Learning** method applied on Decision Trees.

```
Dataset (n samples, f features)
        │
        ├──► D1 (n, f1,f2,f5) ──► DT1 ──╮
        ├──► D2 (n, f3,f4,f5) ──► DT2 ──┼──► Bootstrap Aggregation
        └──► D3 (n, f1,f2,f4) ──► DT3 ──╯
        
                    (max_features = 3 if f=6)
```

**Data Sampling Types:**

| Type | Method |
|------|--------|
| **Row Sampling** | Bootstrap Sampling **with replacement** |
| **Column Sampling** | Feature Sampling / Feature Bagging |

---

### 16. Out of Bag (OOB)

> A **built-in validation method** in bagging that lets us estimate model performance **without a separate validation set**.

```
Dataset
  ├──► Training Data   [~2/3]
  └──► Validation Data [~1/3]  ← OOB Samples
```

**Math:**

```
n samples
P(not getting selected) = 1 - 1/n
n draws ⟹ (1 - 1/n)^n ≈ e⁻¹ ≈ 36.8%
```

> ~36.8% of data is never selected → becomes OOB validation data!

| Metric | Description |
|--------|-------------|
| **OOB Accuracy/Score** | Measured on samples NOT used in training |
| **OOB Error/Estimate** | Misclassification rate on those samples |

```python
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=100, oob_score=True, random_state=42)
rf.fit(X_train, y_train)

print(f"OOB Score: {rf.oob_score_:.4f}")
```

---

### 17. Random Forest (Implementation)

```python
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, mean_squared_error

# Classification
rf_clf = RandomForestClassifier(
    n_estimators=100,       # Number of trees
    max_features='sqrt',    # Feature sampling
    max_depth=None,
    bootstrap=True,         # Bootstrap sampling
    oob_score=True,
    random_state=42
)
rf_clf.fit(X_train, y_train)
print(f"Accuracy: {accuracy_score(y_test, rf_clf.predict(X_test)):.4f}")
print(f"OOB Score: {rf_clf.oob_score_:.4f}")

# Regression
rf_reg = RandomForestRegressor(n_estimators=100, oob_score=True, random_state=42)
rf_reg.fit(X_train, y_train)
print(f"MSE: {mean_squared_error(y_test, rf_reg.predict(X_test)):.4f}")
```

---

### 18. Decision Tree vs Random Forest

| Feature | Decision Tree 🌿 | Random Forest 🌲🌲🌲 |
|---------|-----------------|---------------------|
| **Structure** | Single tree | Collection of many trees |
| **Accuracy** | Lower | Higher |
| **Overfitting** | More prone | Less prone |
| **Interpretability** | Easy to understand & visualize | Difficult to interpret |
| **Training Speed** | Fast | Slower |
| **Use Case** | Small datasets, explainability | Large datasets, accuracy |

---

### 19. Bagging Classifier & Regressor

```python
from sklearn.ensemble import BaggingClassifier, BaggingRegressor
from sklearn.tree import DecisionTreeClassifier

# Bagging Classifier
bag_clf = BaggingClassifier(
    base_estimator=DecisionTreeClassifier(),
    n_estimators=50,
    max_samples=0.8,       # 80% row sampling
    max_features=0.8,      # 80% feature sampling
    bootstrap=True,
    oob_score=True,
    random_state=42
)
bag_clf.fit(X_train, y_train)
print(f"Accuracy: {accuracy_score(y_test, bag_clf.predict(X_test)):.4f}")

# Bagging Regressor
bag_reg = BaggingRegressor(
    base_estimator=DecisionTreeRegressor(),
    n_estimators=50,
    bootstrap=True,
    oob_score=True,
    random_state=42
)
bag_reg.fit(X_train, y_train)
```

---

## 🗺️ Complete Mind Map

```
Supervised ML (Part 5)
│
├── SVM (Support Vector Machine)
│   ├── SVC (Classification)
│   │   ├── Hard Margin
│   │   └── Soft Margin (C parameter)
│   ├── SVR (Regression)
│   │   ├── ε-insensitive tube
│   │   └── Slack variables (ξ)
│   ├── Kernels
│   │   ├── Linear      K(x,x') = xᵀx'
│   │   ├── Polynomial  K(x,x') = (xᵀx' + θ)^d
│   │   ├── RBF         K(x,x') = e^(-γ‖x-x'‖²)  ← Default
│   │   └── Sigmoid     K(x,x') = tanh(γxᵀx' + θ)
│   └── Hyperparameter Tuning (GridSearchCV)
│       ├── C: [1, 2, 5, 10, 50, 100]
│       └── kernel: [rbf, linear]
│
└── Ensemble Learning
    ├── Bagging (Variance ↓, Stability ↑)
    │   ├── Bootstrap Sampling (with replacement)
    │   ├── Parallel Training
    │   ├── Aggregation (Voting / Mean)
    │   ├── Random Forest ⭐
    │   │   ├── Row Sampling
    │   │   ├── Column Sampling
    │   │   └── OOB Validation (~36.8%)
    │   └── Bagging Classifier/Regressor
    └── Boosting (Bias ↓, Accuracy ↑)
        ├── Sequential Training
        └── Weight Adjustment
```

---

## 📊 Quick Reference Cheat Sheet

### SVM Formulas

| Formula | Meaning |
|---------|---------|
| `wᵀx + b = 0` | Decision Boundary |
| `wᵀx + b = ±1` | Margin Hyperplanes |
| `margin = 2/‖w‖` | Width of margin |
| `min ‖w‖²/2` | SVM Objective (Hard) |
| `min ‖w‖²/2 + C·Σξᵢ` | SVM Objective (Soft) |
| `yᵢ(wᵀxᵢ + b) ≥ 1` | Constraint |

### Ensemble Comparison

| | Bagging | Boosting |
|--|---------|---------|
| **Trains** | In parallel | Sequentially |
| **Reduces** | Variance | Bias |
| **Increases** | Stability | Accuracy |
| **Example** | Random Forest | AdaBoost, XGBoost |

---

<div align="center">

---

## 🙋 Made by

<a href="https://www.linkedin.com/in/sayanpal04?utm_source=share_via&utm_content=profile&utm_medium=member_android">
  <img src="https://img.shields.io/badge/Sayan%20Pal-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Sayan LinkedIn"/>
</a>

### **Sayan Pal**
*Machine Learning Enthusiast *

> *"Understanding the math behind the models."*

[![LinkedIn](https://img.shields.io/badge/Connect%20on%20LinkedIn-%40sayanpal04-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/sayanpal04?utm_source=share_via&utm_content=profile&utm_medium=member_android)

---

*📝 study material — Supervised ML Part 5*  
*Topics: SVM · Kernels · SVR · GridSearchCV · Ensemble · Bagging · Boosting · Random Forest · OOB*

</div>
