# 🧠 Unsupervised Machine Learning — Part I

> *A complete study guide covering Clustering algorithms from fundamentals to implementation.*

![ML Banner](https://img.shields.io/badge/Machine%20Learning-Unsupervised-blueviolet?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)
![Topic](https://img.shields.io/badge/Topic-Clustering-orange?style=for-the-badge)

---

## 📚 Table of Contents

| # | Topic |
|---|-------|
| 01 | [Introduction to Unsupervised ML](#-introduction-to-unsupervised-ml) |
| 02 | [What is Clustering?](#-what-is-clustering) |
| 03 | [K-Means Clustering](#-k-means-clustering) |
| 04 | [Elbow Method for K](#-elbow-method) |
| 05 | [Silhouette Score](#-silhouette-score) |
| 06 | [Random Initialization Trap](#-random-initialization-trap) |
| 07 | [Hierarchical Clustering](#-hierarchical-clustering) |
| 08 | [Dendrogram](#-dendrogram) |
| 09 | [DBSCAN Clustering](#-dbscan-clustering) |
| 10 | [Algorithm Comparisons](#-algorithm-comparisons) |

---

## 🌐 Introduction to Unsupervised ML

> Models are trained using **unlabelled data** — no predefined outputs, no supervision.

### Types of Problems

```
Unsupervised ML
├── 🔵 Clustering          → Group similar unlabeled data points
│                             based on defined similarity metrics
└── 🔴 Anomaly Detection   → Identify rare events or observations
```

**Anomaly Detection** finds outliers — the lone wolves in your data that don't belong to any cluster.

---

## 🔵 What is Clustering?

Clustering groups **similar unlabeled data points** into clusters based on similarity metrics.

### Types of Clustering

| Type | Algorithm |
|------|-----------|
| 🔲 Partition Based | **K-Means** |
| 🌿 Hierarchical | Agglomerative / Divisive |
| 🌊 Density Based | **DBSCAN** |

```
  f₂ ↑
      │    ●●●        ●●
      │   ●●  ●      ● ●●
      │    ●●        ●●
      │
      └──────────────────→ f₁
         Cluster 1    Cluster 2
```

---

## ⚙️ K-Means Clustering

The most popular **partition-based** clustering algorithm.

### Algorithm Steps

```
Step 1  →  Choose K (number of clusters)
Step 2  →  Randomly initialize K centroids
Step 3  →  For every point, calculate distance to ALL centroids
              ↓ minimum distance
           Assign point to nearest centroid
Step 4  →  New centroid = mean of all points in the cluster
Step 5  →  Repeat steps 3 & 4 until convergence
```

### Distance Metrics

| Metric | Formula |
|--------|---------|
| **Euclidean** | `d = √[(x₁−x₂)² + (y₁−y₂)²]` |
| **Manhattan** | `d = |x₁−x₂| + |y₁−y₂|` |

> 💡 **Centroid** = mean position of all current points in a cluster

---

## 📐 Elbow Method

Used to find the **optimal K** value.

### WCSS — Within Cluster Sum of Squares

```
         K    n
WCSS = Σ    Σ  (distance of pointᵢ with nearest centroid)²
        k=1  i=1
```

### Plot WCSS vs K

```
WCSS ↑
(inertia)
  │ ●
  │  ●
  │    ●  ← Elbow Point  ✅ K = 3
  │      ●
  │        ● ●
  └──────────────────→ K
     1  2  3  4  5  6
```

> 🎯 Pick the K where WCSS starts to flatten — that's the **elbow point**!

---

## 📊 Silhouette Score

A quantitative measure of clustering quality.

**Range:** `−1 ≤ S(i) ≤ 1`

```
←─────────────────────────────→
-1                              +1
Bad                            Good
```

### Single Sample Score Calculation

**① a(i)** → Intra-cluster distance (mean distance of all points in same cluster)

```
a(i) = 1/(n−1) × Σ dist(i, j)   where j ∈ Cᵢ
```

**② b(i)** → Nearest cluster distance

```
b(i) = min   [ 1/|Cⱼ| × Σ dist(i, j) ]   where j ∈ Cⱼ
       J ≠ i
```

**③ s(i)** → Final score (if |Cᵢ| > 1)

```
s(i) = [b(i) − a(i)] / max{a(i), b(i)}
```

**④ Overall Score**

```
SS = 1/N × Σ s(i)
```

### Interpretation Table

| Case | Condition | Formula | Meaning |
|------|-----------|---------|---------|
| Case 1 | a(i) > b(i) | s(i) = b(i)/a(i) − 1 < 0 | ❌ Bad clustering |
| Case 2 | a(i) < b(i) | s(i) = 1 − a(i)/b(i) > 0 | ✅ Good clustering |
| Case 3 | a(i) = b(i) | s(i) = 0 | 😐 Borderline |

---

## ⚠️ Random Initialization Trap

Because centroids are **randomly placed**, K-Means can converge to a **local minimum** instead of the global optimal.

```
IDEAL ✅                     RIT ❌
─────────────────────────────────────────────
  ●●  ●●●   ●●●           All points → 1 big cluster
  ●●  ● ●   ●●            or weird splits
  3 clean clusters
```

### Solution: **K-Means++**

> To remove RIT, we use **K-Means++** — and by default, **Sklearn uses K-Means++** automatically!

K-Means++ spreads initial centroids far apart, drastically reducing bad initializations.

---

## 🌿 Hierarchical Clustering

No need to specify K beforehand. **No centroids.**

```
Hierarchical Clustering
├── Agglomerative (Bottom-Up) ← most common
└── Divisive (Top-Down)
```

### Agglomerative Steps

```
1. Each sample starts as its own individual cluster
2. For each cluster → find nearest cluster (distance matrix)
3. Merge 2 closest clusters
4. Repeat until 1 cluster remains
```

### Divisive Steps

```
1. Entire dataset = 1 single cluster
2. Find most spread-out sub-cluster (max gap)
   → Divide into 2 clusters
3. Repeat until each sample is its own cluster
```

---

## 🌳 Dendrogram

A **tree-like diagram** produced by agglomerative clustering.

```
Euclidean
distance ↑
         │         *────────────────* ← K=2
         │         │                │
         │    *────*     *───*      │
         │    │          │   │      │
         │    │    *─────*   │      │
         └────────────────────────────→ Samples
              P₁  P₂  P₃  P₄  P₅  P₆
```

> 🎯 **How to choose K from Dendrogram:**
> Find the **longest vertical line** with **no horizontal crossing** — that's your optimal K!
> *(This is the Suggestive Approach)*

---

## 🔵 DBSCAN Clustering

**Density-Based Spatial Clustering of Applications with Noise**

### Benefits

- ✅ Anomaly / outlier detection
- ✅ Handles **non-linear data**
- ✅ No centroids needed
- ✅ No need to choose K

### Point Classification

| Type | Symbol | Condition |
|------|--------|-----------|
| **Core Point** | ● | Points in ε-neighborhood ≥ min_samples |
| **Border Point** | 🔵 | Points in ε-neighborhood < min_samples |
| **Noise/Outlier** | ✕ | Doesn't belong to any cluster |

### Hyperparameters

```
① ε (Epsilon / radius) ──→ defines the ε-neighborhood radius
         ┌────────────┐
         │     e      │  ← ε-neighborhood
         └────────────┘

② min_samples ──→ defines the density of ε-neighborhood
```

### Core vs Border vs Noise

```
Core Point:     ε-neighborhood has ≥ min_samples points
Border Point:   ε-neighborhood has < min_samples points  
Noise/Outlier:  isolated, fits no cluster
```

### DBSCAN Algorithm Steps

```
1. Pick one unvisited sample
   └→ Check if it's a core point
      └→ Build a new cluster
         └→ Repeat for all ε-neighbors
2. Find the next unvisited sample
3. Repeat
```

---

## ⚖️ Algorithm Comparisons

### K-Means vs Hierarchical

| Feature | K-Means | Hierarchical |
|---------|---------|-------------|
| K specification | Required beforehand | Decided later (dendrogram) |
| Dataset size | Large datasets ✅ | Small–Medium only |
| Time Complexity | O(n·k) | O(n²) |
| Speed | Faster ✅ | Slower |

### K-Means vs DBSCAN (Non-linear)

| Feature | K-Means | DBSCAN |
|---------|---------|--------|
| Shape of clusters | Spherical only | Any shape ✅ |
| Outlier handling | Poor | Excellent ✅ |
| K required | Yes | No ✅ |
| Centroids | Yes | No |

---

## 🔬 Quick Reference Formulas

```python
# Euclidean Distance
d = sqrt((x1-x2)² + (y1-y2)²)

# Manhattan Distance  
d = |x1-x2| + |y1-y2|

# WCSS (K=3 example)
wcss = Σ(i=1 to 3) Σ(j=1 to n) (xj - μk)²

# Silhouette Score
a(i) = (1/n-1) * Σ dist(i,j)          # intra-cluster
b(i) = min(1/|Cj| * Σ dist(i,j))      # nearest cluster
s(i) = (b(i) - a(i)) / max(a(i), b(i))
SS   = (1/N) * Σ s(i)                  # overall
```

---

## 📋 Topics Covered (Index)

```
 ✅ 01. Introduction to Unsupervised ML
 ✅ 02. What is Clustering?
 ✅ 03. K-Means Clustering
 ✅ 04. Elbow Method for K
 ✅ 05. Silhouette Score for K
 ✅ 06. Random Initialization Trap
 ✅ 07. K-Means (code)
 ✅ 08. Choosing K (code)
 ✅ 09. K-Means for Iris Dataset
 ✅ 10. Hierarchical Clustering
 ✅ 11. What is Dendrogram
 ✅ 12. Hierarchical Clustering Code
 ✅ 13. K-Means vs Hierarchical Clustering
 ✅ 14. DBSCAN Clustering
 ✅ 15. DBSCAN (code)
 ✅ 16. K-Means vs DBSCAN (non-linear)
```

---

<div align="center">

---

### ✨ Made by [Sayan](https://www.linkedin.com/in/sayanpal04?utm_source=share_via&utm_content=profile&utm_medium=member_android)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sayan%20Pal-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sayanpal04?utm_source=share_via&utm_content=profile&utm_medium=member_android)

*"The best way to learn Machine Learning is to write it, diagram it, and live it."*

---

</div>
