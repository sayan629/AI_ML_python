# 🧠 Deep Learning -- Part 6

## 🎬 Sentiment Analysis using RNN

> A practical deep-learning project for **binary sentiment
> classification** using the **IMDB Movie Reviews Dataset** and a
> **Recurrent Neural Network (RNN)** with PyTorch.

```{=html}
<p align="center">
```
`<b>`{=html}Text Cleaning → Tokenization → Sequence Processing →
Embedding → RNN → Training → Evaluation → Prediction`</b>`{=html}
```{=html}
</p>
```

------------------------------------------------------------------------

## 📌 About This Module

This module focuses on building an end-to-end **Natural Language
Processing (NLP)** pipeline for sentiment analysis.

The model learns from movie reviews and predicts whether a review
expresses a:

-   🟢 **Positive** sentiment
-   🔴 **Negative** sentiment

The project combines classical NLP preprocessing concepts with a
deep-learning workflow using **PyTorch**.

------------------------------------------------------------------------

## 📊 Dataset

### IMDB Movie Reviews Dataset

The project uses the **IMDB Dataset of 50K Movie Reviews**.

  Column        Description
  ------------- --------------------------
  `review`      Movie review text
  `sentiment`   `positive` or `negative`

### Example

``` text
Review:
"Watching Oz, you may become comfortable..."

Sentiment:
positive
```

``` text
Review:
"Some meaningless thriller spots..."

Sentiment:
negative
```

> ⚠️ The dataset is **not included in this repository** because of
> GitHub file-size limitations.

### 📥 Download Dataset

Download the dataset from Kaggle:

**IMDB Dataset of 50K Movie Reviews**

After downloading, place:

``` text
IMDB Dataset.csv
```

inside:

``` text
44. Deep Learning (Part 6)/Lecture Dataset/
```

Expected structure:

``` text
44. Deep Learning (Part 6)/
│
├── Lecture Dataset/
│   └── IMDB Dataset.csv
│
├── RNN Code/
│   └── ...
│
└── README.md
```

------------------------------------------------------------------------

# 🔄 NLP + Deep Learning Pipeline

``` mermaid
flowchart LR
    A[🎬 IMDB Reviews] --> B[🧹 Text Cleaning]
    B --> C[🛑 Stopword Processing]
    C --> D[🌱 Stemming]
    D --> E[🔢 Tokenization]
    E --> F[📏 Sequence Padding]
    F --> G[🧠 Embedding Layer]
    G --> H[🔁 RNN]
    H --> I[🔗 Fully Connected Layer]
    I --> J[📈 Sigmoid]
    J --> K[🎯 Sentiment Prediction]
```

------------------------------------------------------------------------

# 1️⃣ Problem Definition

### Problem Type

**Supervised Learning → Binary Text Classification**

### Objective

Given a movie review:

``` text
"This movie was absolutely fantastic!"
```

the model should predict:

``` text
Positive
```

For:

``` text
"This film was boring and terrible."
```

the model should predict:

``` text
Negative
```

------------------------------------------------------------------------

# 2️⃣ Text Preprocessing

Raw text cannot be directly processed by a neural network.

Therefore, the review must first be cleaned and transformed into a
numerical representation.

## 🧹 Regex Cleaning

Regular expressions are used to remove unnecessary characters and HTML
tags.

Typical operations include:

-   Remove HTML tags
-   Remove special characters
-   Remove punctuation
-   Remove numbers
-   Remove extra spaces
-   Convert text to lowercase

### Example

**Before**

``` text
I loved this movie!!! <br/>
```

**After**

``` text
i loved this movie
```

### Example Code

``` python
import re

def clean_text(text):
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.lower()
    text = re.sub(r'\s+', ' ', text).strip()
    return text
```

------------------------------------------------------------------------

# 3️⃣ Stopword Removal

Stopwords are common words that may contribute relatively little to the
classification task.

Examples:

``` text
the
is
was
are
and
of
```

Using NLTK:

``` python
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

filtered_words = [
    word for word in words
    if word not in stop_words
]
```

### Example

``` text
Before:
"This movie was really very good"

After:
"movie really good"
```

------------------------------------------------------------------------

# 4️⃣ 🌱 Stemming

Stemming attempts to reduce words to a common root form.

Examples:

``` text
running  → run
played   → play
movies   → movi
```

Using the Porter Stemmer:

``` python
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

stemmed_words = [
    stemmer.stem(word)
    for word in words
]
```

> 💡 Note: Stemming is a preprocessing technique. The exact stem does
> not always form a grammatically valid English word,
> e.g. `movies → movi`.

------------------------------------------------------------------------

# 5️⃣ 🔢 Text → Numbers

Neural networks operate on numerical tensors, not raw text.

A typical RNN pipeline converts:

``` text
"This movie was fantastic"
```

into something conceptually similar to:

``` text
[12, 48, 7, 931]
```

