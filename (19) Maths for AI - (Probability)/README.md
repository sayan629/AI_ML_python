<div align="center">

![Banner](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=Math%20for%20AI%20%E2%80%94%20Probability&fontSize=44&fontColor=fff&animation=twinkling&fontAlignY=36&desc=Probability%20Theory%20for%20Machine%20Learning&descAlignY=58&descSize=18)

<br/>

[![MIT License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org)
![Status](https://img.shields.io/badge/Status-Active-60a5fa?style=for-the-badge)

<br/>

> *"Probability is the language of uncertainty — and AI speaks it fluently."*

<br/>

</div>

---

## 🖼️ Visual Overview

<div align="center">

<table>
<tr>
<td align="center" width="33%">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Normal_Distribution_PDF.svg/720px-Normal_Distribution_PDF.svg.png" width="260" alt="Gaussian Distribution"/>
<br/><sub><b>🔔 Gaussian Distribution</b></sub>
</td>
<td align="center" width="33%">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Bayes%27_Theorem_MMB_01.jpg/600px-Bayes%27_Theorem_MMB_01.jpg" width="260" alt="Bayes Theorem"/>
<br/><sub><b>📐 Bayes' Theorem</b></sub>
</td>
<td align="center" width="33%">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Standard_deviation_diagram.svg/700px-Standard_deviation_diagram.svg.png" width="260" alt="Standard Deviation"/>
<br/><sub><b>📊 Standard Deviation</b></sub>
</td>
</tr>
</table>

</div>

---

## 🎯 Why Probability for AI?

Probability is the **backbone of every AI system**. Here's where it shows up:

| Area | How Probability Helps |
|:---|:---|
| 🔊 Noisy Data | Models uncertainty in real-world inputs |
| 🎲 Prediction | Outputs likelihoods, not just hard answers |
| 🧠 Learning | Bayesian updates improve beliefs with data |
| 🤔 Reasoning | Handles ambiguous, incomplete information |

> From **Naive Bayes** to **Bayesian Neural Networks** — probability is everywhere.

---

## 📚 Learning Path

```
┌──────────────┐     ┌──────────────────┐     ┌──────────────────┐
│  01  Basics  │ ──► │ 02 Distributions │ ──► │ 03 Random Vars   │
└──────────────┘     └──────────────────┘     └──────────────────┘
                                                        │
                                                        ▼
┌──────────────────┐     ┌──────────────┐     ┌─────────────────┐
│  06 Advanced AI  │ ◄── │ 05 Bayesian  │ ◄── │ 04 Statistics   │
└──────────────────┘     └──────────────┘     └─────────────────┘
```

---

## 🧠 Prerequisites

```python
requirements = {
    "essential": ["Basic algebra", "Sums & averages", "Curiosity 😊"],
    "optional":  ["Linear Algebra", "Python basics"]
}
```

---

## 📁 Repository Structure

```
📦 math-for-ai-probability/
 ┃
 ┣ 📂 01_foundations/               ← What is probability?
 ┣ 📂 02_probability_rules/         ← Addition, conditional, independence
 ┣ 📂 03_random_variables/          ← Discrete & continuous vars
 ┣ 📂 04_probability_distributions/ ← Gaussian, Binomial, Poisson...
 ┣ 📂 05_statistics/                ← CLT, LLN, descriptive stats
 ┣ 📂 06_bayesian_probability/      ← Bayes theorem & belief updating
 ┣ 📂 07_information_theory/        ← Entropy, KL divergence
 ┣ 📂 08_advanced_topics/           ← Markov chains, Monte Carlo, EM
 ┣ 📂 09_ai_applications/           ← Real ML model walkthroughs
 ┗ 📂 exercises/                    ← Problems + Python simulations
```

---

## 🗺️ Module Deep Dive

<details>
<summary><b>📌 01 — Foundations of Probability</b></summary>

<br/>

Probability measures how likely an event is.

$$0 \leq P(\text{Event}) \leq 1$$

| Experiment | Sample Space | Example Probability |
|:---|:---|:---|
| Coin Toss | `{Heads, Tails}` | P(Heads) = 0.5 |
| Dice Roll | `{1, 2, 3, 4, 5, 6}` | P(6) = 1/6 |
| Card Draw | `{52 cards}` | P(Ace) = 4/52 |

An **event** is any subset of the sample space.

</details>

<details>
<summary><b>📌 02 — Rules of Probability</b></summary>

<br/>

**Addition Rule**
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

**Conditional Probability**
$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

> 🤖 *Used in AI for classification and prediction.*

**Independence**
$$P(A \cap B) = P(A) \cdot P(B)$$

</details>

<details>
<summary><b>📌 03 — Random Variables</b></summary>

<br/>

A random variable maps outcomes to numbers.

| Type | Description | Examples |
|:---|:---|:---|
| Discrete | Countable values | Coin toss, dice, word counts |
| Continuous | Any value in a range | Height, temperature, time |

**Expectation (Mean)**
$$E[X] = \sum x \cdot P(x)$$

**Variance**
$$\text{Var}(X) = E\left[(X - \mu)^2\right]$$

> 🎯 *AI uses expectation to optimize loss functions.*

</details>

<details>
<summary><b>📌 04 — Probability Distributions</b></summary>

<br/>

### Discrete Distributions

| Distribution | Formula | Key Use |
|:---|:---|:---|
| Bernoulli | $P(X=1) = p$ | Single binary trial |
| Binomial | $\binom{n}{k} p^k (1-p)^{n-k}$ | n binary trials |
| Poisson | $\frac{\lambda^k e^{-\lambda}}{k!}$ | Event counts |

### Continuous Distributions

| Distribution | Key Use |
|:---|:---|
| Uniform | Equal probability everywhere |
| **Normal / Gaussian** $\mathcal{N}(\mu, \sigma^2)$ | Central to AI: noise, regression, initialization |
| Exponential | Time between events |

</details>

<details>
<summary><b>📌 05 — Statistics for AI</b></summary>

<br/>

| Concept | Formula | Why It Matters |
|:---|:---|:---|
| Mean | $\bar{x} = \frac{1}{n}\sum x_i$ | Central tendency |
| Variance | $\sigma^2 = E[(X-\mu)^2]$ | Spread of data |
| Law of Large Numbers | $\bar{X}_n \to \mu$ | More data = better estimates |
| **Central Limit Theorem** | Sum of RVs → Normal | Why Gaussians dominate AI |

</details>

<details>
<summary><b>📌 06 — Bayesian Probability ⭐</b></summary>

<br/>

**Bayes' Theorem**

$$\boxed{P(H \mid D) = \frac{P(D \mid H) \cdot P(H)}{P(D)}}$$

| Term | Symbol | Meaning |
|:---|:---|:---|
| **Prior** | $P(H)$ | Belief *before* seeing data |
| **Likelihood** | $P(D \mid H)$ | How well hypothesis explains data |
| **Posterior** | $P(H \mid D)$ | Updated belief *after* data |
| **Evidence** | $P(D)$ | Normalizing constant |

**Why AI Loves Bayes:**
- ✅ Learning from small data
- ✅ Uncertainty quantification
- ✅ Probabilistic reasoning

Used in: `Naive Bayes` · `Bayesian Networks` · `Probabilistic Graphical Models`

</details>

<details>
<summary><b>📌 07 — Information Theory</b></summary>

<br/>

**Entropy** — measures uncertainty
$$H(X) = -\sum_{x} P(x) \log P(x)$$

**Cross-Entropy** — standard classification loss
$$H(P, Q) = -\sum P(x) \log Q(x)$$

**KL Divergence** — how different two distributions are
$$D_{\text{KL}}(P \| Q) = \sum P(x) \log \frac{P(x)}{Q(x)}$$

</details>

<details>
<summary><b>📌 08 — Advanced Topics</b></summary>

<br/>

- 🔗 Joint & Marginal Distributions
- 📐 Covariance & Correlation
- 🔄 Markov Chains
- 👁️ Hidden Markov Models (HMMs)
- 🎲 Monte Carlo Methods & Sampling
- 🔁 Expectation-Maximization (EM)

</details>

<details>
<summary><b>📌 09 — Probability in AI & ML</b></summary>

<br/>

| Model | Role of Probability |
|:---|:---|
| Logistic Regression | Outputs class probabilities |
| Naive Bayes | Conditional independence assumption |
| Gaussian Mixture Models | Soft cluster assignments |
| Reinforcement Learning | Policy & value estimation |
| Bayesian Neural Networks | Uncertainty over weights |
| VAEs / Generative Models | Latent space distributions |

**Core Loss Function:**
$$\mathcal{L} = -\log P(y \mid x)$$

</details>

---

## 🧪 Exercises & Practice

Each module includes:

| Type | Description |
|:---|:---|
| 💡 Conceptual Questions | Test your intuition and understanding |
| 🔢 Numerical Problems | Worked examples with full solutions |
| 🐍 Python Simulations | Jupyter notebooks for hands-on practice |
| 🤖 Real AI Scenarios | Apply concepts to actual ML models |

---

## 🛠️ Tech Stack

<div align="center">

| Tool | Purpose | Install |
|:---:|:---|:---|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) | Core programming | `brew install python` |
| ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white) | Numerical computation | `pip install numpy` |
| ![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=flat&logo=scipy&logoColor=white) | Statistical functions | `pip install scipy` |
| ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat) | Visualizations | `pip install matplotlib` |
| ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white) | Interactive notebooks | `pip install jupyter` |

</div>

---

## 🚀 Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/your-username/math-for-ai-probability.git

# 2. Navigate into the project
cd math-for-ai-probability

# 3. Install dependencies
pip install numpy scipy matplotlib jupyter

# 4. Launch notebooks
jupyter notebook
```

---

## 🌟 What You'll Achieve

```
Before this repo                  After this repo
─────────────────────────────────────────────────────────────────
"Why do models output             "I can derive and explain
 probabilities?"             →    Bayes' theorem from scratch"

"Loss functions are magic"   →    "Loss = -log P(y|x) is obvious"

"I skip math in papers"      →    "I read ML papers confidently"

"I don't understand           →    "I build better, more
 uncertainty in AI"                principled AI models"
```

---

## 🤝 Contributing

Contributions are always welcome!

- 🐛 Open issues for errors or suggestions
- 📥 Submit pull requests with improvements
- ⭐ Star the repo if it helped you learn!

---

## 📜 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

---

<div align="center">

<br/>

*Happy Learning! 📈*

<br/>

![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer)

<br/>

### ✨ Made with ❤️ by **Sayan**

</div>
