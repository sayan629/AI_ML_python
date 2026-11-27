<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venom&color=0:0f0c29,50:302b63,100:24243e&height=300&section=header&text=Generative%20AI&fontSize=80&fontColor=ffffff&animation=twinkling&fontAlignY=38&desc=%E2%9C%A8%20LLMs%20%C2%B7%20Transformers%20%C2%B7%20Attention%20%E2%9C%A8&descSize=24&descAlignY=60&stroke=a855f7&strokeWidth=2" alt="Generative AI Banner" width="100%"/>

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&duration=3000&pause=900&color=A855F7&center=true&vCenter=true&width=720&height=50&lines=Deep+Learning+%E2%80%A2+Part+7+%2F+GenAI+Part+1;What+are+LLMs%3F+%F0%9F%A7%A0;Static+vs+Contextual+Embeddings+%F0%9F%94%A2;Transformer+Architecture+%F0%9F%8F%97%EF%B8%8F;Attention+Is+All+You+Need+%F0%9F%8E%AF" alt="Typing SVG" />
</a>

<br/>

<img src="https://img.shields.io/badge/Generative%20AI-8A2BE2?style=for-the-badge&logo=openai&logoColor=white"/>
<img src="https://img.shields.io/badge/Transformers-FF6F00?style=for-the-badge&logo=huggingface&logoColor=white"/>
<img src="https://img.shields.io/badge/LLMs-0A66C2?style=for-the-badge&logo=anthropic&logoColor=white"/>
<img src="https://img.shields.io/badge/Deep%20Learning-E91E63?style=for-the-badge&logo=tensorflow&logoColor=white"/>
<img src="https://img.shields.io/badge/Beginner-Friendly-2EA44F?style=for-the-badge"/>

<br/><br/>

<img src="https://img.shields.io/badge/Paper-Attention%20Is%20All%20You%20Need%20(2017)-black?style=flat-square&logo=arxiv&logoColor=white"/>
<img src="https://img.shields.io/badge/Notes%20by-Sayan%20Pal-a855f7?style=flat-square&logo=bookstack&logoColor=white"/>
<img src="https://img.shields.io/badge/Made%20with-Markdown-1f1f1f?style=flat-square&logo=markdown&logoColor=white"/>

</div>

<br/>

> [!NOTE]
> A clean, visual walkthrough of **Generative AI**: from *"what is an LLM?"* all the way to the maths behind **Scaled Dot-Product Attention**.

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,2,24&height=3" width="100%"/>

## 🧭 Roadmap

<div align="center">