These token IDs are then passed into an **Embedding Layer**.

### Important Note

**TF-IDF** is an important text-vectorization technique and is useful
for traditional machine-learning models such as Logistic Regression,
Naive Bayes, and SVM.

For an RNN-based deep-learning pipeline, however, the usual approach is:

``` text
Text
 ↓
Tokenization
 ↓
Integer Sequence
 ↓
Padding
 ↓
Embedding
 ↓
RNN
```

So TF-IDF and RNN embeddings should be treated as **alternative
representations**, rather than mandatory consecutive steps.

------------------------------------------------------------------------

# 6️⃣ 📦 Dataset & DataLoader

PyTorch provides:

``` python
Dataset
DataLoader
```

to efficiently prepare and feed training data to the model.

### Typical Flow

``` text
Dataset
   ↓
DataLoader
   ↓
Mini-batches
   ↓
RNN
```

### Why DataLoader?

-   ⚡ Efficient batch processing
-   💾 Better memory usage
-   🔀 Supports shuffling
-   🚀 Works well with GPU training
-   📈 Makes training loops cleaner

Example:

``` python
from torch.utils.data import DataLoader

train_loader = DataLoader(
    train_dataset,
    batch_size=64,
    shuffle=True
)
```

------------------------------------------------------------------------

# 7️⃣ 🧠 RNN Architecture

A Recurrent Neural Network processes sequential information.

For example:

``` text
"This movie was very good"
```

can be processed as:

``` text
This
 ↓
movie
 ↓
was
 ↓
very
 ↓
good
```

The RNN maintains a hidden state that carries information from previous
time steps.

## 🏗️ Model Architecture

``` mermaid
flowchart TD
    A[Input Token IDs] --> B[Embedding]
    B --> C[RNN Layer]
    C --> D[Hidden State]
    D --> E[Fully Connected Layer]
    E --> F[Sigmoid]
    F --> G[Positive / Negative]
```

### PyTorch Example

``` python
import torch
import torch.nn as nn

class RNNModel(nn.Module):
    def __init__(
        self,
        vocab_size,
        embedding_dim,
        hidden_dim
    ):
        super().__init__()

        self.embedding = nn.Embedding(
            vocab_size,
            embedding_dim
        )

        self.rnn = nn.RNN(
            embedding_dim,
            hidden_dim,
            batch_first=True
        )

        self.fc = nn.Linear(
            hidden_dim,
            1
        )

    def forward(self, x):
        x = self.embedding(x)

        output, hidden = self.rnn(x)

        out = self.fc(
            hidden[-1]
        )

        return out
```

------------------------------------------------------------------------

# 8️⃣ ⚙️ Training the Model

The model is trained using the standard deep-learning optimization
cycle.

### Training Process

``` mermaid
flowchart LR
    A[Input Batch] --> B[Forward Pass]
    B --> C[Prediction]
    C --> D[Calculate Loss]
    D --> E[Backpropagation]
    E --> F[Update Weights]
    F --> A
```

### Core Steps

### 1. Forward Pass

``` python
output = model(x_batch)
```

### 2. Calculate Loss

``` python
loss = criterion(
    output,
    y_batch
)
```

### 3. Backpropagation

``` python
loss.backward()
```

### 4. Update Parameters

``` python
optimizer.step()
```

### Complete Training Pattern

``` python
for epoch in range(epochs):

    model.train()

    for x_batch, y_batch in train_loader:

        optimizer.zero_grad()

        output = model(x_batch)

        loss = criterion(
            output,
            y_batch
        )

        loss.backward()

        optimizer.step()
```

------------------------------------------------------------------------

# 9️⃣ 📈 Model Evaluation

After training, the model must be evaluated on unseen data.

Common classification metrics include:

  Metric      Meaning
  ----------- ----------------------------------------------------
  Accuracy    Percentage of correct predictions
  Precision   How many predicted positives are actually positive
  Recall      How many actual positives were identified
  F1 Score    Harmonic mean of precision and recall

### Example

``` text
Accuracy = 88%
```

means approximately:

``` text
88 out of every 100 predictions
were classified correctly.
```

------------------------------------------------------------------------

# 🔟 🎯 Sentiment Prediction

Once trained, the model can classify new reviews.

### Example 1

``` text
"This movie was absolutely fantastic!"
```

Prediction:

``` text
🟢 Positive
```

### Example 2

``` text
"This film was boring and terrible."
```

Prediction:

``` text
🔴 Negative
```

------------------------------------------------------------------------

# 🧩 Complete Project Architecture

``` mermaid
flowchart TD
    A[IMDB Dataset] --> B[Text Cleaning]
    B --> C[Stopword Processing]
    C --> D[Stemming]
    D --> E[Tokenization]
    E --> F[Integer Encoding]
    F --> G[Padding]
    G --> H[PyTorch Dataset]
    H --> I[DataLoader]
    I --> J[Embedding]
    J --> K[RNN]
    K --> L[Fully Connected]
    L --> M[Sigmoid]
    M --> N[Sentiment]
    N --> O[Evaluation]
```

