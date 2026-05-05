# 📊 Math for AI — Calculus

> *"If Linear Algebra builds the model, Calculus teaches it how to learn."*

![Calculus Banner](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Sinusverlauf.png/800px-Sinusverlauf.png)

---

## 🧠 What is This?

Calculus is the **engine behind learning** in AI. Every time a neural network updates its weights, every time a model improves its predictions — **calculus is at work**.

This document covers Calculus **from fundamentals to advanced topics**, specifically focused on **Machine Learning** and **Deep Learning** applications.

---

## 📚 Table of Contents

| # | Topic |
|---|-------|
| 1 | [Why Calculus for AI?](#1-why-calculus-for-ai) |
| 2 | [Functions and Graphs](#2-functions-and-graphs) |
| 3 | [Limits](#3-limits) |
| 4 | [Continuity](#4-continuity) |
| 5 | [Derivatives – Intuition](#5-derivatives--intuition) |
| 6 | [Rules of Differentiation](#6-rules-of-differentiation) |
| 7 | [Higher-Order Derivatives](#7-higher-order-derivatives) |
| 8 | [Partial Derivatives](#8-partial-derivatives) |
| 9 | [Gradients and Directional Derivatives](#9-gradients-and-directional-derivatives) |
| 10 | [Chain Rule (Backpropagation Core)](#10-chain-rule-backpropagation-core) |
| 11 | [Jacobian and Hessian](#11-jacobian-and-hessian) |
| 12 | [Optimization and Critical Points](#12-optimization-and-critical-points) |
| 13 | [Gradient Descent](#13-gradient-descent) |
| 14 | [Convexity](#14-convexity) |
| 15 | [Integrals – Intuition](#15-integrals--intuition) |
| 16 | [Definite and Indefinite Integrals](#16-definite-and-indefinite-integrals) |
| 17 | [Multivariable Integrals](#17-multivariable-integrals) |
| 18 | [Taylor Series](#18-taylor-series) |
| 19 | [L'Hôpital's Rule](#19-lhôpitals-rule) |
| 20 | [Numerical Differentiation](#20-numerical-differentiation) |
| 21 | [Worked Example: Finding Critical Points](#21-worked-example-finding-critical-points) |
| 22 | [Calculus in Machine Learning](#22-calculus-in-machine-learning) |
| 23 | [Summary Cheat Sheet](#23-summary-cheat-sheet) |

---

## 1. Why Calculus for AI?

In AI, calculus is the foundation of **model learning**:

- 📉 Measure how wrong a model is (**loss**)
- 🔍 Understand how parameters affect loss
- 🔧 Decide **how** to update parameters
- ⚡ Optimize models efficiently

```
Loss = f(weights)
Goal: minimize Loss
```

This requires:
- ✅ Derivatives
- ✅ Gradients
- ✅ Optimization methods

> **Key Insight:** Without calculus, there is no learning in AI — only static models that can never improve.

---

## 2. Functions and Graphs

A function maps inputs to outputs:

```
y = f(x)
```

**Common examples:**
```
f(x) = x²
f(x) = 3x + 2
f(x) = sin(x)
f(x) = eˣ
```

**AI Intuition:**
| Math | ML Equivalent |
|------|--------------|
| Input `x` | Features |
| Output `y` | Prediction |
| Function `f` | Model |

![Function Graph](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Polynomialdeg2.svg/600px-Polynomialdeg2.svg.png)

---

## 3. Limits

A limit describes what value a function **approaches** as input nears a value:

```
lim (x → a) f(x)
```

**Example:**
```
lim (x → 2) (x²) = 4
```

Limits form the **mathematical foundation** of derivatives and continuity. They're essential for understanding what happens at discontinuities in activation functions like ReLU.

---

## 4. Continuity

A function is **continuous** at `x = a` if:

1. `f(a)` exists
2. `lim (x → a) f(x)` exists
3. Both are **equal**

> ✅ Most loss functions used in ML are continuous.
> ⚠️ ReLU is continuous but **not differentiable** at x = 0.

---

## 5. Derivatives – Intuition

A derivative measures the **rate of change** — the slope of the tangent line at any point.

```
f(x) = x²
f'(x) = 2x

At x = 3: slope = 6
```

**AI Intuition:**
> _"How much does the loss change when I nudge this weight?"_

![Derivative Tangent Line](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Tangent_to_a_curve.svg/600px-Tangent_to_a_curve.svg.png)

---

## 6. Rules of Differentiation

| Rule | Formula |
|------|---------|
| **Power Rule** | `d/dx (xⁿ) = n·xⁿ⁻¹` |
| **Constant Rule** | `d/dx (c) = 0` |
| **Sum Rule** | `d/dx (f + g) = f' + g'` |
| **Product Rule** | `d/dx (f·g) = f'g + fg'` |
| **Quotient Rule** | `d/dx (f/g) = (f'g − fg') / g²` |
| **Exponential** | `d/dx (eˣ) = eˣ` |
| **Logarithm** | `d/dx (ln x) = 1/x` |
| **Sigmoid** | `σ'(x) = σ(x)·(1 − σ(x))` |

> 💡 The **sigmoid derivative** is used heavily in neural network backpropagation.

---

## 7. Higher-Order Derivatives

The **second derivative** measures curvature:

```
f(x) = x²
f'(x) = 2x
f''(x) = 2  →  positive → MINIMUM
```

| Sign of f''(x) | Meaning |
|----------------|---------|
| `f''(x) > 0` | Concave up (bowl shape) → local minimum |
| `f''(x) < 0` | Concave down (hill shape) → local maximum |
| `f''(x) = 0` | Inflection point (curvature changes) |

---

## 8. Partial Derivatives

Used when functions have **multiple variables** (like neural network weights):

```
f(x, y) = x² + y²

∂f/∂x = 2x    (treat y as constant)
∂f/∂y = 2y    (treat x as constant)
```

**AI Intuition:**
> Each weight in a neural network affects the loss **independently**, and partial derivatives capture exactly that effect.

---

## 9. Gradients and Directional Derivatives

### Gradient Vector

The gradient collects all partial derivatives:

```
∇f = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]
```

**Properties:**
- ↗️ Points in direction of **steepest increase**
- ↙️ **Negative gradient** → direction of steepest decrease
- Used directly in **training neural networks**

### Directional Derivative

The rate of change in any direction `u`:

```
Dᵤf = ∇f · u
```

![Gradient Field](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Gradient_visual.svg/600px-Gradient_visual.svg.png)

---

## 10. Chain Rule (Backpropagation Core)

> 🔑 **The most important rule in AI.**

If:
```
y = f(g(x))
```

Then:
```
dy/dx = f'(g(x)) · g'(x)
```

**Extended Chain Rule (for deep networks):**
```
∂L/∂w₁ = ∂L/∂a₃ · ∂a₃/∂a₂ · ∂a₂/∂a₁ · ∂a₁/∂w₁
```

> **Backpropagation** = repeated application of the chain rule, layer by layer, from output to input.

```
Input → Hidden₁ → Hidden₂ → Output
  ←──── ←──────── ←──────── Gradients flow backward
```

---

## 11. Jacobian and Hessian

### Jacobian Matrix

Used for **vector-valued functions** (multiple outputs):

```
J = ∂(outputs) / ∂(inputs)

J_ij = ∂fᵢ / ∂xⱼ
```

Used in: batch gradient computation, Recurrent Neural Networks (RNNs).

### Hessian Matrix

**Second-order partial derivatives** — captures curvature of a surface:

```
H_ij = ∂²f / ∂xᵢ∂xⱼ
```

Used in:
- Newton's method
- Second-order optimization (L-BFGS)
- Detecting saddle points

---

## 12. Optimization and Critical Points

### What Are Critical Points?

A **critical point** occurs where the gradient is zero:

```
∇f = 0  →  f'(x) = 0
```

At a critical point, the function is **neither increasing nor decreasing** — it's flat.

### Types of Critical Points

| Type | f'(x) | f''(x) | Visual |
|------|--------|--------|--------|
| **Local Minimum** | = 0 | > 0 | Valley bottom ⬇️ |
| **Local Maximum** | = 0 | < 0 | Hill top ⬆️ |
| **Saddle Point** | = 0 | = 0 | Neither min nor max ↔️ |
| **Global Minimum** | = 0 | > 0 | Lowest of all valleys 🏆 |

![Critical Points](https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Extrema_example_original.svg/600px-Extrema_example_original.svg.png)

### Second Derivative Test

```
If f'(a) = 0:
  f''(a) > 0  →  Local MINIMUM
  f''(a) < 0  →  Local MAXIMUM
  f''(a) = 0  →  Test INCONCLUSIVE (check further)
```

### AI Relevance

- Deep learning loss surfaces have **millions of saddle points**
- True local minima are rare in high dimensions
- **Saddle points** are the real challenge — gradient descent can get stuck
- Modern optimizers (Adam, RMSProp) help escape saddle points

---

## 13. Gradient Descent

The core optimization algorithm in ML:

```
θ = θ − α · ∇L(θ)
```

Where:
- `θ` = model parameters (weights)
- `α` = learning rate (step size)
- `L` = loss function
- `∇L(θ)` = gradient of loss

### Variants

| Variant | Data per Step | Speed | Stability |
|---------|--------------|-------|-----------|
| **Batch GD** | Full dataset | Slow | Very stable |
| **Stochastic GD (SGD)** | 1 sample | Fast | Noisy |
| **Mini-batch GD** | Small batch | Balanced | Balanced |

### Learning Rate Effect

```
α too large  → overshoots minimum, diverges ❌
α too small  → very slow convergence 🐌
α just right → smooth convergence ✅
```

![Gradient Descent](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Gradient_descent.svg/600px-Gradient_descent.svg.png)

---

## 14. Convexity

A function is **convex** if:

```
f(tx + (1−t)y) ≤ t·f(x) + (1−t)·f(y)   for all t ∈ [0,1]
```

**Why it matters for AI:**

| Property | Convex Loss | Non-Convex Loss |
|----------|-------------|-----------------|
| Minima | One global minimum | Many local minima |
| Gradient Descent | Always finds optimal | May get stuck |
| Examples | MSE, Logistic Loss | Neural Network Loss |

> 🎯 **Convex loss functions guarantee finding the global minimum.**

---

## 15. Integrals – Intuition

An integral measures **accumulated change** — the area under a curve:

```
∫ f(x) dx
```

**Geometric meaning:** Total area between the curve and the x-axis.

**AI Use Cases:**
- Computing **expected values** of probability distributions
- Normalizing probability density functions
- Computing the **KL divergence** between distributions

---

## 16. Definite and Indefinite Integrals

### Indefinite Integral

```
∫ x² dx = x³/3 + C
∫ eˣ dx = eˣ + C
∫ 1/x dx = ln|x| + C
```

### Definite Integral (Fundamental Theorem of Calculus)

```
∫₀¹ x² dx = [x³/3]₀¹ = 1/3 − 0 = 1/3
```

**Used in:**
- Probability distributions
- Expectation values `E[X] = ∫ x·p(x) dx`

---

## 17. Multivariable Integrals

```
∫∫ f(x, y) dx dy
```

**Applications in AI:**
- Joint probability distributions
- Marginalizing over latent variables
- Variational inference

---

## 18. Taylor Series

Approximates any smooth function using an **infinite polynomial**:

```
f(x) ≈ f(a) + f'(a)(x−a) + f''(a)/2!(x−a)² + f'''(a)/3!(x−a)³ + ...
```

**Common Taylor Expansions:**
```
eˣ ≈ 1 + x + x²/2! + x³/3! + ...
sin(x) ≈ x − x³/3! + x⁵/5! − ...
ln(1+x) ≈ x − x²/2 + x³/3 − ...
```

**Used in AI for:**
- Understanding loss landscapes
- Deriving optimization algorithms
- Approximating complex functions

---

## 19. L'Hôpital's Rule

Evaluates **indeterminate forms** (0/0 or ∞/∞):

```
lim (x→a) f(x)/g(x) = lim (x→a) f'(x)/g'(x)
```

**Example — Softmax Stability:**
```
lim (x→0) sin(x)/x = lim cos(x)/1 = 1
```

Useful in deriving stable numerical implementations of **softmax** and **log-sum-exp** tricks in deep learning.

---

## 20. Numerical Differentiation

When analytical derivatives are hard to compute, **numerical methods** approximate them:

### Finite Difference Method

```
f'(x) ≈ [f(x + h) − f(x)] / h          (forward difference)
f'(x) ≈ [f(x + h) − f(x − h)] / (2h)   (central difference, more accurate)
```

**Used in:**
- Gradient checking (verifying backprop implementation)
- Numerical solvers
- Physics-based simulations

```python
# Gradient check in practice
def numerical_gradient(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)
```

---

## 21. Worked Example: Finding Critical Points

### Problem

> Find all **critical points**, **local maxima**, and **local minima** of:
>
> ```
> f(x) = x³ − 6x² + 9x + 1
> ```

---

### Step 1 — Find the First Derivative

```
f(x)  = x³ − 6x² + 9x + 1

f'(x) = 3x² − 12x + 9
```

---

### Step 2 — Set f'(x) = 0 to Find Critical Points

```
3x² − 12x + 9 = 0

÷ 3:  x² − 4x + 3 = 0

Factor: (x − 1)(x − 3) = 0

∴  x = 1  and  x = 3
```

🎯 **Critical points are at x = 1 and x = 3**

---

### Step 3 — Find the Second Derivative

```
f'(x)  = 3x² − 12x + 9

f''(x) = 6x − 12
```

---

### Step 4 — Apply the Second Derivative Test

**At x = 1:**
```
f''(1) = 6(1) − 12 = −6 < 0

→ f''(1) < 0  ∴  LOCAL MAXIMUM at x = 1
```

**At x = 3:**
```
f''(3) = 6(3) − 12 = +6 > 0

→ f''(3) > 0  ∴  LOCAL MINIMUM at x = 3
```

---

### Step 5 — Find the Function Values

```
f(1) = (1)³ − 6(1)² + 9(1) + 1
     = 1 − 6 + 9 + 1
     = 5

f(3) = (3)³ − 6(3)² + 9(3) + 1
     = 27 − 54 + 27 + 1
     = 1
```

---

### ✅ Final Answer

| Critical Point | x | f(x) | Type |
|----------------|---|------|------|
| **Local Maximum** | x = 1 | f(1) = **5** | f''(1) = −6 < 0 |
| **Local Minimum** | x = 3 | f(3) = **1** | f''(3) = +6 > 0 |

```
         f(x) = x³ − 6x² + 9x + 1

   5 ──── ● (1, 5)  ← Local Maximum
          |
          |       curve goes down
          |
   1 ──────────── ● (3, 1)  ← Local Minimum
                  |
                  curve goes up again
```

> **Interpretation (AI context):** In a loss landscape shaped like this, gradient descent started from x < 1 would climb up, then descend into the minimum at x = 3. Started from x > 3, it descends directly into the minimum. The maximum at x = 1 is an **unstable equilibrium** — a saddle-like region that gradient descent naturally avoids.

---

## 22. Calculus in Machine Learning

| Concept | ML Application | Example |
|---------|---------------|---------|
| **Derivatives** | Loss sensitivity to weights | `∂L/∂w` |
| **Gradients** | Direction for weight updates | `∇L` |
| **Chain Rule** | Backpropagation | Layer-wise gradient flow |
| **Partial Derivatives** | Multi-weight optimization | Each `wᵢ` independently |
| **Jacobian** | Batch gradient computation | RNNs, transformers |
| **Hessian** | Second-order optimization | L-BFGS, Newton's method |
| **Integrals** | Probability & expectation | `E[X]`, KL divergence |
| **Taylor Series** | Approximation & analysis | Loss landscape analysis |
| **Convexity** | Guaranteed convergence | MSE, cross-entropy |
| **Critical Points** | Finding optimal weights | Minima of loss surface |

---

## 23. Summary Cheat Sheet

```
📐 CALCULUS FOR AI — QUICK REFERENCE
══════════════════════════════════════════

DERIVATIVES
  f'(x)        →  Rate of change of f at x
  ∂f/∂xᵢ      →  Partial derivative w.r.t. xᵢ
  ∇f           →  Gradient vector (all partials)
  
CRITICAL POINTS
  f'(x) = 0    →  Critical point (candidate min/max)
  f''(x) > 0   →  Local minimum
  f''(x) < 0   →  Local maximum
  f''(x) = 0   →  Inconclusive

KEY RULES
  Chain Rule:  dy/dx = f'(g(x)) · g'(x)
  Product:     (fg)' = f'g + fg'
  Power:       d/dx(xⁿ) = n·xⁿ⁻¹

GRADIENT DESCENT
  θ ← θ − α·∇L(θ)
  α = learning rate, L = loss

INTEGRALS
  ∫f(x)dx      →  Antiderivative (area under curve)
  E[X]         →  ∫ x·p(x) dx  (expected value)

TAYLOR SERIES
  f(x) ≈ Σ fⁿ(a)/n! · (x−a)ⁿ
══════════════════════════════════════════
```

---

## 🚀 Next Steps

| Topic | Resource |
|-------|----------|
| 📐 Core Concept of Machine Learning | Next in series |
| 🧠 Optimization Algorithms | Adam, RMSProp, L-BFGS |
| 💻 Implementation | NumPy, PyTorch, TensorFlow |

---

## ⭐ Star This Repository

If this helped you understand the mathematics behind AI, consider **starring the repository** to help others find it!

---

<div align="center">

**Made with ❤️ by Sayan**

*"Mathematics is not about numbers, equations, or algorithms — it is about understanding."*

</div>
