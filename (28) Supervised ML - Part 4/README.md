# 🌳 Decision Trees — Supervised ML (Part 4)

> *A comprehensive handwritten study guide on Decision Trees, covering theory, math, and implementation.*

---

![Decision Tree Banner](https://img.shields.io/badge/ML-Decision%20Trees-2ecc71?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-Supervised%20Learning-3498db?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-27ae60?style=for-the-badge)

---

## 📋 Table of Contents

- [Introduction to Decision Trees](#-introduction-to-decision-trees)
- [Decision Tree Classifier](#-decision-tree-classifier)
- [Impurity Metrics](#-impurity-metrics)
  - [Entropy](#entropy)
  - [Gini Impurity](#gini-impurity)
  - [Entropy vs Gini Impurity](#entropy-vs-gini-impurity)
- [Information Gain](#-information-gain)
- [Pruning](#-pruning)
  - [Pre-Pruning](#pre-pruning)
  - [Post-Pruning](#post-pruning)
  - [Common Pruning Rules](#common-pruning-rules)
- [Decision Tree Regressor](#-decision-tree-regressor)
  - [Variance Reduction](#variance-reduction)
- [Algorithms](#-algorithms-in-decision-trees)

---

## 🌿 Introduction to Decision Trees

A **Decision Tree** predicts an outcome by asking a sequence of **if-then questions** about the input features.

```
Used in both:
  ├── Classifications
  └── Regressions
```

The tree splits data at each node into branches based on feature values, continuing until it reaches **homogeneous (pure) leaf nodes**.

---

## 🔍 Decision Tree Classifier

In practically one node, data can be classified or divided into two nodes.

**Example — Loan Approval:**

| Credit Score | Employed | Loan Approved |
|:---:|:---:|:---:|
| Low | No | ❌ No |
| Low | Yes | ❌ No |
| Medium | Yes | ✅ Yes |
| High | Yes | ✅ Yes |
| Medium | No | ❌ No |
| High | No | ✅ Yes |

**What we need to learn:**
1. **Degree of purity of a split** → Entropy / Gini Impurity
2. **Feature selection for split** → Information Gain

---

## 📐 Impurity Metrics

### Entropy

> *Entropy measures the **impurity**, disorder, or uncertainty in a dataset.*

$$E(S) = -\sum_{i=1}^{c} P_i \log_2 P_i$$

For **binary classification**:

$$E(S) = -P_y \log_2 P_y - P_n \log_2 P_n$$

| Entropy ↑ | Uncertainty occurs more |
|---|---|
| Entropy ↓ | Certain / sure dataset |

📊 **Entropy value range: [0 → 1]**

**Example calculation (impure node [3Y, 3N]):**
```
E = -(3/6)log₂(3/6) - (3/6)log₂(3/6)
  = -(1/2)log₂(1/2) - (1/2)log₂(1/2)
  = -(1/2)(-1) - (1/2)(-1)
  = 1/2 + 1/2
  = 1  ← Maximum entropy (most impure)
```

**Example calculation (pure node [0Y, 3N]):**
```
E = 0 - (3/3)log₂(3/3)
  = 0 - 1·log₂(1)
  = 0  ← Zero entropy (pure node)
```

---

### Gini Impurity

> *Measures the **likelihood of a random element being misclassified** in a dataset.*

$$GI = 1 - \sum_{i=1}^{c} (P_i)^2$$

📊 **In Binary Classification: max GI = 0.5**

**Example (impure node [3N, 3Y]):**
```
GI = 1 - (Py² + Pn²)
   = 1 - ((3/6)² + (3/6)²)
   = 1 - (1/4 + 1/4)
   = 1 - 1/2
   = 0.5  ← Impure node
```

**Example (pure node [0N, 3Y]):**
```
GI = 1 - ((1)² + 0)
   = 1 - 1
   = 0  ← Pure node ✅
```

---

### Entropy vs Gini Impurity

| Scenario | Entropy | Gini Impurity |
|---|---|---|
| **Training Speed** | Slightly slower (log calculations) | Faster computation (no log operations) |
| **Split Behaviour** | Produces more balanced node partitions | Creates splits quickly, favouring dominating classes |
| **Dataset Size** | Useful for structured datasets with balanced classes | Efficient for large, high-dimensional datasets |
| **Sensitivity to Distribution** | More sensitive to subtle probability differences | Less sensitive to small probability changes |
| **Common Usage** | Preferred when theoretical information gain matters | Others default in libraries like **CART** |

---

## 📈 Information Gain

> *IG is a measure used to **decide which feature to split on**. It measures the reduction in entropy or randomness.*

$$IG = \text{Entropy of Parent} - \text{Weighted Entropy of Children}$$

$$IG_A = H(S) - \sum_{v \in A} \frac{|S_v|}{|S|} \cdot H(S_v)$$

Where:
- `A` = feature that we split on the basis of
- `H(Sv)` = Entropy of child node
- `V` = possible values of A

**Example (Gender split: [2Y, 4N]):**
```
H(S) = -(2/6)log₂(2/6) - (4/6)log₂(4/6) = 0.918

H(Sm) = -(2/3)log₂(2/3) - (1/3)log₂(1/3) = 0.918
H(Sf) = 0  (pure node)

IG = 0.918 - (3/6 × 0.918 + 3/6 × 0)
   = 0.918 - 0.459
   = 0.459
```

> ⭐ **Information Gain is used for Entropy.**
> For Gini Impurity, we use **Gini Gain** = Gini Impurity of root node − weighted GI of children.

---

## ✂️ Pruning

> *Pruning is a technique used in Decision Trees to **remove parts of the tree that are unnecessary** in order to reduce overfitting and improve performance on unseen data.*

### Pre-Pruning

Pre-pruning **stops the tree from growing** before it becomes too complex.

**Conditions to stop:**
- Max depth reached
- Minimum samples
- Minimum information gain

### Post-Pruning

Post-pruning **first builds the full tree**, then removes unnecessary branches.

The most popular way is **Cost Complexity Pruning (CCP)**, which involves one hyperparameter: **ccp_alpha**.

```
Small datasets  ⟹ Pre-Pruning
Large datasets  ⟹ Post-Pruning
```

### Common Pruning Rules

| Parameter | Description |
|---|---|
| `max_depth` | Stop splitting when the tree reaches max depth |
| `min_samples_split` | Node must contain at least N samples to be built |
| `min_samples_leaf` | Leaf must contain at least N samples |
| `max_leaf_nodes` | Limit total number of leaf nodes |
| `min_impurity_decrease` | Only split if impurity reduction exceeds a threshold |

---

## 📉 Decision Tree Regressor

**Steps to make a Decision Tree for Regression:**

1. Decide which feature to split on
2. Split data into two parts
3. Repeat steps 1 & 2 recursively

```
Classification               Regression
─────────────────            ─────────────────
Gini Impurity                Variance (σ²)
    &                        (MAE, MSE...)
Entropy                            ↓
    ↓                     Variance Reduction (VR)
Information Gain
```

> **decision → leaf node/data → mean/avg ← Regression Predictions**

### Variance Reduction

$$VR = V_S - \left(\frac{|S_L|}{|S|} \cdot V_L + \frac{|S_R|}{|S|} \cdot V_R\right)$$

**MAE variance:** $\text{var} = \frac{1}{n}\sum_{i=1}^{n}|y_i - \bar{y}|$

**MSE variance:** $\text{var} = \frac{1}{n}\sum_{i=1}^{n}(y_i - \bar{y})^2$

Where $\bar{y}$ = mean value of data, $y_i$ = i-th value in sample.

**Example — choosing best split for dataset {(1,2),(2,4),(3,6),(4,10)}:**

| | Case 1: X ≤ 2 | Case 2: X ≤ 3 |
|---|---|---|
| Left node | [2, 4] | [2, 4, 6] |
| Right node | [6, 10] | [10] |
| VR | **6.25** | **6.75** ✅ |

> **VR₂ > VR₁ → Case 2 (X ≤ 3) is selected as the better split!**

---

## ⚙️ Algorithms in Decision Trees

| # | Algorithm | Impurity Metric |
|---|---|---|
| (i) | **CART** | Gini Impurity |
| (ii) | **ID3 / C4.5** | Entropy |
| (iii) | **CHAID** | Chi-square |

> 💡 **IQ:** If you are using scikit-learn for the decision tree implementation, which algorithm does sklearn use by default?
> **Answer: CART algorithm** (uses Gini Impurity by default)

---

## 🛠️ Quick Code Reference

```python
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor

# Classifier (default: CART with Gini)
clf = DecisionTreeClassifier(
    criterion='gini',       # or 'entropy'
    max_depth=5,
    min_samples_split=2,
    min_samples_leaf=1,
    ccp_alpha=0.0           # for post-pruning
)

# Regressor
reg = DecisionTreeRegressor(
    criterion='squared_error',  # variance-based
    max_depth=5
)
```

---

## 📚 Key Takeaways

- ✅ Decision Trees ask if-then questions to reach predictions
- ✅ **Entropy** and **Gini Impurity** measure node impurity
- ✅ **Information Gain** / **Gini Gain** selects the best feature to split
- ✅ **Pruning** prevents overfitting (pre = stop early, post = trim after)
- ✅ **Variance Reduction** is used for regression trees instead of entropy
- ✅ scikit-learn uses **CART** by default

---

<div align="center">

---

### 🤝 Made by **[Sayan](https://www.linkedin.com/in/sayanpal04?utm_source=share_via&utm_content=profile&utm_medium=member_android)**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sayan%20Pal-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sayanpal04?utm_source=share_via&utm_content=profile&utm_medium=member_android)

*If this helped you, drop a ⭐ and connect on LinkedIn!*

</div>
