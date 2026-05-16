# Supervised Learning - Part 3

## Table of Contents
1. [Normalization & Standardization](#1-normalization--standardization)
2. [Standardizing Data with Standard Scaler](#2-standardizing-data-with-standard-scaler)
3. [Evaluation Metrics for Classification](#3-evaluation-metrics-for-classification)
4. [Naive Bayes](#4-naive-bayes)
5. [Types of Naive Bayes](#5-types-of-naive-bayes)
6. [KNN – K Nearest Neighbours](#6-knn--k-nearest-neighbours)
7. [Limitation of KNN](#7-limitation-of-knn)
8. [Validation Data](#8-validation-data)
9. [Cross Validation](#9-cross-validation)
10. [CV for Hyperparameter Tuning](#10-cv-for-hyperparameter-tuning)
11. [Pipeline in Sklearn](#11-pipeline-in-sklearn)

---

## 1. Normalization & Standardization

### Normalization (Min-Max Scaling)
Normalization rescales the features to a particular range, i.e., **(0, 1)**.

$$X_{scaled} = \frac{X - X_{min}}{X_{max} - X_{min}}$$

### Standardization (Z-Score Scaling)
Here we transform the data in such a way that:
- **mean (μ) = 0**
- **std dev (σ) = 1, variance = 1**

We calculate **μ** and **σ** of the data.

$$X_{standardized} = \frac{X - \mu}{\sigma}$$

### When is Scaling Important?
Scaling of data is important for:
- Logistic Regression
- SVM
- ANN

### Benefits of Scaling
- Convergence is faster

> ⭐ **Note:** Standardization becomes necessary when feature magnitudes differ by **10x or more** and become critical beyond **100x**, especially for distance or gradient-based algorithms.

---

## 2. Standardizing Data with Standard Scaler

There are multiple functions in `StandardScaler`:

| Function | Description |
|----------|-------------|
| `fit()` | Computes the mean and std dev |
| `transform()` | Uses mean & std dev computed by `fit()` → applies `X = (X - μ) / σ` |
| `fit_transform()` | Fit to data, then transform it |

### Data Split Flow

```
          Data
         /    \
  X_training   X_Testing
       ↓             ↓
fit_transform()   transform()
```

### Why does X_testing NOT use `fit_transform()`?

Using `fit` on test data would let the model learn the **σ, μ** of testing data. We want the details of testing data to **remain separate from the model**.

If we told the details of test data to the model, **Data Leakage** is performed.

---

## 3. Evaluation Metrics for Classification

### Confusion Matrix

```
                   Predicted Value
                    0        1
                 ┌──────┬──────┐
Actual Value  0  │  TN  │  FP  │  ← Type 1 Error
              1  │  FN  │  TP  │
                 └──────┴──────┘
                    ↑
               Type 2 Error
```

- **TN** → True Negative
- **FP** → False Positive (Type 1 Error)
- **FN** → False Negative (Type 2 Error)
- **TP** → True Positive

```python
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred)
```

### Classification Report

Used to show detailed performance of a classification model.

```python
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
```

**Sample Output:**

|               | Precision | Recall | F1-Score | Support |
|---------------|-----------|--------|----------|---------|
| 0             | 0.83      | 0.86   | 0.85     | 29      |
| 1             | 0.87      | 0.84   | 0.86     | 32      |
| accuracy      |           |        | 0.85     | 61      |
| macro avg     | 0.85      | 0.85   | 0.85     | 61      |
| weighted avg  | 0.85      | 0.85   | 0.85     | 61      |

### Macro Average
Average of metrics across all classes. Every class gets **equal importance**.

$$\text{Macro Avg} = \frac{\text{metric1} + \text{metric2} + \ldots + \text{metricN}}{n}$$

### Weighted Average
Average based on class support (number of samples). Helps fix class imbalance.

$$\text{Weighted Avg} = \frac{\sum(\text{metric}_i \times \text{support}_i)}{\sum \text{support}_i}$$

### Accuracy
How often is the model correct?

$$\text{Accuracy} = \frac{TN + TP}{TN + FP + FN + TP}$$

### Precision
When the model predicts positive, how often is it correct?

$$\text{Precision} = \frac{TP}{FP + TP}$$

> Used when we want to **minimize Type 1 Errors** (False Positives become costly).
> **Example:** Spam Detection

### Recall (Sensitivity)
How many positives did it catch?

$$\text{Recall} = \frac{TP}{FN + TP}$$

> Used when **Type 2 Errors** become costly.
> **Example:** Medical Diagnosis

### F1 Score
Harmonic mean of Precision and Recall.

$$\text{F1 Score} = \frac{2 \times \text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

```python
from sklearn.metrics import accuracy_score, precision_score
print("Accuracy Score =", accuracy_score(y_test, y_pred))
print("Precision Score =", precision_score(y_test, y_pred))
```

---

## 4. Naive Bayes

Naive Bayes is a **probabilistic Supervised ML algorithm** mainly used for **classification tasks**.

It uses **Bayes' Theorem** to predict probability:

$$P\left(\frac{A}{B}\right) = \frac{P\left(\frac{B}{A}\right) \cdot P(A)}{P(B)}$$

### Why "Naive"?
"Naive" comes from the **naive assumption** the algorithm makes — it assumes that **all input features are independent** of each other within the class.

$$P(A \cap B) = P(A) \cdot P(B)$$

### Applications
- Email/Spam Detection
- Text Classification
- Medical Diagnosis

### Generalized Formula

For a dataset with features X₁, X₂, X₃ and output y:

$$P\left(\frac{y}{X_1, X_2, X_3}\right) = \frac{P\left(\frac{X_1 X_2 X_3}{y}\right) \cdot P(y)}{P(X_1, X_2, X_3)}$$

Since we **ignore the denominator** (it's constant):

$$P\left(\frac{yes}{X_1, X_2, X_3}\right) \propto P\left(\frac{X_1}{yes}\right) \cdot P\left(\frac{X_2}{yes}\right) \cdot P\left(\frac{X_3}{yes}\right) \cdot P(yes)$$

### Example – Rain Prediction

**Dataset:**

| Weather | Wind   | Rain |
|---------|--------|------|
| Hot     | Weak   | Y    |
| Hot     | Weak   | Y    |
| Cold    | Weak   | N    |
| Hot     | Strong | N    |
| Cold    | Strong | Y    |

**Given:** Weather = Hot (X₁), Wind = Strong (X₂)

- P(Yes) = 3/5, P(No) = 2/5

**P(Yes | hot, strong):**

$$\propto P\left(\frac{Hot}{Yes}\right) \cdot P\left(\frac{Strong}{Yes}\right) \cdot P(Yes) = \frac{2}{3} \cdot \frac{1}{3} \cdot \frac{3}{5} = \frac{2}{15} \approx 0.133$$

**P(No | hot, strong):**

$$\propto P\left(\frac{Hot}{No}\right) \cdot P\left(\frac{Strong}{No}\right) \cdot P(No) = \frac{1}{2} \cdot \frac{1}{2} \cdot \frac{2}{5} = \frac{1}{10} \approx 0.1$$

**Prediction:** Since P(Yes) > P(No) → **Rain = Yes**

---

## 5. Types of Naive Bayes

### 1. Gaussian Naive Bayes
$$P\left(\frac{x}{c}\right) = \frac{1}{\sqrt{2\pi\sigma^2}} \cdot e^{-\frac{(x - \mu)^2}{2\sigma^2}}$$

- Used for **continuous values** in datasets
- **Examples:** Medical Diagnosis, temperature, weight, height, scores

### 2. Multinomial Naive Bayes
- Used for **discrete values** in datasets
- **Example:** Text classification

### 3. Bernoulli Naive Bayes
- Used when features have **binary values**

### 4. Complementary Naive Bayes / Categorical Naive Bayes

### Code Example

```python
from sklearn.naive_bayes import GaussianNB

gnb_model = GaussianNB()
gnb_model.fit(X_train, y_train)

y_pred = gnb_model.predict(X_test)
print("Recall Score:", recall_score(y_test, y_pred))
```

---

## 6. KNN – K Nearest Neighbours

KNN is used in both **Classification** and **Regression**.

### Steps

1. **Choose a hyperparameter K** — which is basically odd.
2. **Calculate distance** of the new point from all the data points. After calculating distance, we get the nearest K neighbours.
3. **Predict:**
   - **Classification** → Majority of K neighbors
   - **Regression** → Mean/Average of K neighbours

### Distance Formulas

#### ① Euclidean Distance
$$d = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$$

#### ② Manhattan Distance
$$d = |x_1 - x_2| + |y_1 - y_2|$$

Used when we calculate the data in format of a **grid**. Also used for **High Dimensional Data**.

> ⭐ **KNN is also called a Lazy Learner model.** In training, KNN memorizes the data; computation is done in predictions.

### Code (KNN)

```python
from sklearn.metrics import precision_score, recall_score
from sklearn.preprocessing import StandardScaler

# KNN model
knn_classifier = KNeighborsClassifier(n_neighbors=3)

# Training
knn_classifier.fit(X_train_scaled, y_train)

# Testing
y_pred = knn_classifier.predict(X_test_scaled)
print("Recall Score:", recall_score(y_test, y_pred))
```

> **Note:** In KNN, data should always be **scaled before sending**.

---

## 7. Limitation of KNN

- **Slow at predictions** (not suitable for huge datasets)
- **Sensitive to outliers**
- **Sensitive to feature scaling**
- **Curse of Dimensionality** (High Dimensional Data)

---

## 8. Validation Data

A **validation dataset** is a sample of data kept separate from training data and used to estimate the model's performance while tuning the model's hyperparameters.

### Analogy – Exam Preparation

| Data Type | Analogy |
|-----------|---------|
| Training Data | Your notes used for studying |
| Validation Data | A few practice questions you solve while preparing, to check which study method is good |
| Test Data | The final Exam, used to see real performance |

### Workflow

```
80% Training Data                    20% Test
[Training Data] [Validation Data]   [Test]

Train model → Evaluate on Validation Set
          ↑                        ↓
          ← Tweak model according to result

Pick best model → Confirm results on Test Set
```

---

## 9. Cross Validation

### K-Fold CV

**Example:** 1000 values → 80% training = 800, 20% testing = 200; K=5

**Iteration 1:**

| Fold1 (Validation) | Fold2 | Fold3 | Fold4 | Fold5 | → Accuracy 1 |
|--------------------|-------|-------|-------|-------|--------------|

**Iteration 2:**

| Fold1 | Fold2 (Validation) | Fold3 | Fold4 | Fold5 | → Accuracy 2 |
|-------|--------------------|-------|-------|-------|--------------|

...and so on for K iterations.

We get the **best model which is the average of all iterations**, after which testing is performed.

---

## 10. CV for Hyperparameter Tuning

Uses **GridSearchCV** to find the best hyperparameters using cross validation.

---

## 11. Pipeline in Sklearn

### Problem Without Pipeline

In a typical ML workflow, you do:
1. Missing value handling
2. Encoding
3. Scaling
4. Train model
5. Predict

Every time you train or test the model, you must repeat all steps **manually**. This creates problems like:
- Forgetting a step
- Applying wrong scaling
- Data leakage
- Messy code

### Definition

> **Pipeline** allows us to perform data preprocessing steps one after another **automatically**, and finally use a machine learning model to make predictions.

Pipeline connects all steps into **one fixed process**:

```
Data → Preprocessing → Scaling → Model → Predict
```

### Code

```python
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier())
])
```

---

## Made by Sayan

<a href="https://www.linkedin.com/in/sayanpal04?utm_source=share_via&utm_content=profile&utm_medium=member_android" target="_blank">
  <img src="https://img.shields.io/badge/LinkedIn-Sayan%20Pal-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn - Sayan Pal"/>
</a>

> Connect with me on LinkedIn — click the badge above! 🚀