------------------------------------------------------------------------

# 🛠️ Technologies & Libraries

```{=html}
<p align="center">
```
**Python** • **PyTorch** • **NLTK** • **Pandas** • **NumPy** •
**Scikit-learn** • **Regex**

```{=html}
</p>
```
### Core Concepts

-   🐍 Python
-   🔥 PyTorch
-   🧠 Deep Learning
-   🔁 Recurrent Neural Networks
-   💬 Natural Language Processing
-   🧹 Text Preprocessing
-   📊 Binary Classification
-   📈 Model Evaluation

------------------------------------------------------------------------

# 📚 What I Learned

By completing this module, I learned how to build an NLP deep-learning
pipeline from raw text to predictions.

### NLP

-   ✅ Regex-based text cleaning
-   ✅ Stopword processing
-   ✅ Stemming
-   ✅ Tokenization
-   ✅ Numerical text representation
-   ✅ Sequence preparation

### Deep Learning

-   ✅ PyTorch datasets
-   ✅ DataLoaders
-   ✅ Embedding layers
-   ✅ RNN architecture
-   ✅ Hidden states
-   ✅ Forward propagation
-   ✅ Loss calculation
-   ✅ Backpropagation
-   ✅ Optimizer-based weight updates
-   ✅ Model evaluation
-   ✅ Sentiment prediction

------------------------------------------------------------------------

# 💡 Key Learning

> **An RNN is designed to process sequential data by carrying
> information from previous time steps through its hidden state.**

For NLP, this makes RNNs useful for tasks such as:

``` text
📝 Sentiment Analysis
💬 Text Classification
🌐 Language Modeling
🔤 Sequence Prediction
📖 Text Generation
```

------------------------------------------------------------------------

# ⚠️ Important Practical Note

For modern NLP projects, basic RNNs are often replaced or supplemented
by architectures such as:

``` text
RNN
 ↓
LSTM / GRU
 ↓
Transformer
 ↓
BERT / Modern LLMs
```

Nevertheless, implementing an RNN from scratch is an excellent way to
understand:

-   Sequential processing
-   Hidden states
-   Embeddings
-   Backpropagation through time
-   Text classification

------------------------------------------------------------------------

# 📂 Suggested Repository Structure

``` text
44. Deep Learning (Part 6)/
│
├── Lecture Dataset/
│   └── IMDB Dataset.csv
│
├── RNN Code/
│   └── sentiment_analysis_rnn.ipynb
│
├── Handwritten Digit Classification Assignment/
│   └── ...
│
├── Refer for MNIST Dataset/
│   └── ...
│
└── README.md
```

> 🔒 Keep large datasets outside Git when they exceed GitHub's file-size
> limits. You can also add dataset files to `.gitignore`.

------------------------------------------------------------------------

# 🚀 Future Improvements

This project can be extended by experimenting with:

-   🔁 LSTM
-   🔄 GRU
-   🧠 Bidirectional RNN
-   🧹 Improved text normalization
-   📊 Confusion matrix
-   📈 Training/validation curves
-   ⚡ GPU acceleration
-   🎯 Hyperparameter tuning
-   🧪 Dropout and regularization
-   🤗 Transformer-based sentiment analysis

------------------------------------------------------------------------

# 🏁 Final Takeaway

This module provided a complete introduction to **sentiment analysis
using recurrent neural networks**.

The complete journey is:

``` text
🎬 Movie Reviews
        ↓
🧹 Clean Text
        ↓
🔤 Process Tokens
        ↓
🔢 Convert Text to Sequences
        ↓
📦 Create Dataset & DataLoader
        ↓
🧠 Embedding
        ↓
🔁 RNN
        ↓
🎯 Classification
        ↓
📈 Evaluation
        ↓
💬 Sentiment Prediction
```

------------------------------------------------------------------------

## 👨‍💻 Made by Sayan Pal

```{=html}
<p align="center">
```
`<b>`{=html}AI / ML • Deep Learning • NLP • Python •
PyTorch`</b>`{=html}
```{=html}
</p>
```
```{=html}
<p align="center">
```
⭐ Learning • Building • Experimenting • Improving ⭐
```{=html}
</p>
```
```{=html}
<p align="center">
```
`<a href="https://www.linkedin.com/in/sayanpal04?utm_source=share_via&utm_content=profile&utm_medium=member_android">`{=html}
`<b>`{=html}🔗 Connect with Sayan on LinkedIn`</b>`{=html} `</a>`{=html}
```{=html}
</p>
```

------------------------------------------------------------------------

```{=html}
<p align="center">
```
`<i>`{=html}Part of my AI / ML Deep Learning learning
journey.`</i>`{=html}
```{=html}
</p>
```
