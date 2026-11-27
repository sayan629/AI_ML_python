<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venom&color=0:0f2027,50:203a43,100:2c5364&height=300&section=header&text=Inside%20Transformers&fontSize=70&fontColor=ffffff&animation=twinkling&fontAlignY=38&desc=%F0%9F%94%8D%20Attention%20%C2%B7%20Residuals%20%C2%B7%20Masking%20%C2%B7%20Pretraining%20%F0%9F%9A%80&descSize=22&descAlignY=60&stroke=22d3ee&strokeWidth=2" alt="Inside Transformers Banner" width="100%"/>

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&duration=3000&pause=900&color=22D3EE&center=true&vCenter=true&width=760&height=50&lines=Deep+Learning+%E2%80%A2+Part+8+%2F+GenAI+Part+2;Multi-Head+Attention+%F0%9F%A7%A0;Residual+Connections+%F0%9F%94%97;Masked+%26+Cross+Attention+%F0%9F%8E%AD;Pretrained+Transformers+%F0%9F%8E%93" alt="Typing SVG" />
</a>

<br/>

<img src="https://img.shields.io/badge/Generative%20AI-0891B2?style=for-the-badge&logo=openai&logoColor=white"/>
<img src="https://img.shields.io/badge/Transformers-FF6F00?style=for-the-badge&logo=huggingface&logoColor=white"/>
<img src="https://img.shields.io/badge/Attention-8A2BE2?style=for-the-badge&logo=pytorch&logoColor=white"/>
<img src="https://img.shields.io/badge/Deep%20Learning-E91E63?style=for-the-badge&logo=tensorflow&logoColor=white"/>
<img src="https://img.shields.io/badge/Beginner-Friendly-2EA44F?style=for-the-badge"/>

<br/><br/>

<img src="https://img.shields.io/badge/Part-8%20%2F%20GenAI%202-22d3ee?style=flat-square"/>
<img src="https://img.shields.io/badge/Notes%20by-Sayan%20Pal-0A66C2?style=flat-square&logo=bookstack&logoColor=white"/>
<img src="https://img.shields.io/badge/Made%20with-Markdown-1f1f1f?style=flat-square&logo=markdown&logoColor=white"/>

</div>

<br/>

> [!NOTE]
> The sequel to Part 7. This time we open the Transformer's engine: **multi-head attention, residual connections, FFN, cross-attention, masked attention**, and how **pretrained transformers** save us from training LLMs from scratch.

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,2,24&height=3" width="100%"/>

## 🧭 Roadmap

<div align="center">

