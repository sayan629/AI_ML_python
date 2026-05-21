# 🚀 Scratch Implementations in Machine Learning

<p align="center">
  <img src="https://img.shields.io/badge/Machine%20Learning-From%20Scratch-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-NumPy-yellow?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Open%20Source-Learning-success?style=for-the-badge" />
</p>

---

# 📚 Table of Contents

1. Introduction  
2. Linear Regression with Gradient Descent  
3. Gradient Descent Derivation  
4. Why Transpose is Used in `np.dot()`  
5. Linear Regression using OLS  
6. Gradient Descent vs OLS  
7. Logistic Regression from Scratch  
8. KNN Classifier from Scratch  
9. Important NumPy Functions  
10. KNN Classifier vs Regressor  
11. Author  

---

# 🌟 Introduction

This repository contains **Machine Learning Algorithms implemented completely from scratch using Python and NumPy**.

The goal of this project is to understand the **core mathematics and intuition behind ML algorithms** instead of directly using libraries like Scikit-Learn.

---

# 📈 Linear Regression with Gradient Descent

Linear Regression tries to fit a straight line:

:contentReference[oaicite:0]{index=0}

Where:

- `θ₀` → Bias  
- `θ₁` → Weight / Coefficient  

---

## 🔥 Steps of Gradient Descent

### 1️⃣ Initialize Parameters
Randomly initialize:

```python
theta0 = 0
theta1 = 0
```

---

### 2️⃣ Prediction Calculation

```python
y_pred = theta0 + theta1 * x
```

---

### 3️⃣ Calculate Gradients

Cost Function:

:contentReference[oaicite:1]{index=1}

Gradient w.r.t bias:

:contentReference[oaicite:2]{index=2}

Gradient w.r.t weight:

:contentReference[oaicite:3]{index=3}

---

### 4️⃣ Update Parameters

:contentReference[oaicite:4]{index=4}

Where:

- `α` → Learning Rate  

---

### 5️⃣ Repeat Until Convergence

Repeat:
- Prediction
- Gradient Calculation
- Parameter Update

Until minimum cost is reached.

---

# 🧠 Why Transpose is Used in `np.dot()` ?

Suppose:

```python
X = [[1],
     [2],
     [3]]

error = [[-1],
         [-1],
         [-1]]
```

Direct multiplication:

```python
X * error
```

❌ Not possible because dimensions are incompatible.

So we use:

```python
X.T @ error
```

After transpose:

```python
X.T = [1 2 3]
```

Now matrix multiplication becomes valid ✅

---

# 📉 Linear Regression using OLS

OLS = Ordinary Least Squares

It uses the **Normal Equation**:

:contentReference[oaicite:5]{index=5}

This gives the **closed-form solution** directly without iterations.

---

## ⚡ NumPy Implementation

```python
import numpy as np

class LinearRegressionOLS:

    def __init__(self):
        self.bias = None
        self.weights = None

    def fit(self, X, y):

        m, n = X.shape

        X_b = np.c_[np.ones((m,1)), X]

        theta = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y

        self.bias = theta[0]
        self.weights = theta[1:]

    def predict(self, X):

        y_pred = self.bias + np.dot(X, self.weights)

        return y_pred
```

---

# ⚔️ Gradient Descent vs OLS

| Gradient Descent | OLS |
|---|---|
| Works well on large datasets | Better for small datasets |
| Handles high-dimensional data | Expensive for many features |
| Supports online learning | Closed-form solution |
| Memory efficient | Matrix inversion costly |

---

# 🔐 Logistic Regression from Scratch

Logistic Regression uses the **Sigmoid Function**:

:contentReference[oaicite:6]{index=6}

Where:

:contentReference[oaicite:7]{index=7}

---

## 🎯 Prediction Rule

```python
if g(z) >= 0.5:
    predict = 1
else:
    predict = 0
```

---

## 📌 Cost Function

:contentReference[oaicite:8]{index=8}

---

## 🔄 Steps

1. Initialize weights  
2. Compute `z`  
3. Apply sigmoid  
4. Compute gradients  
5. Update weights  
6. Repeat  

---

# 🤖 KNN Classifier from Scratch

KNN = K Nearest Neighbors

---

## 🚀 Steps

### 1️⃣ Initialize K

```python
k = 3
```

Usually odd numbers are preferred:

```python
3, 5, 7, 9 ...
```

---

### 2️⃣ Calculate Euclidean Distance


::contentReference[oaicite:9]{index=9}


---

## 🧮 Example

```python
x1 = np.array([1,2])
x2 = np.array([3,4])

distance = np.sqrt(np.sum((x1-x2)**2))
```

Output:

```python
2.828
```

---

### 3️⃣ Sort Distances

```python
np.argsort()
```

Returns indices that would sort the array.

Example:

```python
arr = np.array([50,20,40,10])

np.argsort(arr)
```

Output:

```python
[3,1,2,0]
```

---

### 4️⃣ Majority Voting

```python
np.argmax(np.bincount(knn))
```

---

# 🔥 Important NumPy Functions

---

## 📌 `np.argsort()`

Returns sorted indices.

```python
arr = [50,20,40,10]

np.argsort(arr)
```

Output:

```python
[3,1,2,0]
```

---

## 📌 `np.bincount()`

Counts frequency of non-negative integers.

```python
a = [0,0,1,1,0,0,3,3,5]

np.bincount(a)
```

Output:

```python
[4,2,0,2,0,1]
```

Meaning:

- 0 appears 4 times  
- 1 appears 2 times  
- 2 appears 0 times  
- 3 appears 2 times  

---

## 📌 `np.argmax()`

Returns index of largest value.

```python
np.argmax(np.bincount(a))
```

Output:

```python
0
```

---

# ⚖️ KNN Classifier vs KNN Regressor

| KNN Classifier | KNN Regressor |
|---|---|
| Predicts class | Predicts numerical value |
| Discrete output | Continuous output |
| Uses majority voting | Uses averaging |

---

## 📌 KNN Classifier

```python
majority_class = np.argmax(np.bincount(knn))
```

Example:

```python
[0,1,1,1,0]
```

Prediction:

```python
1
```

---

## 📌 KNN Regressor

```python
prediction = np.mean(knn)
```

Example:

```python
[10,20,30]
```

Prediction:

```python
20
```

---

# 🎯 Final Goal

This repository is designed to help beginners:

✅ Understand ML Mathematics  
✅ Learn NumPy deeply  
✅ Build algorithms from scratch  
✅ Prepare for Interviews  
✅ Improve ML intuition  

---

# 📷 Preview

<p align="center">
  <img src="https://media.giphy.com/media/LmNwrBhejkK9EFP504/giphy.gif" width="500"/>
</p>

---

# 💻 Tech Stack

- Python  
- NumPy  
- Mathematics  
- Machine Learning Fundamentals  

---

# ⭐ Support

If you found this useful:

🌟 Star the repository  
🍴 Fork the project  
📢 Share with friends  

---

# 👨‍💻 Made with Passion by

<p align="center">
  <a href="https://www.linkedin.com/in/sayanpal04?utm_source=share_via&utm_content=profile&utm_medium=member_android">
    <img src="https://img.shields.io/badge/Made%20By-Sayan%20Pal-blue?style=for-the-badge&logo=linkedin"/>
  </a>
</p>

<p align="center">
  <b>✨ “When Sayan touches ML, mathematics becomes intuition.” ✨</b>
</p>
