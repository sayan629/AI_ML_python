# 🧠 Deep Learning Notes — Part 4: CNN (Convolutional Neural Networks)

> Notes, cleaned up and organized into a proper reference guide.

---

## 📑 Table of Contents

1. [Neural Network Architectures](#1-neural-network-architectures)
2. [Computer Vision](#2-computer-vision)
3. [Why Not Normal ANN for Images?](#3-why-not-normal-ann-for-images)
4. [CNN Architecture](#4-cnn-architecture)
5. [Convolutional Layer](#5-convolutional-layer)
6. [Stride, Padding & Output Size](#6-stride-padding--output-size)
7. [Pooling Layer](#7-pooling-layer)
8. [Fully Connected Layer](#8-fully-connected-layer)
9. [Pipeline of CNN](#9-pipeline-of-cnn)

---

## 1. Neural Network Architectures

![FNN Architecture](images/img1_fnn_intro.jpg)

Deep Learning has several core architectures, each suited to a different type of data:

| Architecture | Best Suited For |
|---|---|
| **FNN** (Feed Forward Neural Network) | Regression & classification on tabular data (`.csv`) |
| **CNN** (Convolutional Neural Network) | Computer Vision |
| **RNN** (Recurrent Neural Network) | NLP (sequential data) |
| **Transformers** | Modern NLP / sequence modeling |
| **GANs** | Generative tasks |

### FNN (Feed Forward Neural Network)
A simple network where data flows in **one direction** — input → hidden layer(s) → output. Every neuron connects to every neuron in the next layer.

```
i/p layer → hidden layer(s) → o/p layer
```

**Used for:**
- ✅ Regression & classification problems
- ✅ Tabular data (`.csv`)

---

## 2. Computer Vision

![Computer Vision Basics](images/img2_computer_vision.jpg)

> **Computer Vision** = extracting meaningful information from images, videos, and visual data.

### 🎯 Real-World Applications
- Face Recognition
- Traffic systems
- Drones / Self-driving cars
- Self checkouts
- Medical diagnosis
- Instagram filters
- Surveillance tools

### 🎯 Core Tasks
1. **Object Detection**
2. **Tracking Movement**

### 🖼️ Black & White vs Color Images

**Black & White (Binary)**
- `0` → Black
- `1` → White

**Grayscale**
- Range: `0 – 255` (0 = Black, 255 = White)
- Shape: `4 × 4 × 1` → 1 **channel**

**Color Images (RGB)**
- Range: `0 – 255` per channel
- `Red + Green + Blue = RGB`
- Example: `Yellow = (255, 255, 0)`
- Shape: `4 × 4 × 3` → 3 **channels**

---

## 3. Why Not Normal ANN for Images?

Suppose we have a **224 × 224 RGB image**:

```
224 × 224 × 3 = 150,528 pixels
```

👉 All of these pixel values need to be fed into the ANN as individual input features — resulting in a **massive number of parameters** and **huge computational complexity**.

This is exactly why **CNNs** exist — they drastically reduce this complexity while preserving spatial/feature information.

---

## 4. CNN Architecture

![Convolutional Layer](images/img3_conv_layer.jpg)

The overall CNN pipeline flows through three major blocks:

```
Input Image → Convolutional Layer → Pooling Layer → Fully Connected Layer → ANN → Output
```

---

## 5. Convolutional Layer

### Step 1 — Min-Max Scaling
Before anything else, pixel values (`0–255`) are normalized to a `[0, 1]` range:

```
scaled_value = original_value / 255
```

So: `0 → 0` and `255 → 1`

### Step 2 — Apply Filter (Kernel)
A small matrix called a **filter/kernel** (e.g., `3×3`) slides over the image to detect features. This sliding operation is called **Convolution**.

**Example:**

Image (5×5, after min-max scaling):
```
0 0 1 1 0
0 0 1 1 0
0 0 1 1 0
1 0 1 0 1
0 0 1 0 1
```

Kernel (3×3):
```
 1  0 -1
 1  0 -1
 1  0 -1
```

**1st Convolution Sum:**
```
0+0+-1+0+0-1+0+0-1 = -3
```

➡️ Output is called the **Feature Map**:
```
-3  -3  ...
...
```

After the feature map is generated, **ReLU** activation is applied to introduce non-linearity.

> 🔍 **Function of the Kernel:** It scans the image and detects specific features like:
> - Edges
> - Lines
> - Curves
> - Shapes

---

## 6. Stride, Padding & Output Size

![Stride & Padding](images/img4_stride_padding.jpg)

### Stride
**Stride** = how many pixels the filter moves at each step.

### Output Size Formula

```
        n - f + 2p
O/P  =  ---------- + 1
            s
```

Where:
- `n` = input matrix size
- `f` = filter size
- `p` = padding
- `s` = stride

**Example:**
```
Input  = 5×5
Filter = 3×3
Stride = 2

O/P = (5 - 3)/2 + 1 = 1 + 1 = 2
```

### Padding
**Padding** means adding extra pixels (usually zeros) around the border of an image *before* applying the kernel.

**Example — Original Image (3×3):**
```
1 2 3
4 5 6
7 8 9
```

**With Padding = 1:**
```
0 0 0 0 0
0 1 2 3 0
0 4 5 6 0
0 7 8 9 0
0 0 0 0 0
```

### Why Do We Use Padding?
👉 To **preserve the image size** after convolution.

| | Without Padding | With Padding = 1 |
|---|---|---|
| Input | 5×5 | 5×5 |
| Kernel | 3×3 | 3×3 |
| Stride | 1 | 1 |
| **Output** | **3×3** (shrinks!) | **5×5** (size preserved!) |

### Types of Padding
1. **Valid** → No padding
2. **Zero** → Add zeros around the border

---

## 7. Pooling Layer

![Pooling Layer](images/img5_pooling.jpg)

> **Pooling** reduces the size of the feature map **while keeping the important features**.

### Example — 2×2 Max Pooling with Stride 2

Input (4×4), split into four 2×2 blocks:

```
Block 1     Block 2
1  3        2  1
4  6        5  2

Block 3     Block 4
7  2        8  3
1  2        3  4
```

Applying **Max Pooling** (take the max value from each block):

```
6  5
7  8
```

### Types of Pooling
1. **Max Pooling** — takes the maximum value
2. **Min Pooling** — takes the minimum value
3. **Average Pooling** — takes the average value

---

## 8. Fully Connected Layer

![Fully Connected Layer & Pipeline](images/img6_fc_pipeline.jpg)

The final pooled feature map is **flattened** into a 1D vector and fed into a fully connected **ANN**, which produces the final output.

```
Pooled Output (2×2)      Flatten           Fully Connected (ANN)
     6  5        →       [6, 5, 7, 8]  →      → Output
     7  8
```

---

## 9. Pipeline of CNN

The complete end-to-end CNN pipeline:

```
Input Image
     ↓
Convolution + ReLU
     ↓
Pooling
     ↓
Convolution + ReLU
     ↓
Pooling
     ↓
Feature Map
     ↓
Flatten
     ↓
Fully Connected Layer
     ↓
Apply Softmax (Activation Function)
     ↓
Output Layer
```

---

## 📌 Summary

| Layer | Purpose |
|---|---|
| **Convolutional Layer** | Extracts features (edges, curves, shapes) using kernels |
| **Pooling Layer** | Reduces spatial size while retaining key features |
| **Fully Connected Layer** | Flattens & classifies using a standard ANN |

---

<div align="center">

### ✨ Made with ❤️ by **[Sayan](https://www.linkedin.com/in/sayanpal04?utm_source=share_via&utm_content=profile&utm_medium=member_android)** ✨

</div>