| | | |
|:---:|:---:|:---:|
| **🔍 01**<br/>[Self & Multi-Head Attention](#-1-self-attention--multi-head-attention) | **🔗 02**<br/>[Residual Connections](#-2-residual-connections) | **🧪 03**<br/>[FFN in Encoder](#-3-ffn-in-encoder) |
| **🌉 04**<br/>[Cross-Attention](#-4-cross-attention-in-decoder) | **🎭 05**<br/>[Masked Attention](#-5-masked-attention-in-decoder) | **🧩 06**<br/>[Architecture Summary](#-6-summary-transformer-architecture) |
| **🎓 07**<br/>[Pretrained Transformers](#-7-pretrained-transformers) | **🌐 08**<br/>[Multiple Platforms](#-8-multiple-platforms) | |

</div>

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,2,24&height=3" width="100%"/>

## 🔍 1. Self-Attention & Multi-Head Attention

### 🎯 Single-Head Self-Attention

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#cffafe','primaryBorderColor':'#0891b2','lineColor':'#0891b2','fontSize':'15px'}}}%%
flowchart LR
    A(["📥 Input Embedding"]) --> B["Positional Encoding"] --> C["Scaled Dot-Product Attention"] --> D(["✅ Contextual Embedding"])
    style A fill:#fde68a,stroke:#f59e0b
    style D fill:#bbf7d0,stroke:#22c55e
```

### 🧠 Multi-Head Attention

> It uses **multiple attention mechanisms in parallel**, so the model can understand **different relationships between words at the same time**.

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#cffafe','primaryBorderColor':'#0891b2','lineColor':'#0891b2','fontSize':'15px'}}}%%
flowchart BT
    V(["V"]) --> LV["Linear"]
    K(["K"]) --> LK["Linear"]
    Q(["Q"]) --> LQ["Linear"]
    LV --> SDPA
    LK --> SDPA
    LQ --> SDPA
    SDPA["⚡ Scaled Dot-Product Attention  ×h heads"] --> CC["Concat"]
    CC --> LO["Linear"]
    LO --> OUT(["✅ Multi-Head Attention"])
    style SDPA fill:#ede9fe,stroke:#8b5cf6,stroke-width:2px
    style OUT fill:#bbf7d0,stroke:#22c55e
    style Q fill:#fde68a,stroke:#f59e0b
    style K fill:#fbcfe8,stroke:#ec4899
    style V fill:#bfdbfe,stroke:#3b82f6
```

### 🔀 Each head learns a different view

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#cffafe','primaryBorderColor':'#0891b2','lineColor':'#0891b2'}}}%%
flowchart LR
    I(["📥 Input Embedding"]) --> P["Positional Encoding"]
    P --> H1["Attention Head 1"] --> C1(["Contextual Embedding 1"])
    P --> H2["Attention Head 2"] --> C2(["Contextual Embedding 2"])
    P --> H3["Attention Head 3"] --> C3(["Contextual Embedding 3"])
    style H1 fill:#fecaca,stroke:#ef4444
    style H2 fill:#fde68a,stroke:#f59e0b
    style H3 fill:#bbf7d0,stroke:#22c55e
```

### 📚 Types of Attention

<div align="center">

| 🔵 Self Attention | 🟣 Cross Attention | 🟠 Masked Attention |
|:---:|:---:|:---:|
| Q, K, V from the **same sequence** | Q from **decoder**, K & V from **encoder** | Sees only **current + previous** tokens |

</div>

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,2,24&height=3" width="100%"/>

## 🔗 2. Residual Connections

> Instead of passing information only *through* layers, a **residual connection** lets the **original input skip some layers** and be **added to the final output**, preserving the original information.

$$\text{Output} = \text{LayerNorm}\big(x + \text{Sublayer}(x)\big)$$

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#cffafe','primaryBorderColor':'#0891b2','lineColor':'#0891b2','fontSize':'15px'}}}%%
flowchart BT
    S(["📝 Input Sequence"]) --> E["Input Embedding"]
    E --> PE(("➕"))
    POS["〰️ Positional Encoding"] --> PE

    subgraph ENC ["🔵 ENCODER LAYER  (×N)"]
        direction BT
        MH["Multi-Head Self-Attention<br/>(Q, K, V)"] --> A1(("➕"))
        A1 --> N1["Norm"]
        N1 --> FF["Feed Forward"]
        FF --> A2(("➕"))
        A2 --> N2["Norm"]
    end

    PE --> MH
    PE -. "🔗 residual connection" .-> A1
    N1 -. "🔗 residual connection" .-> A2
    N2 --> OUT(["✅ Encoder Output"])

    style ENC fill:#dbeafe,stroke:#3b82f6
    style OUT fill:#bbf7d0,stroke:#22c55e
    style S fill:#fde68a,stroke:#f59e0b
```

> [!TIP]
> Residual connections keep the **original signal alive** through deep stacks, which makes deep networks easier to train.

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,2,24&height=3" width="100%"/>

## 🧪 3. FFN in Encoder

<div align="center">

| 🎯 Attention | 🔧 Feed-Forward Network (FFN) |
|:---:|:---:|
| **Determines / gathers** the important information | **Transforms** that information to learn **richer features** |

</div>

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#cffafe','primaryBorderColor':'#0891b2','lineColor':'#0891b2'}}}%%
flowchart LR
    A["🎯 Attention<br/>(gather info)"] --> B["🔧 FFN<br/>(transform info)"] --> C(["✨ Richer Features"])
    style C fill:#bbf7d0,stroke:#22c55e
```

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,2,24&height=3" width="100%"/>

## 🌉 4. Cross-Attention in Decoder

> Cross-attention allows the **decoder** to **access and focus on relevant information from the encoder's output**.

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#cffafe','primaryBorderColor':'#0891b2','lineColor':'#0891b2','fontSize':'15px'}}}%%
flowchart LR
    EO["🔵 Encoder Output"] --> KV["Key (K)<br/>Value (V)"]
    DEC(["🟣 Decoder"]) --> MSA["Masked<br/>Self-Attention"]
    MSA -- "Q" --> CA["🌉 Cross-Attention"]
    KV -- "K, V" --> CA
    CA --> FFN["FFN"] --> OT(["✅ Output Token"])
    style CA fill:#ede9fe,stroke:#8b5cf6,stroke-width:2px
    style OT fill:#bbf7d0,stroke:#22c55e
```

### ⚖️ Self-Attention vs Cross-Attention

<div align="center">

| | 🔵 Self-Attention | 🟣 Cross-Attention |
|:---|:---|:---|
| **Q** | Same sequence | From **Decoder** |
| **K** | Same sequence | From **Encoder** |
| **V** | Same sequence | From **Encoder** |

</div>

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,2,24&height=3" width="100%"/>

## 🎭 5. Masked Attention in Decoder

> Masked attention ensures the decoder can **only see the current and previously generated tokens, not future tokens.**

### 🤔 How does it work?

Example sentence: **"I love AI today"**

<div align="center">

| Query ↓ / Key → | I | love | AI | today |
|:---:|:---:|:---:|:---:|:---:|
| **I** | ✅ | ❌ | ❌ | ❌ |
| **love** | ✅ | ✅ | ❌ | ❌ |
| **AI** | ✅ | ✅ | ✅ | ❌ |
| **today** | ✅ | ✅ | ✅ | ✅ |

</div>

### 🧮 The attention mask

$$M = \begin{bmatrix} 0 & -\infty & -\infty & -\infty \\ 0 & 0 & -\infty & -\infty \\ 0 & 0 & 0 & -\infty \\ 0 & 0 & 0 & 0 \end{bmatrix}$$

<div align="center">

| Value | Meaning |
|:---:|:---|
| **0** | ✅ Attention **allowed** |
| **−∞** | ⛔ Attention **blocked** |

</div>

The mask is added before softmax, so blocked positions become **zero probability**:

$$\text{softmax}\left(\frac{QK^T}{\sqrt{d_k}} + M\right)V$$

### 🆚 Masked Self-Attention vs Cross-Attention

<div align="center">

| 🟠 Masked Self-Attention | 🟣 Cross-Attention |
|:---:|:---:|
| Looks at **previous and current tokens** | Looks at the **encoder output** |

</div>

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,2,24&height=3" width="100%"/>

## 🧩 6. Summary: Transformer Architecture

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#cffafe','primaryBorderColor':'#0891b2','lineColor':'#0891b2','fontSize':'15px'}}}%%
flowchart TD
    A(["📝 Input Sequence"]) --> B["Tokenization + Embedding"]
    B --> C["Positional Encoding"]
    C --> D["🔵 Encoder<br/>Self-Attention + FFN"]
    D --> E["🟣 Decoder<br/>Masked Attention + Cross-Attention + FFN"]
    E --> F["Linear Layer + Softmax"]
    F --> G(["✅ Output Prediction"])
    style A fill:#fde68a,stroke:#f59e0b
    style D fill:#dbeafe,stroke:#3b82f6
    style E fill:#f3e8ff,stroke:#a855f7
    style G fill:#bbf7d0,stroke:#22c55e
```

<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/8f/The-Transformer-model-architecture.png" alt="Transformer Model Architecture" width="380"/>
  <br/>
  <sub><i>The Transformer architecture · Source: Wikimedia Commons</i></sub>
</div>

<br/>

> [!IMPORTANT]
> ⭐ **GPT** uses a **decoder-only** Transformer architecture.
> ⭐ **BERT** uses **masked language modelling**.

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,2,24&height=3" width="100%"/>

## 🎓 7. Pretrained Transformers

### 😰 Why not build an LLM from scratch?

Building an LLM from scratch is **complex** because it:

<div align="center">

| 📚 Needs millions of text samples | ⏳ Takes a lot of time | 💸 Is very expensive |
|:---:|:---:|:---:|

</div>

### 💡 Why we need pretrained transformers

<div align="center">

| 💰 Reduce cost | ⏱️ Save time | 📉 Need less data | 🚀 Better performance |
|:---:|:---:|:---:|:---:|

</div>

> **Definition:** A **pretrained transformer** model has **already been trained on a large amount of data**.

### ⚙️ How does it work?

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#cffafe','primaryBorderColor':'#0891b2','lineColor':'#0891b2','fontSize':'15px'}}}%%
flowchart TD
    A[("🗄️ Large Dataset")] --> B["Transformer Pre-training"]
    B --> C["🎓 Pre-trained Model<br/>(BERT / GPT / T5)"]
    C --> D["🔧 Fine-Tuning"]
    C --> E["💬 Prompting"]
    D --> F(["🎯 Specific AI Application"])
    E --> F
    style A fill:#fde68a,stroke:#f59e0b
    style C fill:#ede9fe,stroke:#8b5cf6,stroke-width:2px
    style F fill:#bbf7d0,stroke:#22c55e
```

### 🏛️ Popular Pretrained Transformers

<div align="center">

| # | Model | Architecture |
|:---:|:---:|:---:|
| 1 | **BERT** | 🔵 Encoder-only |
| 2 | **GPT** | 🟣 Decoder-only |
| 3 | **T5** *(Text-to-Text Transfer Transformer)* | 🔵🟣 Encoder-Decoder |
| 4 | **RoBERTa** | 🔵 Encoder-only |

</div>

### 🔧 Fine-Tuning

> **Fine-tuning** means taking a **pretrained model** and **training it further on a smaller dataset**.

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,2,24&height=3" width="100%"/>

## 🌐 8. Multiple Platforms

> [!NOTE]
> Pretrained transformers are available on many platforms, so you rarely need to start from zero.

<div align="center">

| 🤗 Hugging Face Hub | 🔥 PyTorch Hub | 🧠 TensorFlow Hub | ☁️ Cloud AI APIs |
|:---:|:---:|:---:|:---:|
| Thousands of ready models | Pretrained PyTorch models | Reusable TF modules | Hosted LLM services |

</div>

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,2,24&height=3" width="100%"/>

## 🗺️ Quick Summary

```mermaid
mindmap
  root((Transformers))
    Attention
      Self
      Multi-Head
      Cross
      Masked
    Encoder
      Self-Attention
      Residual + Norm
      FFN
    Decoder
      Masked Attention
      Cross-Attention
      FFN
    Pretrained
      BERT
      GPT
      T5
      RoBERTa
    Adapt
      Fine-Tuning
      Prompting
```

<br/>

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=140&section=footer" width="100%"/>

### ✍️ Made with ❤️ by **Sayan Pal**

<a href="https://www.linkedin.com/in/sayanpal04/">
  <img src="https://img.shields.io/badge/Connect%20on%20LinkedIn-Sayan%20Pal-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
</a>

<br/><br/>

<sub>⭐ If these notes helped you, drop a star on the repo and share it with a friend!</sub>

</div>
