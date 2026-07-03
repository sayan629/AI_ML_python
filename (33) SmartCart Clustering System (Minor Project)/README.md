# 🛒 SmartCart Customer Segmentation using Machine Learning

<p align="center">
  <img src="https://img.icons8.com/color/96/shopping-cart.png" alt="SmartCart"/>
  <img src="https://img.icons8.com/color/96/artificial-intelligence.png" alt="AI"/>
  <img src="https://img.icons8.com/color/96/combo-chart.png" alt="Analytics"/>
</p>

<p align="center">
  <b>An End-to-End Unsupervised Machine Learning Project for Customer Segmentation using PCA, K-Means, and Agglomerative Clustering.</b>
</p>

---

## 📌 Project Overview

Customer segmentation is one of the most important applications of Machine Learning in retail and e-commerce. Different customers have different purchasing behaviors, making personalized marketing strategies essential for improving customer satisfaction and increasing business revenue.

In this project, SmartCart customers are segmented into meaningful groups using **Unsupervised Machine Learning** techniques. The project covers the complete ML workflow—from data preprocessing and feature engineering to dimensionality reduction, clustering, and business insights.

---

## 🎯 Objectives

- Clean and preprocess customer data
- Handle missing values
- Perform feature engineering
- Detect and remove outliers
- Encode categorical variables
- Standardize numerical features
- Apply Principal Component Analysis (PCA)
- Determine the optimal number of clusters
- Compare K-Means and Agglomerative Clustering
- Analyze customer segments and generate business insights

---

## 📂 Dataset Features

The dataset contains customer demographic and purchasing information, including:

- Year of Birth
- Education
- Marital Status
- Income
- Number of Children
- Registration Date
- Product Spending
- Purchase Frequency
- Campaign Responses
- Web, Store & Catalog Purchases
- Customer Complaints

---

## ⚙️ Project Workflow

```text
📂 Load Dataset
        │
        ▼
🧹 Data Preprocessing
        │
        ▼
⚙️ Feature Engineering
        │
        ▼
📊 Exploratory Data Analysis
        │
        ▼
🚫 Outlier Detection & Removal
        │
        ▼
🔄 One-Hot Encoding
        │
        ▼
📏 Feature Scaling
        │
        ▼
📉 Principal Component Analysis (PCA)
        │
        ▼
🎯 Elbow Method & Silhouette Score
        │
        ▼
🤖 K-Means Clustering
        │
        ▼
🌳 Agglomerative Clustering
        │
        ▼
📈 Cluster Visualization
        │
        ▼
💡 Business Insights
```

---

# 🧰 Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Dimensionality Reduction | PCA |
| Clustering | K-Means, Agglomerative Clustering |

---

# 📊 Exploratory Data Analysis

The following analyses were performed:

- Missing Value Analysis
- Feature Engineering
- Pair Plot Visualization
- Correlation Heatmap
- Outlier Detection
- Feature Scaling
- Principal Component Analysis (2D & 3D)

---

# 🧠 Machine Learning Models

### ✅ K-Means Clustering

- Centroid-based clustering
- Fast and efficient
- Suitable for spherical clusters

---

### ✅ Agglomerative Clustering

- Hierarchical clustering approach
- Produces more compact clusters
- Better cluster separation for this dataset

---

# 📈 Model Evaluation

The optimal number of clusters was determined using:

- 📉 Elbow Method
- 📊 Silhouette Score

Both methods suggested an optimal value of:

## **K = 4**

---

# 📌 Results

After comparing both clustering techniques:

| Algorithm | Performance |
|------------|------------|
| K-Means | Good |
| Agglomerative Clustering | ⭐ Better |

Agglomerative Clustering produced more compact and meaningful customer segments than K-Means.

---

# 💡 Business Insights

The identified customer segments can help businesses:

- 🎯 Personalized Marketing Campaigns
- ❤️ Improve Customer Retention
- 💰 Increase Revenue
- 📦 Product Recommendations
- 📈 Better Decision Making
- 👥 Customer Behavior Analysis

---

# 📷 Project Screenshots

> Add your notebook screenshots here.

```
images/
│── pairplot.png
│── heatmap.png
│── elbow_method.png
│── silhouette_score.png
│── pca_2d.png
│── pca_3d.png
│── kmeans_clusters.png
│── agglomerative_clusters.png
```

Example:

```markdown
## Pair Plot

![Pair Plot](images/pairplot.png)

## Correlation Heatmap

![Heatmap](images/heatmap.png)

## PCA Visualization

![PCA](images/pca_3d.png)

## Agglomerative Clustering

![Clusters](images/agglomerative_clusters.png)
```

---

# 📁 Project Structure

```
SmartCart-Customer-Segmentation/
│
├── data/
│   └── marketing_campaign.csv
│
├── images/
│   ├── pairplot.png
│   ├── heatmap.png
│   ├── elbow_method.png
│   ├── silhouette_score.png
│   ├── pca_2d.png
│   ├── pca_3d.png
│   ├── kmeans_clusters.png
│   └── agglomerative_clusters.png
│
├── notebooks/
│   └── SmartCart_Customer_Segmentation.ipynb
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/your-username/SmartCart-Customer-Segmentation.git
```

Navigate to the project folder

```bash
cd SmartCart-Customer-Segmentation
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Jupyter Notebook

```bash
jupyter lab
```

or

```bash
jupyter notebook
```

---

# 📦 Requirements

```
numpy
pandas
matplotlib
seaborn
scikit-learn
kneed
jupyterlab
```

---

# 🎓 Learning Outcomes

Through this project, I gained hands-on experience with:

- Data Cleaning
- Feature Engineering
- Data Visualization
- Principal Component Analysis (PCA)
- Unsupervised Learning
- K-Means Clustering
- Agglomerative Clustering
- Model Evaluation
- Business Analytics

---

# 🌟 Future Improvements

- Apply DBSCAN
- Gaussian Mixture Models (GMM)
- Interactive Dashboard using Streamlit
- Deploy the model
- Real-time Customer Segmentation

---

<div align="center">

## 👨‍💻 Made with ❤️ by Sayan Pal

🎓 **MCA Student @ KIIT University**  
🤖 **AI | Machine Learning | Data Science**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sayan%20Pal-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sayanpal04/)

⭐ If you enjoyed this project, don't forget to **Star** this repository!

</div>
