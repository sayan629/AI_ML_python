<p align="center">
  <img src="https://logo.svgcdn.com/logos/matplotlib-icon.svg" alt="Matplotlib Logo" width="120"/>
</p>

<h1 align="center">📊 Matplotlib Complete Notes</h1>

<p align="center">
  A beginner-friendly guide covering all essential Matplotlib plotting techniques with examples and explanations.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python" />
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-orange?style=flat-square&logo=plotly" />
  <img src="https://img.shields.io/badge/Level-Beginner-green?style=flat-square" />
</p>

---

## 🚀 Getting Started

### Import Library

```python
import matplotlib.pyplot as plt
```

---

## 📈 Line Plot

```python
plt.plot(x, y)
plt.show()
```

> Used to draw a simple line graph.

---

## 🏷️ Title and Axis Labels

```python
plt.title("Graph Title")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
```

| Function | Description |
|----------|-------------|
| `title()` | Adds a heading to the graph |
| `xlabel()` | Labels the X-axis |
| `ylabel()` | Labels the Y-axis |

---

## 📌 Legend Function

```python
plt.plot(x, y, label="Data")
plt.legend(loc="upper right")
```

- Displays labels of plotted data
- `loc` → Sets the legend position

**Common Positions:**

| Position | Position |
|----------|----------|
| `upper right` | `upper left` |
| `lower right` | `lower left` |
| `center` | `best` |

---

## 🔀 Multiple Line Plots

```python
plt.plot(x, y1, label="Line 1")
plt.plot(x, y2, label="Line 2")
plt.legend()
```

> Used to compare multiple datasets on the same graph.

---

## 🎨 Line Customization

**Shorthand syntax:**

```python
plt.plot(x, y, "o--r")
```

| Symbol | Meaning |
|--------|---------|
| `o` | Circle marker |
| `--` | Dashed line |
| `r` | Red color |

**Explicit syntax:**

```python
plt.plot(x, y, color="red", marker="<", linestyle="-.", linewidth=3)
```

---

## 🧱 Styles and Grid

```python
plt.style.use("default")
plt.grid()
```

> Improves graph readability and visual appeal.

---

## ✏️ XKCD Style *(Cartoon Style)*

```python
with plt.xkcd():
    plt.plot(x, y)
    plt.show()
```

---

## 📊 Bar Chart

```python
plt.bar(x, y, color="green")
```

**Add values on top of bars:**

```python
for i in range(len(x)):
    plt.text(x[i], y[i], str(y[i]))
```

---

## 📊 Grouped Bar Chart

```python
import numpy as np

x = np.arange(len(data))
width = 0.4

plt.bar(x - width/2, y1, width)
plt.bar(x + width/2, y2, width)
```

---

## ↔️ Horizontal Bar Chart

```python
plt.barh(labels, values)
```

---

## 🔵 Scatter Plot

```python
plt.scatter(x, y)
```

### 🎯 Scatter Customization

```python
plt.scatter(x, y, c=y, cmap="OrRd", sizes=y)
plt.colorbar()
```

---

## 📝 Annotation

```python
plt.annotate("Text", xy=(x, y), xytext=(x+1, y+1))
```

---

## 🔄 Multiple Scatter Plot

```python
plt.scatter(x1, y1, label="Data1")
plt.scatter(x2, y2, label="Data2")
plt.legend()
```

---

## 📏 Axis Limits

```python
plt.xlim(min, max)
plt.ylim(min, max)
```

---

## 🥧 Pie Chart

```python
plt.pie(values, labels=labels)
```

### 🎯 Pie Chart Customization

```python
plt.pie(
    values,
    labels=labels,
    autopct="%1.1f%%",
    explode=[0, 0.1, 0, 0],
    startangle=45,
    shadow=True
)
```

| Parameter | Description |
|-----------|-------------|
| `autopct` | Shows percentage on slices |
| `explode` | Offsets a slice outward |
| `startangle` | Rotates the start of the chart |
| `shadow` | Adds a drop shadow effect |

---

## 📚 Summary Table

| Function | Purpose |
|----------|---------|
| `plot()` | Line graph |
| `bar()` | Bar chart |
| `barh()` | Horizontal bar chart |
| `scatter()` | Scatter plot |
| `pie()` | Pie chart |
| `title()` | Set graph title |
| `xlabel()` | X-axis label |
| `ylabel()` | Y-axis label |
| `legend()` | Show data labels |
| `grid()` | Add grid lines |
| `show()` | Display the graph |

---

## ✅ Final Tips

- ✔️ Always use `label` + `legend()` for clarity
- ✔️ Use styles, colors, and markers for better visualization
- ✔️ Keep graphs clean and readable
- ✔️ Use `plt.tight_layout()` to prevent overlapping elements

---

## ⭐ Contribution

Feel free to fork this repo and improve the notes! 🚀

---

<p align="center">
  Made with ❤️ by <strong>Sayan</strong> &nbsp;|&nbsp; Happy Plotting! 📊
</p>
