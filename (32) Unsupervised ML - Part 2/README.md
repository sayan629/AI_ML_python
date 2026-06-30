# 🧠 Unsupervised Machine Learning — Part 2

> *Dimensionality Reduction · Anomaly Detection · Outlier Detection*

![ML Banner](https://img.shields.io/badge/Machine%20Learning-Unsupervised-blueviolet?style=for-the-badge&logo=python&logoColor=white)
![PCA](https://img.shields.io/badge/PCA-Principal%20Component%20Analysis-blue?style=for-the-badge)
![Anomaly Detection](https://img.shields.io/badge/Anomaly-Detection-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Notes%20Complete-brightgreen?style=for-the-badge)

---

## 📋 Table of Contents

1. [Dimensionality Reduction](#-dimensionality-reduction)
2. [What is PCA?](#-what-is-pca)
3. [PCA — Step by Step](#-pca--step-by-step)
4. [Complete PCA Flow](#-complete-pca-flow)
5. [Anomaly Detection](#-anomaly-detection)
6. [Isolation Forest](#-isolation-forest-for-anomaly-detection)
7. [DBSCAN for Anomalies](#-dbscan-for-anomaly-detection)
8. [LOF for Anomalies](#-lof-local-outlier-factor-for-anomaly-detection)

---

## 📐 Dimensionality Reduction

### ⚠️ Curse of Dimensionality

> When the number of dimensions/features increases, machine learning problems become **more difficult**.

```
More Features → More Problems 😓
```

| Problem | Description |
|--------|-------------|
| 📦 **Data Sparsity** | More dimensions → More empty spaces |
| 📏 **Distance becomes meaningless** | In high dimensions, all distances become almost equal (KNN & K-Means fail) |
| 💻 **Expensive Computation** | More features = more storage + more calculations |
| 📉 **Model Performance Decrease** | Too many features introduce noise and irrelevant information |

---

### 🔧 Techniques to Reduce Dimensions

```
┌─────────────────────────────────────────────────────────┐
│              DIMENSIONALITY REDUCTION                   │
├───────────────────┬─────────────────────────────────────┤
│ Feature Selection │ Remove redundant features OR        │
│                   │ keep only important features        │
├───────────────────┼─────────────────────────────────────┤
│ Feature           │ Transform original features into a  │
│ Transformation    │ new set of features (combinations)  │
│ (e.g. PCA, LDA)   │                                     │
├───────────────────┼─────────────────────────────────────┤
│ Regularization    │ Naive Bayes, Linear Regression with │
│                   │ Regularization                      │
└───────────────────┴─────────────────────────────────────┘
```

### 🔗 Feature Selection via Correlation Matrix

```
Feature changes → Output changes
─────────────────────────────────────────────
   ↑  →  ↑     (+ve Correlation)
   ↑  →  ↓     (-ve Correlation)
   ↑  →  No Change   (No Correlation)
```

---

## 🔍 What is PCA?

**PCA (Principal Component Analysis)** is a **Feature Transformation / Dimensionality Reduction** technique.

### 💡 PCA Intuition

```
Spread of data = Variance = Information
Higher Variance = More Information 🎯
```

**Steps to understand PCA:**

1. Start with the original dataset having many features
2. Analyze relationships among features
3. Combine or transform features into a smaller set of **new features**
4. Keep the most informative transformed features → discard the rest

---

## 🧮 PCA — Step by Step

### Step 1 — Standardize the Data (Z-Score Normalization)

$$x_{std} = \frac{x - \mu}{\sigma}$$

### Step 2 — Compute the Covariance Matrix

> *How much do feature f₁ and f₂ vary with each other?*

$$\text{Cov}(X, Y) = \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})$$

Matrix form:
```
         x(f₁)        y(f₂)
A =  x [ Var(x)    Cov(x,y) ]
     y [ Cov(y,x)  Var(y)   ]
```

### Step 3 — Compute Eigenvectors & Eigenvalues

> Find the best fit line — the **principal component**.

A best-fit line satisfies:
- **(i)** d₁ (perpendicular distance) can be **minimized** for all samples  
  **OR**
- **(ii)** d₂ (projected distance) can be **maximized** for all samples

$$\text{Maximize} \sum_{i=1}^{n} d_i^2$$

```
┌─────────────────────────────────────────────────┐
│         KEY EQUATION OF PCA                     │
│                                                 │
│              A · v = λ · v                      │
│                                                 │
│   A = Covariance Matrix                         │
│   v = Eigenvector (unit vector → PC1)           │
│   λ = Eigenvalue (variance captured by PC1)     │
└─────────────────────────────────────────────────┘
```

- **Eigenvector** → unit vector → **PC1** (where `||v|| = 1`)
- **Eigenvalue** → how much variance PC1 captures

### Step 4 — Select Important Features

```
var(PC1) >> var(PC2)
→ PC1 becomes new feature, PC2 is dropped
```

#### Feature Selection Based on PCA:
```
PC1(x) > PC2(y)?  →  PC1(x) selected ✅
PC1(x) < PC2(y)?  →  PC2(y) selected ✅
```

---

## 🔄 Complete PCA Flow

```
         Dataset
            │
            ▼
     Calculate Mean
            │
            ▼
       Center Data
            │
            ▼
    Covariance Matrix
            │
            ▼
  Eigenvalues & Eigenvectors
            │
            ▼
     Find PC₁, PC₂ ...
            │
            ▼
       Project Data
            │
            ▼
      Select Top PCs
            │
            ▼
     Train ML Model 🚀
```

### Visual PCA Steps Illustrated

```
Step 1: Data spread         Step 2: Center at mean
  d₂↑                        d₂↑
  |  | | | | |               |   • • •
  |  | | | | |       →    mean*
  └──────────→f₁            └────────→f₁
                                    mean

Step 3: Find origin         Step 4: Eigenvectors
  d₂↑                        d₂↑
  |     X←─ •                |
  |   •                      |
  └──────────→f₁             └──────────→f₁

Step 5: Project             Step 6: New axes (PCA rotates)
  d₂↑    PC₁                 d₂↑  /PC₁(80%)
  |  ↗                       |  /
  | /                        | /
  └──────────→f₁             └────→f₁
               \PC₂(20%)
```

---

## 🚨 Anomaly Detection

### Where Is It Used?

| Domain | Use Case |
|--------|----------|
| 💳 Finance | Credit card fraud detection |
| 🏭 Manufacturing | Defect detection |
| 🏥 Medical | Diagnosis of rare diseases |
| 🔐 Cyber Security | Intrusion detection |
| 🤖 Bot Detection | Identifying automated traffic |

### Outlier Detection Techniques

```
┌─────────────────────────────────┐
│     OUTLIER DETECTION           │
├─────────────────────────────────┤
│  1. DBSCAN  → noise (-1)        │
│               ↓ outliers        │
│  2. Isolation Forest            │
│  3. LOF (Local Outlier Factor)  │
└─────────────────────────────────┘
```

---

## 🌲 Isolation Forest for Anomaly Detection

### Core Idea

Anomalies are **easier to isolate** → they have a **shorter path length** in isolation trees.

```
Shorter Path Length → Outlier / Anomaly 🚨
Long Path Length    → Normal ✅
```

### Steps

1. **Construct** isolation trees
2. **Calculate** path length for each point
3. **Build multiple trees** and compute the **average path length**
4. Use average path length to calculate the **Anomaly Score**

### 🎯 Anomaly Score Formula

$$AS(x) = 2^{-\frac{E(h(x))}{c(n)}}$$

| Symbol | Meaning |
|--------|---------|
| `x` | One sample |
| `n` | Size of dataset |
| `E(h(x))` | Average path length of x in all trees |
| `c(n)` | Mean path length (normalization) |

### Score Interpretation

```
AS(x) ≈ 1    → Outlier 🔴
AS(x) ≈ 0.5  → Borderline 🟡
AS(x) ≈ 0    → Normal 🟢
```

> When `E(h(x)) <<< c(n)` → `AS(x) ≈ 1` → **Anomaly!**

---

## 🔵 DBSCAN for Anomaly Detection

**DBSCAN** = Density-Based Spatial Clustering of Applications with Noise

### Point Types

```
┌──────────────────────────────────────────────────┐
│  Core Point   = ε-neighbourhood samples ≥ min_pts│
│  Border Point = < min_pts but near a core point  │
│  Noise Point  = < min_pts AND far from core pts  │
└──────────────────────────────────────────────────┘
```

### Steps

1. Choose `ε` (epsilon) and `min_points`
2. Pick an unvisited point
3. Count neighbours within `ε`:
   - If neighbours ≥ min_pts → **Core Point** ✅
   - Else → **Candidate for Border or Noise**
4. Expand cluster by connecting density-reachable points
5. Points that cannot join any cluster → labeled as **Noise** 🚨

### Tuning `min_samples`

```
min_samples too low  → noise becomes normal sample
min_samples too high → normal data becomes noise

Rule of thumb: min_samples ≈ 2 × features
```

### Tuning `ε` (Epsilon)

| Dimension | Feature Count | ε Range |
|-----------|--------------|---------|
| Low | < 10f | 0.5 – 1 |
| Medium | 10–20f | 1 – 2 |
| High | > 20f | > 2 |

---

## 🎯 LOF (Local Outlier Factor) for Anomaly Detection

LOF detects **local outliers** — points that are anomalous relative to their *local neighborhood*, not globally.

```
d₂↑        local outlier ←●
|     • • •     ↗
|   • •    • •
|
|  ●  ← global outlier
└──────────────→f₁
```

### Steps

**1. Choose value K**

**2. For each point, find its K nearest neighbors**

**3. Calculate Reachability Distance**

$$\text{reach-dist}(P, O) = \max(k\text{-distance}(O),\ d(P, O))$$

Where:
- `d(P, O)` = actual distance
- `k-distance(O)` = distance to O's kth neighbor

**4. Calculate LRD (Local Reachability Density)**

$$LRD(P) = \frac{1}{\text{Average reach-distance of P's neighbors}}$$

**5. Calculate LOF Score**

$$LOF(P) = \frac{\text{Average LRD of neighbors}}{LRD(P)}$$

### LOF Score Interpretation

```
LOF ≈ 1          → Normal ✅
LOF > 1          → Outlier 🔴
LOF >> 1         → Strong Anomaly 🚨
```

---

## 📊 Quick Comparison: Anomaly Detection Methods

| Method | Best For | Key Parameter | Anomaly Score |
|--------|----------|---------------|---------------|
| **Isolation Forest** | High-dimensional data | n_estimators | Score ≈ 1 |
| **DBSCAN** | Density-based clusters | ε, min_samples | Label = -1 |
| **LOF** | Local density anomalies | K | LOF > 1 |

---

## 🧩 Key Formulas Summary

```
┌────────────────────────────────────────────────────────┐
│  Z-Score:      x_std = (x - μ) / σ                    │
│                                                        │
│  Covariance:   Cov(X,Y) = (1/n)Σ(xᵢ-x̄)(yᵢ-ȳ)       │
│                                                        │
│  PCA Equation: A·v = λ·v                              │
│                                                        │
│  Anomaly Score: AS(x) = 2^(-E(h(x))/c(n))            │
│                                                        │
│  LRD(P) = 1 / (Avg reach-dist)                        │
│                                                        │
│  LOF(P) = Avg LRD(neighbors) / LRD(P)                 │
└────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack Used

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=matplotlib&logoColor=white)

---

## 📁 Topics Covered

- [x] Dimensionality Reduction
- [x] What is PCA?
- [x] PCA Step by Step
- [x] PCA (Code)
- [x] Anomaly Detection
- [x] Isolation Forest for Anomalies + Code
- [x] DBSCAN for Anomalies
- [x] DBSCAN for Anomalies (Code)
- [x] LOF for Anomalies
- [x] LOF for Anomalies (Code)

---

<div align="center">

---

### ✨ Made by

<a href="https://www.linkedin.com/in/sayanpal04?utm_source=share_via&utm_content=profile&utm_medium=member_android">
  <img src="https://img.shields.io/badge/Sayan%20Pal-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0077B5" alt="Sayan Pal LinkedIn" />
</a>

**🚀 Sayan Pal**

*Machine Learning Enthusiast | Notes & Knowledge Sharing*

> *"Learning is not attained by chance, it must be sought for with ardor and attended to with diligence."*

[![LinkedIn](https://img.shields.io/badge/Connect%20on%20LinkedIn-Sayan%20Pal-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/sayanpal04?utm_source=share_via&utm_content=profile&utm_medium=member_android)

---

*⭐ If you found these notes helpful, give this repo a star!*

</div>