| | | |
|:---:|:---:|:---:|
| **🎨 01**<br/>[Intro to GenAI](#-1-introduction-to-genai) | **🧠 02**<br/>[What are LLMs?](#-2-what-are-llms) | **⚡ 03**<br/>[Intro to Transformers](#-3-introduction-to-transformers) |
| **🔢 04**<br/>[Static vs Contextual](#-4-embeddings-static-vs-contextual) | **🏗️ 05**<br/>[Architecture Overview](#️-5-transformer-architecture-overview) | **🔄 06**<br/>[Encoder & Decoder](#-6-encoder--decoder) |
| **🧬 07**<br/>[Transformer Variants](#-7-various-transformer-architectures) | **🎯 08**<br/>[Attention Is All You Need](#-8-attention-is-all-you-need) | **🧮 09**<br/>[Scaled Dot-Product](#-9-scaled-dot-product-attention) |

</div>

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,2,24&height=3" width="100%"/>

## 🎨 1. Introduction to GenAI

> **Generative AI (GenAI)** is a subfield of AI that **creates new content**, such as audio, video, images, text and more.

<div align="center">

| 🖼️ Images | 🎵 Audio | 🎬 Video | 💬 Text | 💻 Code |
|:---:|:---:|:---:|:---:|:---:|
| Generate art | Generate speech & music | Generate clips | Chat & write | Write programs |

</div>

### 🛠️ Popular GenAI Tools

<div align="center">

| 🟠 Claude | 🟢 ChatGPT | 🔵 Copilot |
|:---:|:---:|:---:|
| by **Anthropic** | by **OpenAI** | by **Microsoft** |

</div>

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,2,24&height=3" width="100%"/>

## 🧠 2. What are LLMs?

**Language Model:** an AI system used to **predict the most likely next word based on context**.

```text
How are ____ ?   ──▶   you
```

**LLM (Large Language Model):** an advanced AI system trained on a **huge amount of data** to **understand, generate or summarize** human language and code.

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#ede9fe','primaryBorderColor':'#8b5cf6','primaryTextColor':'#1f1f1f','lineColor':'#8b5cf6','fontSize':'16px'}}}%%
flowchart LR
    G(["🎨 Generative AI"]) --- L(("🧠 LLM")) --- N(["📚 NLP"])
    style L fill:#8b5cf6,color:#ffffff,stroke:#6d28d9,stroke-width:3px
    style G fill:#fce7f3,stroke:#ec4899
    style N fill:#dbeafe,stroke:#3b82f6
```

> [!TIP]
> LLMs live at the **intersection of GenAI and NLP**.

### 🆚 Application vs. Engine (LLM)

<div align="center">

| 📱 Application | ⚙️ Engine behind it (LLM) |
|:---:|:---:|
| **ChatGPT** | GPT-4o, GPT-4 |
| **Gemini** | Gemini 2.5 Flash, Gemini Nano |

</div>

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,2,24&height=3" width="100%"/>

## ⚡ 3. Introduction to Transformers

- 📅 Introduced in **2017** in the research paper **"Attention Is All You Need"**
- 🧩 Transformers are a **neural network architecture** that uses **attention** to understand the relationships between **tokens** and generate meaningful output.

<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/8f/The-Transformer-model-architecture.png" alt="Transformer Model Architecture" width="380"/>
  <br/>
  <sub><i>The Transformer architecture · Source: Wikimedia Commons</i></sub>
</div>

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,2,24&height=3" width="100%"/>

## 🔢 4. Embeddings: Static vs Contextual

> **Embedding** = a **numerical representation of each token.**

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#ede9fe','primaryBorderColor':'#8b5cf6','lineColor':'#8b5cf6'}}}%%
flowchart LR
    T["📝 I Like Python"] -->|Tokenization| A["I"] & B["Like"] & C["Python"]
    A --> A1["[0.1, 0.9]"]
    B --> B1["[0.32, 0.41]"]
    C --> C1["[0.8, 0.2]"]
    style T fill:#8b5cf6,color:#fff
```

Each number captures a feature, such as *"Is it a mammal?"* or *"Is it a language?"*.

> [!IMPORTANT]
> In **GPT-3**, embeddings have **≈ 12,288 dimensions** (12K+).

### 🧊 Static  vs  🌊 Contextual

<div align="center">

| | 🧊 **Static Embeddings** | 🌊 **Contextual Embeddings** |
|:---|:---|:---|
| **Idea** | One **fixed vector** per word, regardless of context | **Different vectors** based on context |
| **Examples** | Word2Vec, GloVe | GPT-style models, BERT |
| `book` in *"I will read **book**"* | `[0.21, 0.54, 0.73, …]` | `[0.91, 0.23, 0.45, …]` |
| `book` in *"I will **book** tickets"* | `[0.21, 0.54, 0.73, …]` ⚠️ *same!* | `[0.12, 0.84, 0.31, …]` ✅ *different!* |

</div>

> [!TIP]
> ⭐ **Modern GenAI is built on contextual embeddings.**

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,2,24&height=3" width="100%"/>

## 🏗️ 5. Transformer Architecture Overview

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#ede9fe','primaryBorderColor':'#8b5cf6','lineColor':'#6d28d9','fontSize':'15px'}}}%%
flowchart TD
    A(["📝 Input Text"]) --> B["Tokenizer"]
    B --> C["Token Embeddings"]
    C --> D["Positional Encoding"]
    D --> E1

    subgraph ENC ["🔵 ENCODER  (repeat N times)"]
        direction TB
        E1["Multi-Head Self Attention"] --> E2["Add & Norm"]
        E2 --> E3["Feed Forward Network"]
        E3 --> E4["Add & Norm"]
    end

    E4 --> F1

    subgraph DEC ["🟣 DECODER"]
        direction TB
        F1["Masked Self Attention"] --> F2["Add & Norm"]
        F2 --> F3["Cross-Attention"]
        F3 --> F4["Add & Norm"]
        F4 --> F5["Feed Forward Network"]
        F5 --> F6["Add & Norm"]
    end

    F6 --> G["Linear Layer"]
    G --> H["Softmax Probability"]
    H --> I(["✅ Next Token"])

    style A fill:#fde68a,stroke:#f59e0b
    style I fill:#bbf7d0,stroke:#22c55e
    style ENC fill:#dbeafe,stroke:#3b82f6
    style DEC fill:#f3e8ff,stroke:#a855f7
```

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,2,24&height=3" width="100%"/>

## 🔄 6. Encoder & Decoder

<div align="center">

| 🔵 Encoder | 🟣 Decoder |
|:---:|:---:|
| Understands our speech/text **in terms of embeddings** | Used for **translation / generation** |

</div>

### 🗣️ Example: Translation

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#ede9fe','primaryBorderColor':'#8b5cf6','lineColor':'#8b5cf6'}}}%%
flowchart LR
    I["🇬🇧 I Like Python"] --> E["🔵 Encoder"]
    E --> V["Embeddings<br/>[I, Like, Python]"]
    V --> D["🟣 Decoder"]
    D --> S(["&lt;START&gt;"]) --> W1["আমি"] --> W2["পাইথন"] --> W3["পছন্দ"] --> W4["করি"] --> EOS(["&lt;EOS&gt;"])
    style E fill:#dbeafe,stroke:#3b82f6
    style D fill:#f3e8ff,stroke:#a855f7
```

At every step, the decoder picks the next word using **probabilities**:

<div align="center">

| Candidate word | Probability | |
|:---:|:---:|:---|
| **আমি** | **72 %** | ████████████████████ ✅ |
| আমার | 10 % | ███ |
| আপনি | 0.2 % | ▏ |

</div>

> `<START>` marks the beginning · `<EOS>` = **End of Sequence**

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,2,24&height=3" width="100%"/>

## 🧬 7. Various Transformer Architectures

<table align="center">
<tr>
<td width="50%" valign="top">

### 🔵 BERT
**Encoder-only** Transformer

- ✅ Text classification
- ✅ Sentiment analysis
- 👁️ **Understands** text only

</td>
<td width="50%" valign="top">

### 🟣 GPT
**Decoder-only** Transformer

- ✅ Chat
- ✅ Generation & coding
- ✍️ **Generates** text

</td>
</tr>
</table>

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,2,24&height=3" width="100%"/>

## 🎯 8. Attention Is All You Need

Attention decides **which information matters most** for a given query.

> **Query (Q):** *What is the capital of India?*

<div align="center">

| | Key (K) | Value (V) | Match Weight |
|:---:|:---:|:---|:---:|
| **R** | 🌍 Geography | Capital of India | 🟢 **0.80** · strong |
| **S** | ➗ Math | 2 + 2 = 4 | 🔴 **0.05** · low |
| **G** | 📜 History | Independence / Constitution of India | 🟡 **0.10** · medium |

</div>

> [!IMPORTANT]
> Attention depends on **3 components, Q · K · V**, which together produce the **attention score**: `Attention(Q, K, V)`

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,2,24&height=3" width="100%"/>

## 🧮 9. Scaled Dot-Product Attention

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#ede9fe','primaryBorderColor':'#8b5cf6','lineColor':'#8b5cf6'}}}%%
flowchart BT
    Q(["Q"]) --> M1["MatMul"]
    K(["K"]) --> M1
    M1 --> S["Scale"]
    S --> MK["Mask (optional)"]
    MK --> SM["Softmax"]
    SM --> M2["MatMul"]
    V(["V"]) --> M2
    M2 --> O(["✅ Attention Output"])
    style O fill:#bbf7d0,stroke:#22c55e
    style Q fill:#fde68a,stroke:#f59e0b
    style K fill:#fbcfe8,stroke:#ec4899
    style V fill:#bfdbfe,stroke:#3b82f6
```

### 🪜 Step-by-step

**1️⃣ &nbsp; Start with the input matrix `X`**

$$X \in \mathbb{R}^{n \times d}$$

`n` = number of tokens &nbsp;·&nbsp; `d` = embedding / model dimension

**2️⃣ &nbsp; Create Q, K, V** using learnable weights `W_Q`, `W_K`, `W_V`

$$Q = XW_Q \qquad K = XW_K \qquad V = XW_V$$

**3️⃣ &nbsp; Similarity score**

$$QK^T$$

**4️⃣ &nbsp; Scaling**

$$\frac{QK^T}{\sqrt{d_k}}$$

**5️⃣ &nbsp; Softmax**: converts the scores into **probabilities**

$$\text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)$$

**6️⃣ &nbsp; Second MatMul** with `V`

### ✅ Final Formula

$$\boxed{\;\text{Attention}(Q,K,V)=\text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V\;}$$

> [!TIP]
> ✨ **This is Scaled Dot-Product Attention.**

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,2,24&height=3" width="100%"/>

## 🗺️ Quick Summary

```mermaid
mindmap
  root((GenAI))
    LLMs
      Predict next word
      GPT-4o
      Gemini
    Embeddings
      Static
        Word2Vec
        GloVe
      Contextual
        BERT
        GPT
    Transformers
      Encoder
      Decoder
      Attention Q K V
    Architectures
      BERT = Encoder only
      GPT = Decoder only
```

<br/>

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=140&section=footer" width="100%"/>

### ✍️ Made with ❤️ by **Sayan Pal**

<a href="https://www.linkedin.com/in/sayanpal04/">
  <img src="https://img.shields.io/badge/Connect%20on%20LinkedIn-Sayan%20Pal-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
</a>

<br/><br/>

<sub>⭐ If these notes helped you, drop a star on the repo and share it with a friend!</sub>

</div>
