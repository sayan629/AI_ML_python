# 🧠 ML from Scratch — Implementation Notes

> *Hand-crafted notes covering Linear Regression, Logistic Regression, and KNN — implemented from scratch using NumPy.*

---

<p align="center">
  <img src="https://img.shields.io/badge/Machine%20Learning-From%20Scratch-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-NumPy-yellow?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Open%20Source-Learning-success?style=for-the-badge" />
</p>

---

## 📋 Table of Contents

1. [Linear Regression with Gradient Descent](#linear-regression-with-gradient-descent)
2. [Linear Regression with OLS](#linear-regression-with-ols-ordinary-least-squares)
3. [GD vs OLS — When to Use What?](#gd-vs-ols--when-to-use-what)
4. [Logistic Regression](#logistic-regression)
5. [KNN Classifier](#knn-classifier)
6. [NumPy Utilities Used](#numpy-utilities-used)
7. [KNN Classifier vs Regressor](#knn-classifier-vs-regressor)

---

## 📈 Linear Regression with Gradient Descent

### Parameters
| Symbol | Meaning |
|--------|---------|
| `θ₀` | Bias |
| `θ₁` | Coefficient / Weight |

### Algorithm Steps

```
1. Initialize θ₁ & θ₀ with random values
2. Predicted values calculation → h(x) = θ₀ + θ₁x
3. Calculate Gradients → ∂J(θ)/∂θ₀  and  ∂J(θ)/∂θ₁
4. Update: θk = θk − α · ∂J(θ)/∂θk   ← Convergence Theorem
5. Repeat steps 2, 3, and 4 till we reach minima
```

### 📐 Derivation

**Cost Function:**

```
         1   m
J(θ) = ─── · Σ  ( ŷ⁽ⁱ⁾ - y⁽ⁱ⁾ )²
        2m  i=1

        1    m
     = ─── · Σ  ( θ₀ + θ₁x⁽ⁱ⁾ - y⁽ⁱ⁾ )²
        2m  i=1
```

**Gradient w.r.t. θ₀:**

```
∂J(θ)     1   m
───── = ─── · Σ  ( ŷ⁽ⁱ⁾ - y⁽ⁱ⁾ )
 ∂θ₀     m  i=1

  ⟹  (1/m) * np.sum(y_pred - y)
```

**Gradient w.r.t. θ₁:**

```
∂J(θ)     1   m
───── = ─── · Σ  x⁽ⁱ⁾ · ( ŷ⁽ⁱ⁾ - y⁽ⁱ⁾ )
 ∂θ₁     m  i=1

  ⟹  (1/m) * np.dot(X.T, y_pred - y)
```

> **Why transpose of X in `np.dot()`?**
> Matrix multiplication requires compatible shapes. Since X is a column vector `(n×1)` and `(y_pred - y)` is also `(n×1)`, direct multiplication is not possible. Taking `X.T` gives shape `(1×n)`, making the dot product valid → result is a scalar.

---

## 📊 Linear Regression with OLS (Ordinary Least Squares)

OLS gives a **closed-form solution** called the **Normal Equation**:

```
┌─────────────────────────────────┐
│  θ = (Xᵀ · X)⁻¹ · Xᵀ · y        │  ← Closed Form Equation
└─────────────────────────────────┘
```

### `np.c_` Function
Column-wise concatenation — joins arrays side by side as columns.

```python
import numpy as np

m = 5
X = np.array([[1], [2], [3], [4]])   # 4 rows (samples), 1 column (feature)
X_b = np.c_[np.ones((m, 1)), X]
print(X_b)
# Output:
# [[1, 1]
#  [1, 2]
#  [1, 3]
#  [1, 4]]
```

### OLS Implementation

```python
class LinearRegressionOLS():
    def __init__(self):
        self.bias = None
        self.weights = None

    def fit(self, X, y):
        m, n = X.shape
        X_b = np.c_[np.ones((m, 1)), X]
        # np.linalg.inv() → finds inverse of a square matrix
        theta = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y
        self.bias = theta[0]
        self.weights = theta[1:]

    def predict(self, X):
        y_pred = self.bias + np.dot(X, self.weights)
        return y_pred
```

---

## ⚔️ GD vs OLS — When to Use What?

| Scenario | Recommended |
|----------|------------|
| Very large data (Big Data) | ✅ Gradient Descent |
| Many features (high-dimensional) | ✅ Gradient Descent |
| Regularization required | ✅ Gradient Descent |
| Streaming / online learning | ✅ Gradient Descent |
| Dataset doesn't fit in memory | ✅ Gradient Descent |
| Small data & few features | ✅ OLS |

> **Time Complexity:**
> - OLS = O(n³) — high TC, so model efficiency is not good
> - GD = O(n·m) — scales well with data

---

## 🔵 Logistic Regression

### Sigmoid Function

```
           
Sigmoid Function
g(z)=11+e−xg(z) = \frac{1}{1 + e^{-x}}
g(z)=1+e−x1​   where  z = θ₀ + θ₁x  =  θᵀx
        
```

```
g(z) ≥ 0.5  →  predict 1
g(z) < 0.5  →  predict 0
```

### Cost Function (Log Loss)

```
          1   m
J(θ) = - ─── Σ  [ y⁽ⁱ⁾ · log(ŷ⁽ⁱ⁾)  +  (1 - y⁽ⁱ⁾) · log(1 - ŷ⁽ⁱ⁾) ]
          m  i=1
```

### Gradients

```
∂J(θ)     1
───── = ─── · (ŷ - y)
 ∂θ₀     m

∂J(θ)     1
───── = ─── · (ŷ - y) · x
 ∂θ₁     m
```

### Algorithm Steps

```
1. Initialize θ₀ & θ₁
2. GD:
     z      = θ₀ + θ₁x
     y_pred = sigmoid(z)
3. Compute db = ∂J/∂θ₀  and  dw = ∂J/∂θ₁
4. θk = θk − α · ∂J(θ)/∂θk
5. Repeat steps 2, 3, & 4
```

---

## 🔍 KNN Classifier

### Algorithm Steps

```
1. Initialize K with odd numbers (3, 5, 7, 9, ...)
2. Calculate Euclidean distance from new (test) datapoint to all training datapoints
3. Sort K points as per minimum distance → np.argsort()
4. KNN → majority vote (0 or 1)
```

### Euclidean Distance Formula

```
d = √[ (x₂ - x₁)² + (y₂ - y₁)² ]
```

**Example:**
```
x₁ = [1, 2],  x₂ = [3, 4]
d = √((1-3)² + (2-4)²) = √(4+4) = √8 = 2√2 ≈ 2.83
```

**In Code:**
```python
x1 = np.array([1, 2])
x2 = np.array([3, 4])
d = np.sqrt(np.sum((x1 - x2) ** 2))
```

---

## 🧰 NumPy Utilities Used

### `np.argsort()`
Returns the **indices** that would sort an array.

```python
arr = np.array([50, 20, 40, 10])
sorted_arr = np.argsort(arr)
print(sorted_arr)  # [3, 1, 2, 0]
# 10 at index 3, 20 at index 1, 40 at index 2, 50 at index 0
```

### `np.bincount()`
Counts how many times each **non-negative integer** appears.

```python
a = [0, 0, 1, 1, 0, 0, 3, 3, 5]
np.bincount(a)
# Output: [4, 2, 0, 2, 0, 1]
# 0→4 times, 1→2 times, 2→0 times, 3→2 times, 4→0 times, 5→1 time
```

### `np.argmax()`
Returns the **index of the largest element**.

```python
np.argmax(np.bincount(a))  # → 0 (most frequent element)
```

---

## 🆚 KNN Classifier vs Regressor

| | KNN Classifier | KNN Regressor |
|--|----------------|---------------|
| **Output** | Discrete (class) | Continuous (number) |
| **Prediction** | Majority voting | Average (mean) |
| **Formula** | `np.argmax(np.bincount(knn))` | `np.mean(knn)` |
| **Example** | `[0,1,1,1,0]` → **1** | `[10,20,30]` → **(10+20+30)/3 = 20** |

---

## 📦 Full Section Index

| # | Topic |
|---|-------|
| 1 | Section Introduction |
| 2 | Linear Regression with Gradient Descent |
| 3 | LR with GD (Step 1) |
| 4 | LR with GD (Step 2) |
| 5 | LR with GD (Step 3) |
| 6 | LR with GD (Step 4) |
| 7 | Linear Regression (with OLS) |
| 8 | LR with Gradient Descent v/s OLS |
| 9 | Logistic Regression (Steps) |
| 10 | Logistic Regression Implementation |
| 11 | KNN Classifier (Steps) |
| 12 | KNN Classifier Implementation |

---

<div align="center">

---

## 📷 Preview
<p align="center">
  <img src="https://media.giphy.com/media/LmNwrBhejkK9EFP504/giphy.gif" width="500"/>
</p>

---

### 🤝 Connect with Me

<a href="https://www.linkedin.com/in/sayanpal04?utm_source=share_via&utm_content=profile&utm_medium=member_android">
  <img src="https://img.shields.io/badge/LinkedIn-Sayan%20Pal-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn - Sayan Pal"/>
</a>

---

**Made by [Sayan](https://www.linkedin.com/in/sayanpal04?utm_source=share_via&utm_content=profile&utm_medium=member_android)** 🚀

*"The best way to learn ML is to build it from scratch."*

</div>
