<div align="center">

# 🧠 Deep Learning — Part 1

### *From Neurons to Networks: The Foundations of Deep Learning*

![Deep Learning](https://img.shields.io/badge/Deep%20Learning-Part%201-blueviolet?style=for-the-badge&logo=pytorch&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![Status](https://img.shields.io/badge/Status-Learning-success?style=for-the-badge)

*A beginner-friendly, structured walkthrough of Deep Learning fundamentals — built from handwritten study notes.*

</div>

---

## 📑 Table of Contents

| # | Topic |
|---|-------|
| 1 | [What is Deep Learning?](#-1-what-is-deep-learning) |
| 2 | [Machine Learning vs Deep Learning](#-2-machine-learning-vs-deep-learning) |
| 3 | [What are Neural Networks](#-3-what-are-neural-networks) |
| 4 | [Perceptron](#-4-perceptron) |
| 5 | [Activation Functions](#-5-activation-functions) |
| 6 | [Forward & Backward Propagation](#-6-forward--backward-propagation) |
| 7 | [Multilayered Neural Networks](#-7-multilayered-neural-network) |
| 8 | [PyTorch vs TensorFlow vs Keras](#-8-pytorch-vs-tensorflow-vs-keras) |
| 9 | [Google Colab](#-9-google-colab) |
| 10 | [Building a Neuron (Hands-on Code)](#-10-building-a-neuron--first-implementation) |

---

## 🌐 1. What is Deep Learning?

> **Deep Learning (DL)** is the part of Computer Science where we create **neural networks inside a machine** to mimic the workings of the **human brain**.

DL sits at the innermost layer of the AI ecosystem:

```
┌───────────────────────────────────────┐
│                  AI                   │
│   ┌───────────────────────────────┐   │
│   │              ML                │  │
│   │   ┌───────────────────────┐   │   │
│   │   │         DL             │   │  │
│   │   │   ┌───────────────┐   │   │   │
│   │   │   │    GenAI       │   │   │  │
│   │   │   └───────────────┘   │   │   │
│   │   └───────────────────────┘   │   │
│   └───────────────────────────────┘   │
└───────────────────────────────────────┘
```

### 🔀 Two Major Branches of Deep Learning

| Branch | Deals With | Example Application |
|--------|------------|----------------------|
| **NLP** (Natural Language Processing) | Text | LLMs (Large Language Models) |
| **CV** (Computer Vision) | Images / Videos | Self-Driving Cars |

---

## ⚖️ 2. Machine Learning vs Deep Learning

| # | Machine Learning (ML) | Deep Learning (DL) |
|---|------------------------|----------------------|
| 1 | Uses **structured data** | Uses **unstructured data** |
| 2 | Solves **simple tasks** | Solves **complex tasks** |
| 3 | **More interpretable** | **Less interpretable** (Black Box) |
| 4 | **Less** training time | **More** training time |
| 5 | **Less computation** — runs on CPU / PC / small servers | **More computation** — needs GPUs / TPUs |

---

## 🕸️ 3. What are Neural Networks?

A **Neural Network** is a web of interconnected **neurons**, organized into layers, inspired by the human brain.

```
        Input Layer      Hidden Layer      Output Layer
           (o)  ────────────▶ (o) ───────────▶ (o)
           (o)  ─────╲  ╱───▶ (o) ─────╲  ╱───▶
           (o)  ──────╳───────(o) ──────╳
                      ╱  ╲            ╱  ╲
```

<div align="center">
<img src="images/neural_network_example.png" width="450" alt="Neural Network Example"/>
</div>

**Types of Artificial Neural Networks (ANN):**

- 🔹 **FNN** — Feedforward Neural Network
- 🔹 **RNN** — Recurrent Neural Network
- 🔹 **CNN** — Convolutional Neural Network

---

## 🎯 4. Perceptron

> Introduced in **1950**, the **Perceptron** was designed for **binary classification**. It is basically made up of a **single neuron**.

### 🏦 Example: Loan Approval Prediction

| Input Feature | Meaning |
|---------------|---------|
| `x1` | DTI (Debt-to-Income ratio) |
| `x2` | Credit Score |
| `x3` | Income |
| Output | Loan Approved? (Y/N) |

```
   DTI  ───▶ (x1) ─── w1 ──╲
                            ╲
Credit Score ─▶ (x2) ─ w2 ──▶ Σ ──▶ (f) ──▶ Output
                            ╱
   Income ───▶ (x3) ─── w3 ╱
                            
                b (bias) ──▶ Σ
```

### 🔑 Key Components

| Term | Description |
|------|-------------|
| **Input Layer** | Features `(x1, x2, x3, ..., xn)` |
| **Weight** | Contribution of each input to the output |
| **Bias** | Constant term added to the weighted sum |
| **Weighted Sum / Dot Product / Net Input** | Combines inputs, weights & bias |
| **Activation Function** | Converts weighted sum into the neuron's final output |

### 📐 The Core Formula

$$
z = \sum_{i=1}^{n} w_i x_i + b
$$

<div align="center">
<img src="images/perceptron.png" width="600" alt="Perceptron Diagram"/>
</div>

---

## ⚡ 5. Activation Functions

| Function | Formula | Notes |
|----------|---------|-------|
| **Sigmoid** | `f(x) = 1 / (1 + e⁻ˣ)` | S-shaped curve, output between 0 and 1 |
| **Tanh** | `f(x) = tanh(x) = (eˣ - e⁻ˣ) / (eˣ + e⁻ˣ)` | Output ranges from -1 to 1 |
| **ReLU** ⭐ | `f(x) = max(0, x)` | Rectified Linear Unit — most widely used |
| **Softmax** | `zᵢ = e^zᵢ / Σ e^zⱼ` | Converts a vector of values into a probability distribution |
| **Linear** | `f(x) = x` | Simple identity function |
| **Step Function** | `f(x) = 0 if x ≥ 0, else 1` | Used in the original 1950's Perceptron |

---

## 🔄 6. Forward & Backward Propagation

```
Input  ───▶  Forward Propagation  ───▶  Output
Input  ◀───  Backward Propagation ◀───  Output
```

- **Forward Propagation:** Data flows from the input layer → hidden layers → output layer, producing a prediction.
- **Backward Propagation:** The error is sent back through the network to update weights and biases (learning step).

---

## 🧩 7. Multilayered Neural Network

A network with **multiple hidden layers** between the input and output layers.

```
 Input Layer    Hidden Layers     Output Layer
    (o)  ───────  (o)  (o)  ───────  (o)
    (o)  ───────  (o)  (o)  ───────  
    (o)  ───────  (o)  (o)  ───────  (o)
```

<div align="center">
<img src="images/multilayer_neural_network.png" width="600" alt="Multilayer Neural Network"/>
</div>

> 📌 **Note:** The **number of hidden layers = Depth** of the neural network.

---

## ⚔️ 8. PyTorch vs TensorFlow vs Keras

<div align="center">

<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pytorch/pytorch-original.svg" width="70" alt="PyTorch logo"/>&nbsp;&nbsp;&nbsp;&nbsp;
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/tensorflow/tensorflow-original.svg" width="70" alt="TensorFlow logo"/>&nbsp;&nbsp;&nbsp;&nbsp;
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/keras/keras-original.svg" width="70" alt="Keras logo"/>

</div>

| Framework | Logo | Created By | Year | Backend |
|-----------|:----:|-----------|------|---------|
| **PyTorch** | ![PyTorch](https://img.shields.io/badge/-EE4C2C?style=flat-square&logo=pytorch&logoColor=white) | Facebook | 2017 | C++ (for speed) |
| **TensorFlow** | ![TensorFlow](https://img.shields.io/badge/-FF6F00?style=flat-square&logo=tensorflow&logoColor=white) | Google | 2015 | C++ (for speed) |
| **Keras** | ![Keras](https://img.shields.io/badge/-D00000?style=flat-square&logo=keras&logoColor=white) | — | — | High-level API (frontend only); uses **TensorFlow**, **Theano**, or **CNTK** as backend |

> 💡 Both PyTorch and TensorFlow use a **C++ backend** internally to make computations faster. Keras was later integrated with TensorFlow as its official high-level API.

---

## ☁️ 9. Google Colab

A free, cloud-based Jupyter notebook environment used to write and run Deep Learning code with GPU/TPU support — no local setup required.

---

## 🛠️ 10. Building a Neuron — First Implementation

A hands-on example of creating a **single neuron** using `torch.nn`.

The neuron computes the linear equation:

$$
y = \sum_{i=1}^{n} w_i x_i + b
$$

```python
import torch
import torch.nn as nn

# Create input
torch.manual_seed(42)  # generates the same random numbers after each run
inputs = torch.tensor([1.0, 2.0, 3.0])

# Create a single neuron
neuron = nn.Linear(in_features=3, out_features=1)

# Get output from the neuron
output = neuron(inputs)
output

# View weight and bias
neuron.weight
neuron.bias

# Verify manually using the formula: y = Σ(xi * wi) + b
neuron.weight @ inputs + neuron.bias
```

---

<div align="center">

## 🙌 Made with ❤️ by

### **Sayan**

<a href="https://www.linkedin.com/in/sayanpal04?utm_source=share_via&utm_content=profile&utm_medium=member_android" target="_blank">
  <img src="https://img.shields.io/badge/LinkedIn-Connect%20with%20Sayan-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect with Sayan on LinkedIn"/>
</a>

⭐ *If these notes helped you, consider giving a star!* ⭐

</div>
