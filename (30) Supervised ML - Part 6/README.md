# 🚀 Supervised ML — Ensemble Methods & Boosting

<div align="center">

![ML Banner](https://img.shields.io/badge/Machine%20Learning-Ensemble%20Methods-blueviolet?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Study%20Notes-success?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Boosting%20%7C%20Voting%20%7C%20Stacking-orange?style=for-the-badge)

<br/>

> *"Alone we can do so little; together we can do so much."*
> — A perfect motto for **Ensemble Learning**

</div>

---

## 📚 Table of Contents

| # | Topic | Type |
|---|-------|------|
| 1 | [Gradient Boosting Regressor](#-gradient-boosting-regressor) | Regression |
| 2 | [Gradient Boosting Classifier](#-gradient-boosting-classifier) | Classification |
| 3 | [Mathematical Representation of GB](#-mathematical-representation) | Theory |
| 4 | [AdaBoost (Adaptive Boosting)](#-adaboost-adaptive-boosting) | Boosting |
| 5 | [Other Boosting Algorithms](#-other-boosting-algorithms) | XGBoost / LightGBM / CatBoost |
| 6 | [Homogeneous vs Heterogeneous Ensemble](#-homogeneous-vs-heterogeneous-ensemble) | Comparison |
| 7 | [Voting](#-voting) | Ensemble |
| 8 | [Stacking & Blending](#-stacking--blending) | Ensemble |

---

## 🌲 Gradient Boosting Regressor

> Gradient Boosting works for **both classification and regression**.
> By default, it uses **Decision Trees** as weak learners.

### ⚙️ Steps (Regression)

```
1️⃣  Fit a simple model F₀  →  mean = ŷ = Pseudo
2️⃣  Calculate residuals (y - ŷ) for all samples  →  Rᵢ
3️⃣  Train Decision Tree on (X, R)  →  output
4️⃣  Calculate new ŷ:
        Pred₁ = Pseudo + η · DT₁        [η = Learning Rate]
5️⃣  Repeat steps 2, 3 & 4
```

### 🔄 Visual Pipeline

```
(X, y)                 (X, R₁)              (X, R₃)          (X, R₅)
   ↓                      ↓                    ↓                 ↓
[Simple Model F₀]      [ DT₁ ]             [ DT₂ ]           [ DT₃ ] ---
   ↓                      ↓                    ↓
   R₁ ————————→  R₂ → ŷ → R₃ ————→  R₄ → ŷ → R₅
```

### 📊 Example Walkthrough

**Dataset:**

| SEM | BRANCH | GIPA |
|-----|--------|------|
| 1   | CS     | 8    |
| 2   | ECE    | 6    |
| 3   | ME     | 8    |
| 4   | CS     | 7    |
| 5   | ECE    | 9    |

**Learning Rate η = 0.1**

```
Step 1:  mean = (8+6+8+7+9)/5 = 7.6  →  Pseudo = 7.6

Step 2 & 4: Pred₁ = 7.6 + 0.1 × 0.3 = 7.63
```

**Iteration Table:**

| SEM | BRANCH | GIPA (y) | R₁ = y - 7.6 | Predicted R₂ (DT) | ŷ (Pred) | R₃ = y - ŷ |
|-----|--------|-----------|---------------|-------------------|-----------|-------------|
| 1   | CS     | 8         | 0.4           | 0.3               | 7.63      | 0.37        |
| 2   | ECE    | 6         | −1.6          | −1.4              | 7.46      | −1.46       |
| 3   | ME     | 8         | 0.4           | 0.2               | 7.62      | 0.38        |
| 4   | CS     | 7         | −0.6          | −0.3              | 7.57      | −0.57       |
| 5   | ECE    | 9         | 1.4           | 1.6               | 7.76      | 1.24        |

**Final Formula:**
```
F(x) = F₀(x) + f₁
```

---

## 🧠 Mathematical Representation

```
Full Equation:
F(x) = f₀(x) + f₁(x) + f₂(x) + ... + fₘ(x)

Simplified (Recursive):
╔══════════════════════════════════════╗
║  Fₘ(x) = Fₘ₋₁(x) + η · fₘ(x)          ║
╚══════════════════════════════════════╝

Where:
  m    → boosting steps
  η    → learning rate
  Fₘ   → model after m steps
  Fₘ₋₁ → model after (m-1) steps
  fₘ   → weak learner (small DT)
```

---

## 🌿 Gradient Boosting Classifier

### ⚙️ Steps (Classification)

```
1️⃣  Simple model → calculate log odds
        F₀ = log(P / 1-P)

2️⃣  Calculate residuals (y - ŷ)

3️⃣  Fit DT on (X, R₁)

4️⃣  Convert predicted residual → probability (ŷ)
        using Sigmoid function σ(F₀)

Mathematical Equation:
        F₁(x) = F₀(x) + η · f₁(x)
```

---

## ⚡ AdaBoost (Adaptive Boosting)

> *It combines multiple **weak classifiers** to form a **strong classifier** by **reweighting misclassified samples** in each iteration.*

### 🎓 Analogy

```
📚 Round 1: Some students get answers wrong...
       ↓
🔍 Focus on Mistakes → "Let's review this!"
       ↓
✅ Round 2: Students Get Better!

             Focused Help → Better Results! 🚀
```

### 🌳 What is a Decision Tree Stump?

> A Decision Tree with only **a single split** (depth = 1).

```
         ◯
        / \
       ◯   ◯
```

### ⚙️ Steps to Perform AdaBoost

```
Initialize:  wᵢ = 1/N   (ensures Σwᵢ = 1)

1️⃣  Start with a weak learner

2️⃣  Calculate weighted error (Total Error):
        ε = Σ wᵢ · 1      (for misclassified)

3️⃣  Calculate stump importance / learner weight:
        α = ½ ln((1-ε) / ε)

4️⃣  Update all sample weights:
        Incorrect:  wᵢ' = wᵢ · eᵅ    (↑ weight)
        Correct:    wᵢ' = wᵢ · e⁻ᵅ   (↓ weight)

5️⃣  Normalize new weights:
        wᵢ_new / Σwᵢ_new

6️⃣  Repeat for a new weak learner with weighted data

7️⃣  Final output (weighted voting):
        F(x) = α₁f₁(x) + α₂f₂(x) + ... + αₘfₘ(x)
```

### 📊 Example — Spam Detection

**Dataset:**

| Email Length | Num of Links | SPAM | wᵢ  | New wᵢ |
|-------------|--------------|------|-----|--------|
| 1200        | 10           | Yes  | 1/6 | 0.07   |
| 800         | 0            | No   | 1/6 | 0.07   |
| 200         | 2            | Yes  | 1/6 | 0.37   |
| 300         | 1            | No   | 1/6 | 0.07   |
| 400         | 2            | No   | 1/6 | 0.07   |
| 900         | 8            | Yes  | 1/6 | 0.07   |

```
Stump: Limit ≤ 2  →  [3N, 9Y]
           No ↙       ↘ Yes
        [3N, 1Y]    [0N, 2Y]

ε = Σwᵢ = 1/6
α = ½ ln((1-ε)/ε) ≈ 0.805

Incorrect wᵢ' = wᵢ · eᵅ ≈ 0.37
Correct   wᵢ' = wᵢ · e⁻ᵅ ≈ 0.074
```

---

## 🏆 Other Boosting Algorithms

### ⚡ XGBoost (Extreme Gradient Boosting)

| ✅ Pros | ❌ Cons |
|---------|---------|
| Extreme Gradient Boosting | Slower to train on large datasets |
| Optimized & scalable version of GB | |
| Very accurate for competitions & real-world tasks | |
| Sparsity aware — handles sparse data well | |
| Prevents overfitting through **L1 & L2 regularization** | |

---

### 💡 LightGBM (Light Gradient Boosting Machine)

| ✅ Pros | ❌ Cons |
|---------|---------|
| Uses less memory & swift computations | Can overfit small datasets |
| Histogram-based: speeds up training by binning continuous features | |
| Extremely fast on large datasets | |

---

### 🐱 CatBoost (Categorical Boosting)

| ✅ Pros | ❌ Cons |
|---------|---------|
| Developed by Yandex, optimized for categorical features | Slightly slower than LightGBM on large numeric-only datasets |
| Automatically encodes categorical variables | |
| Uses symmetric trees for balanced splits | |

---

## 🔀 Homogeneous vs Heterogeneous Ensemble

```
                    Ensemble Learning
                          │
            ┌─────────────┴─────────────┐
            │                           │
    Homogeneous                   Heterogeneous
     Ensemble                      Ensemble
    ┌────────┐                   ┌──────────┐
    │Bagging │                   │  Voting  │
    │Boosting│                   │ Stacking │
    └────────┘                   └──────────┘
```

| Feature | Homogeneous | Heterogeneous |
|---------|-------------|---------------|
| Base Learners | Same type | Different types |
| Examples | Bagging, Boosting | Voting, Stacking |
| Diversity | From data/sampling | From model types |

---

## 🗳️ Voting

> Voting works for **both regression and classification**.

```
               Log. Reg.
              [model 1] ──── P₁ ──┐
                                  │
Datasets ───  SVC                 ├──► VOTING ──► Final
              [model 2] ──── P₂ ──┤
                                  │
              DT                  │
              [model 3] ──── P₃ ──┘

★ Classification → majority vote
★ Regression     → mean

Helps:
  Model Strength → Combine
  Weakness       → Reduce
```

---

## 🧱 Stacking & Blending

### Stacking

```
              [model 1] ─── P₁ ──┐
                                 │
Datasets ──── [model 2] ─── P₂ ──┼──► [meta model] ──► final prediction
                                 │
              [model 3] ─── P₃ ──┘
```

> There is overfitting risk in stacking, so it uses techniques to prevent it:
> 1. **K-Fold CV** (K-fold method)
> 2. **Blending**

---

### 🫐 Blending

```
Dataset splits into:  [Train] [Validation] [Test]

Each model trains on Train+Validation+Test:
  model 1 → [Train | Validation | Test]
  model 2 → [Train | Validation | Test]
  model 3 → [Train | Validation | Test]

Validation predictions → Val-Pred1, Val-Pred2, Val-Pred3
                               ↓ train
                         [Meta Model]
                               ↓ test
                    Test-Pred1, Test-Pred2  →  Test meta set
```

---

## 🧬 Quick Reference Cheat Sheet

```
┌─────────────────┬──────────────────────────────────────────────┐
│   Algorithm     │   Key Idea                                   │
├─────────────────┼──────────────────────────────────────────────┤
│ Gradient Boost  │ Fit DTs on residuals sequentially            │
│ AdaBoost        │ Reweight misclassified samples               │
│ XGBoost         │ GB + L1/L2 regularization                    │
│ LightGBM        │ Histogram-based, fast on large data          │
│ CatBoost        │ Handles categorical features natively        │
│ Voting          │ Combine different models by vote/mean        │
│ Stacking        │ Use predictions as input to meta-model       │
│ Blending        │ Stacking with held-out validation set        │
└─────────────────┴──────────────────────────────────────────────┘
```

---

## 📖 Course Progress

> **Section 33 — Supervised ML (Part 6)**

- [x] Gradient Boosting Regressor 
- [x] GB Classifier Intuition 
- [x] GB Regressor Code 
- [x] GB Classifier Code 
- [x] AdaBoost Intuition 
- [x] AdaBoost Code 
- [x] Other Boosting Algorithms 
- [x] XGBoost Code 
- [x] Homogeneous vs Heterogeneous Ensemble 
- [x] Voting Logic 
- [x] Voting Code 
- [x] Stacking Logic 
- [x] What is Blending? 
- [x] Stacking Code

---

<div align="center">

---

### 🤝 Connect with the Author

<a href="https://www.linkedin.com/in/sayanpal04?utm_source=share_via&utm_content=profile&utm_medium=member_android">
  <img src="https://img.shields.io/badge/Made%20by%20Sayan-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="Made by Sayan - LinkedIn"/>
</a>

*Click the badge to connect on LinkedIn* 🔗

---

* ML Engineering Journey*

</div>
