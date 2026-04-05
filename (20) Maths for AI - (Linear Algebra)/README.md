<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0a0f1e,50:0d1b3e,100:0a0f1e&height=220&section=header&text=Math%20for%20AI&fontSize=60&fontColor=ffffff&fontAlignY=38&desc=LINEAR%20ALGEBRA&descSize=22&descAlignY=58&descColor=00d4ff&animation=fadeIn" width="100%"/>

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
