<div align="center">

<!-- Banner SVG -->
<svg width="900" height="220" viewBox="0 0 900 220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0a0f1e"/>
      <stop offset="50%" style="stop-color:#0d1b3e"/>
      <stop offset="100%" style="stop-color:#0a0f1e"/>
    </linearGradient>
    <linearGradient id="accent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00d4ff"/>
      <stop offset="100%" style="stop-color:#7b61ff"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <!-- Background -->
  <rect width="900" height="220" fill="url(#bg)" rx="12"/>
  <!-- Grid lines -->
  <g opacity="0.08" stroke="#00d4ff" stroke-width="0.8">
    <line x1="0" y1="44" x2="900" y2="44"/>
    <line x1="0" y1="88" x2="900" y2="88"/>
    <line x1="0" y1="132" x2="900" y2="132"/>
    <line x1="0" y1="176" x2="900" y2="176"/>
    <line x1="90" y1="0" x2="90" y2="220"/>
    <line x1="180" y1="0" x2="180" y2="220"/>
    <line x1="270" y1="0" x2="270" y2="220"/>
    <line x1="360" y1="0" x2="360" y2="220"/>
    <line x1="450" y1="0" x2="450" y2="220"/>
    <line x1="540" y1="0" x2="540" y2="220"/>
    <line x1="630" y1="0" x2="630" y2="220"/>
    <line x1="720" y1="0" x2="720" y2="220"/>
    <line x1="810" y1="0" x2="810" y2="220"/>
  </g>
  <!-- Matrix brackets left -->
  <g filter="url(#glow)" opacity="0.6">
    <path d="M60 40 L45 40 L45 180 L60 180" stroke="#00d4ff" stroke-width="2.5" fill="none"/>
    <path d="M840 40 L855 40 L855 180 L840 180" stroke="#7b61ff" stroke-width="2.5" fill="none"/>
  </g>
  <!-- Floating numbers -->
  <g font-family="'Courier New', monospace" font-size="11" opacity="0.2" fill="#00d4ff">
    <text x="75" y="65">1</text><text x="105" y="65">0</text><text x="135" y="65">0</text>
    <text x="75" y="95">0</text><text x="105" y="95">1</text><text x="135" y="95">0</text>
    <text x="75" y="125">0</text><text x="105" y="125">0</text><text x="135" y="125">1</text>
    <text x="735" y="65">2</text><text x="765" y="65">0</text><text x="795" y="65">0</text>
    <text x="735" y="95">0</text><text x="765" y="95">3</text><text x="795" y="95">0</text>
    <text x="735" y="125">0</text><text x="765" y="125">0</text><text x="795" y="125">5</text>
  </g>
  <!-- Accent line under title -->
  <rect x="200" y="142" width="500" height="2" fill="url(#accent)" rx="1"/>
  <!-- Title -->
  <text x="450" y="110" font-family="Georgia, serif" font-size="38" font-weight="bold"
        fill="white" text-anchor="middle" filter="url(#glow)">Math for AI</text>
  <text x="450" y="138" font-family="Georgia, serif" font-size="20"
        fill="url(#accent)" text-anchor="middle" letter-spacing="6">LINEAR ALGEBRA</text>
  <!-- Subtitle -->
  <text x="450" y="172" font-family="'Courier New', monospace" font-size="12"
        fill="#8899bb" text-anchor="middle">vectors · matrices · eigenvalues · SVD · transformations</text>
  <!-- Corner dots -->
  <circle cx="30" cy="30" r="4" fill="#00d4ff" opacity="0.5" filter="url(#glow)"/>
  <circle cx="870" cy="30" r="4" fill="#7b61ff" opacity="0.5" filter="url(#glow)"/>
  <circle cx="30" cy="190" r="4" fill="#7b61ff" opacity="0.5" filter="url(#glow)"/>
  <circle cx="870" cy="190" r="4" fill="#00d4ff" opacity="0.5" filter="url(#glow)"/>
