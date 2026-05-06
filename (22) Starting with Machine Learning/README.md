# 🤖 Machine Learning — Notes

> *A part of Computer Science where we teach computers to learn from data, find patterns, and make decisions and predictions.*

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Kernel_Machine.svg/1200px-Kernel_Machine.svg.png" alt="Machine Learning" width="500"/>
</p>

---

## 📌 Traditional Algorithm vs. Machine Learning

| Aspect | Traditional Algorithm | Machine Learning |
|---|---|---|
| **Flow** | Input → Logic → Output | Input/Output → **Model** → New Logic (Hypothesis) → New Output |
| **Logic** | Hard-coded by developer | Learned automatically from data |
| **Adaptability** | Fixed | Adapts with new input |

```
Traditional:          Machine Learning:
    Input                 Input + Output
      ↓                        ↓
   [Logic]                  [Model]
      ↓                        ↓
   Output          New Input → Logic (Hypothesis) → New Output
```

---

## 🧩 ML Types

### ⭐⭐ 1. Supervised Learning
> Models are trained using **labelled data** `(Input → Output)`

<p align="center">
  <img src="https://www.softhouse.se/wp-content/uploads/2023/09/supervised-vs-unsupervised-learning.png" alt="Supervised vs Unsupervised Learning" width="700"/>
</p>

#### 🏷️ What is Labelled Data?
Labelled data is **raw data** (image, text, audio) that has been paired with a meaningful **tag, label, or annotation** that informs a machine learning model about the desired outcome.

#### 🔀 Problems Solved in Supervised Learning

```
                    ┌── Classification  (Classes / Categories)
Supervised Learning ┤   e.g., [cat / dogs]
                    │
                    └── Regression      (Predict some continuous value)
                        e.g., [AQI], [Stock Price]
```

<p align="center">
  <img src="https://media.geeksforgeeks.org/wp-content/uploads/20231122174515/Classification-vs-Regression.png" alt="Classification vs Regression" width="700"/>
</p>

| Problem Type | Description | Examples |
|---|---|---|
| **Classification** | Predicts a class/category | Cat vs Dog detection |
| **Regression** | Predicts a continuous value | AQI prediction, Stock prices |

---

### 2. Unsupervised Learning
> Models are trained using **unlabelled data**

- We solve problems using **Clustering**
- Example: `[iPhone + Charger]` — grouping similar items together

<p align="center">
  <img src="https://developers.google.com/static/machine-learning/glossary/images/clustering.svg" alt="Clustering Visualization" width="600"/>
</p>

```
Dataset (no labels)          Clustered Output
  o o x x                →   [Group A: o o]
  x o x o                    [Group B: x x]
                              e.g., Alcoholic / Non-Alcoholic
```

---

### 3. Reinforcement Learning
> **Goal-Oriented** — Learn from **Rewards & Penalties**

- The model learns by interacting with an environment
- It gets rewarded for correct actions and penalized for wrong ones

<p align="center">
  <img src="https://www.mathworks.com/discovery/reinforcement-learning/_jcr_content/mainParsys/image_1621705020.adapt.full.medium.jpg/1726496892913.jpg" alt="Reinforcement Learning Diagram" width="700"/>
</p>

**Example:** Training Robots 🤖

```
Agent → Action → Environment → Reward/Penalty → Agent (learns & improves)
```

---

## 🗺️ Quick Reference Summary

```
Machine Learning
│
├── Supervised Learning       ← Labelled Data (Input → Output)
│   ├── Classification        ← Categories (cat/dog)
│   └── Regression            ← Continuous values (price, AQI)
│
├── Unsupervised Learning     ← Unlabelled Data
│   └── Clustering            ← Group similar data points
│
└── Reinforcement Learning    ← Reward & Penalty based
    └── Goal-Oriented         ← e.g., Train robots
```

---

## 📚 Key Terminology

| Term | Definition |
|---|---|
| **Model** | A mathematical function learned from data |
| **Hypothesis** | The logic/rule the model learns |
| **Labelled Data** | Data tagged with correct answers |
| **Unlabelled Data** | Raw data without any tags |
| **Classification** | Predicting a category |
| **Regression** | Predicting a numeric value |
| **Clustering** | Grouping similar data points |
| **Reward/Penalty** | Feedback mechanism in Reinforcement Learning |

---

<p align="center">
  <i>📓 Notes from ML class — handwritten & digitized</i>
  <br><br>
  <strong>✍️ Made by Sayan</strong>
</p>