</svg>

<br/>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Enabled-013243?style=flat-square&logo=numpy&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-Ready-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![Math](https://img.shields.io/badge/Math-Linear%20Algebra-7b61ff?style=flat-square&logo=wolfram&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-00d4ff?style=flat-square)

> *"To understand AI is to understand the geometry of data."*

</div>

---

## 🧠 Why Linear Algebra for AI?

Linear Algebra is the **core mathematical language** of Artificial Intelligence and Machine Learning. Almost everything in AI — data, models, training, optimization — is expressed using **vectors**, **matrices**, and **linear transformations**.

| Concept | AI Application |
|---|---|
| 🔢 **Vectors** | Feature representation of data |
| 📐 **Matrices** | Datasets, weight layers in neural nets |
| ✖️ **Dot Product** | Predictions and similarity scores |
| 🌀 **Eigenvectors** | Principal Component Analysis (PCA) |
| 🔀 **SVD** | Dimensionality reduction & recommendations |
| 📏 **Norms** | Regularization (L1, L2) |
| 🎯 **Projections** | Feature extraction |

```python
# A 28×28 grayscale image → a 784-dimensional vector
import numpy as np
image = np.random.rand(28, 28)
vector = image.flatten()   # shape: (784,)

# A dataset → a matrix
X = np.random.rand(1000, 784)   # 1000 images, 784 features each
```

---

## 📚 Table of Contents

<details>
<summary><b>Click to expand all topics</b></summary>

1. [Scalars, Vectors, and Matrices](#1-scalars-vectors-and-matrices)
2. [Vector Operations](#2-vector-operations)
3. [Matrix Operations](#3-matrix-operations)
4. [Systems of Linear Equations](#4-systems-of-linear-equations)
5. [Vector Spaces](#5-vector-spaces)
6. [Linear Transformations](#6-linear-transformations)
7. [Matrix Properties](#7-matrix-properties)
8. [Determinants](#8-determinants)
9. [Matrix Inverse](#9-matrix-inverse)
10. [Rank and Null Space](#10-rank-and-null-space)
11. [Eigenvalues and Eigenvectors](#11-eigenvalues-and-eigenvectors)
12. [Diagonalization](#12-diagonalization)
13. [Orthogonality and Orthonormal Bases](#13-orthogonality-and-orthonormal-bases)
14. [Projections](#14-projections)
15. [Singular Value Decomposition (SVD)](#15-singular-value-decomposition-svd)
16. [Norms and Distance Measures](#16-norms-and-distance-measures)
17. [Quadratic Forms](#17-quadratic-forms)
18. [Linear Algebra in Machine Learning](#18-linear-algebra-in-machine-learning)
19. [Summary Cheat Sheet](#19-summary-cheat-sheet)

</details>

---

## 1. Scalars, Vectors, and Matrices

**Scalar** — a single number: `a = 5`

**Vector** — an ordered list of numbers:

$$\mathbf{v} = \begin{bmatrix} 2 \\ 4 \\ 6 \end{bmatrix}$$

**Matrix** — a 2D array of numbers:

$$A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$$

> 💡 **AI Intuition:** A vector = one data point. A matrix = an entire dataset.

---

## 2. Vector Operations

| Operation | Formula | Example |
|---|---|---|
| **Addition** | `u + v` | `[1,2] + [3,4] = [4,6]` |
| **Scalar Multiply** | `c · v` | `2 × [1,3] = [2,6]` |
| **Dot Product** | `u · v = Σ uᵢvᵢ` | `[1,2]·[3,4] = 11` |

```python
import numpy as np
u, v = np.array([1, 2]), np.array([3, 4])
dot = np.dot(u, v)          # 11 — measures similarity
```

> 💡 **AI Intuition:** The dot product is the engine of cosine similarity, attention mechanisms, and neural network predictions.

---

## 3. Matrix Operations

**Matrix Multiplication** `A(m×n) × B(n×p) = C(m×p)`:

$$\begin{bmatrix}1&2\\3&4\end{bmatrix} \times \begin{bmatrix}5&6\\7&8\end{bmatrix} = \begin{bmatrix}19&22\\43&50\end{bmatrix}$$

```python
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
C = A @ B    # [[19,22],[43,50]]
```

> 💡 **AI Intuition:** Every neural network layer is `output = W @ input + b`. Matrix multiplication is the fundamental operation.

---

## 4. Systems of Linear Equations

$$2x + y = 5 \quad \Rightarrow \quad \begin{bmatrix}2&1\\1&-1\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix} = \begin{bmatrix}5\\1\end{bmatrix}$$
$$x - y = 1$$

Solved via Gaussian elimination, LU decomposition, or matrix inverse.

---

## 5. Vector Spaces

A vector space satisfies:
- ✅ Closure under addition
- ✅ Closure under scalar multiplication
- ✅ Zero vector exists
- ✅ Additive inverse exists

> 💡 **AI Intuition:** Feature vectors live in high-dimensional vector spaces (e.g., word embeddings in ℝ³⁰⁰).

---

## 6. Linear Transformations

A function `T(v)` is linear if:

$$T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) \qquad T(c\mathbf{v}) = cT(\mathbf{v})$$

Every linear transformation is representable as: `T(v) = Av`

Common transformations: **Rotation**, **Scaling**, **Reflection**, **Projection**

---

## 7. Matrix Properties

| Property | Symbol | Note |
|---|---|---|
| **Transpose** | `Aᵀ` | Flip rows ↔ columns |
| **Symmetric** | `A = Aᵀ` | Common in covariance matrices |
| **Identity** | `I` | `AI = IA = A` |
| **Zero Matrix** | `0` | All elements zero |

---

## 8. Determinants

$$\det\begin{pmatrix}a&b\\c&d\end{pmatrix} = ad - bc$$

- `det ≠ 0` → Matrix is **invertible**
- `det = 0` → Matrix is **singular** (no inverse)
- `|det|` → Area/volume scaling factor of the transformation

---

## 9. Matrix Inverse

If `A⁻¹` exists: `A · A⁻¹ = I`

Solution to `Ax = b` is `x = A⁻¹b`

```python
A_inv = np.linalg.inv(A)
x = A_inv @ b
# Better (faster, more stable):
x = np.linalg.solve(A, b)
```

> ⚠️ Direct matrix inversion is computationally expensive — in ML, prefer `np.linalg.solve`.

---

## 10. Rank and Null Space

- **Rank** — number of linearly independent columns (information content)
- **Null Space** — all vectors `x` such that `Ax = 0` (lost information)

$$\text{rank}(A) + \text{nullity}(A) = n \quad \text{(columns)}$$

```python
rank = np.linalg.matrix_rank(A)
```

---

## 11. Eigenvalues and Eigenvectors

$$A\mathbf{v} = \lambda\mathbf{v}$$

Where `v` is the **eigenvector** and `λ` is the **eigenvalue**.

```python
eigenvalues, eigenvectors = np.linalg.eig(A)
```

> 💡 **AI Intuition:** Eigenvectors point in the **principal directions** of data variance — this is the heart of PCA.

---

## 12. Diagonalization

If `A` is diagonalizable: `A = P D P⁻¹`

Where `D` is diagonal (eigenvalues) and `P` contains eigenvectors as columns.

**Benefit:** Compute `Aⁿ = P Dⁿ P⁻¹` cheaply (just raise diagonal entries to the power).

---

## 13. Orthogonality and Orthonormal Bases

- **Orthogonal:** `v · w = 0` (vectors are perpendicular)
- **Orthonormal:** Orthogonal **and** unit length (`‖v‖ = 1`)

Used in: **QR Decomposition**, **PCA**, **Signal Processing**

---

## 14. Projections

Projection of **v** onto **u**:

$$\text{proj}_{\mathbf{u}}(\mathbf{v}) = \frac{\mathbf{v} \cdot \mathbf{u}}{\mathbf{u} \cdot \mathbf{u}} \, \mathbf{u}$$

> 💡 **AI Intuition:** Attention mechanisms project queries onto keys. Dimensionality reduction projects data onto lower-dimensional subspaces.

---

## 15. Singular Value Decomposition (SVD)

$$A = U \Sigma V^\top$$

| Symbol | Meaning |
|---|---|
| `U` | Left singular vectors (output space) |
| `Σ` | Singular values (importance/magnitude) |
| `Vᵀ` | Right singular vectors (input space) |

```python
U, S, Vt = np.linalg.svd(A)
```

**Applications:** PCA · Noise Reduction · Recommender Systems · Image Compression · NLP

---

## 16. Norms and Distance Measures

$$\|\mathbf{v}\|_2 = \sqrt{v_1^2 + v_2^2 + \cdots} \qquad \|\mathbf{v}\|_1 = |v_1| + |v_2| + \cdots$$

$$\text{cosine similarity} = \frac{\mathbf{v} \cdot \mathbf{w}}{\|\mathbf{v}\|\|\mathbf{w}\|}$$

```python
l2 = np.linalg.norm(v)               # Euclidean
l1 = np.linalg.norm(v, ord=1)        # Manhattan
cos_sim = np.dot(v, w) / (l2 * np.linalg.norm(w))
```

---

## 17. Quadratic Forms

$$f(\mathbf{x}) = \mathbf{x}^\top A \mathbf{x}$$

Used in: **Loss functions** · **Optimization landscapes** · **Regularization** · **MSE derivation**

---

## 18. Linear Algebra in Machine Learning

```
Data Pipeline:
  Raw Data  →  Matrix X (n_samples × n_features)
      ↓
  Normalize  →  Scale columns (norms)
      ↓
  Model      →  y = Xw + b  (dot products)
      ↓
  Loss       →  ‖y - ŷ‖²   (norms, quadratic forms)
      ↓
  Optimize   →  solve linear system / gradient descent
      ↓
  Compress   →  PCA / SVD for dimensionality reduction
```

---

## 19. Summary Cheat Sheet

```
┌─────────────────────────────────────────────────────────┐
│               LINEAR ALGEBRA CHEAT SHEET                │
├──────────────────────────┬──────────────────────────────┤
│  Data                    │  vectors & matrices           │
│  Models                  │  linear transformations       │
│  Training                │  solving linear systems       │
│  Optimization            │  quadratic forms              │
│  Dimensionality Reduction│  eigenvalues & SVD            │
│  Similarity              │  dot product, cosine sim      │
│  Regularization          │  L1 / L2 norms                │
└──────────────────────────┴──────────────────────────────┘
```

---

## 🚀 Next Steps

- [ ] 📈 **Calculus for AI** — Gradients, partial derivatives, chain rule
- [ ] 🎲 **Probability & Statistics for AI** — Distributions, Bayes, MLE
- [ ] 💻 **Implement with NumPy** — `numpy.linalg` module
- [ ] 🔥 **Implement with PyTorch** — `torch.linalg`, autograd

```python
# Get started
import numpy as np
import torch

# Your linear algebra journey starts here ↓
A = np.array([[2, 0], [0, 3]])
eigenvalues, eigenvectors = np.linalg.eig(A)
print(f"Eigenvalues: {eigenvalues}")   # [2. 3.]
```

---

<div align="center">

<br/>

*"Mastering Linear Algebra = Understanding how AI thinks mathematically."*

<br/>

---

**Made with ❤️ by Sayan**

![Visitor Badge](https://img.shields.io/badge/Thanks%20for%20visiting!-⭐%20Star%20this%20repo-FFD700?style=for-the-badge)

</div>
