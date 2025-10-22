# Market Basket Analysis for Sena Grocery Platform

## 📋 Project Overview

This project implements **Market Basket Analysis** using **Association Rule Mining** algorithms (Apriori and FP-Growth) to identify frequently bought together product relationships for Sena, an online grocery platform.

## 🎯 Business Objectives

Identify "frequently bought together" relationships between products (SKUs) to enable:

1. **Bundle Suggestion System**: Recommend product combinations that customers are likely to purchase together
2. **Strategic Promotions**: Design logical "buy A get B" promotional campaigns based on actual purchasing patterns  
3. **Inventory and App Optimization**: Optimize product arrangement in the application and warehouse by grouping complementary items

## 📊 Dataset Description

- **Source**: Sample extracted from Sena's internal transaction records
- **Period**: 10 days of historical purchase data from a district
- **Records**: 195,167 transactions
- **Products**: 4,127 unique SKUs
- **Customers**: 15,829 unique buyers
- **Orders**: 50,051 unique orders

### Dataset Columns
| Column | Description |
|--------|-------------|
| `ordernumber` | Unique identifier for each transaction |
| `orderdate` | The date of the transaction |
| `buyerid` | Anonymized customer identifier |
| `productid` | Unique identifier for the product (SKU) |
| `productname` | The name of the product (translated to English) |
| `cateid` | The category identifier for the product |
| `quantity` | The number of units purchased |
| `price` | The price of a single unit of the product |

## 🔬 Technical Approach

### Machine Learning Methodology
- **Type of Learning**: Unsupervised Learning
- **Type of Task**: Association Rule Mining
- **Algorithms**: Apriori Algorithm & FP-Growth Algorithm
- **Evaluation Metrics**: Support, Confidence, and Lift measures

### Performance Analysis
- Comparative analysis of both algorithms' performance
- Computational efficiency evaluation
- Scalability assessment
- Rule quality and interpretability analysis

## 🛠️ Tools and Technologies

- **Python** for algorithm implementation
- **Jupyter Notebook** for analysis and visualization
- **Machine Learning Libraries**: scikit-learn, mlxtend
- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn, plotly

## 📁 Project Structure

```
ML_Unsupervied_final_Project/
├── data/
│   ├── orderdetail.csv              # Original dataset (Vietnamese)
│   └── orderdetail_en.csv           # Translated dataset (English)
├── notebook/
│   └── final_project.ipynb          # Main analysis notebook
├── requirement.txt                   # Python dependencies
└── README.md                        # Project documentation
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Jupyter Notebook
- Required libraries (see `requirement.txt`)

### Installation
1. Clone the repository:
```bash
git clone https://github.com/hoangop/ML_unsupervised_final_project.git
cd ML_unsupervised_final_project
```

2. Install dependencies:
```bash
pip install -r requirement.txt
```

3. Launch Jupyter Notebook:
```bash
jupyter notebook
```

4. Open `notebook/final_project.ipynb` to run the analysis

## 📈 Key Results

The analysis generates association rules showing product relationships with metrics:
- **Support**: Frequency of itemset occurrence
- **Confidence**: Probability of consequent given antecedent
- **Lift**: How much more likely the consequent is given the antecedent

## 🎯 Business Applications

1. **Product Bundling**: Create attractive product combinations
2. **Cross-selling**: Recommend complementary products
3. **Inventory Management**: Group related products in warehouse
4. **Marketing Campaigns**: Design targeted promotional offers
5. **App UX**: Optimize product arrangement in mobile app

## 📝 Project Repository

**GitHub URL**: https://github.com/hoangop/ML_unsupervised_final_project

## 👨‍💻 Author

**Hoang Nguyen** - CU Boulder ML Unsupervised Learning Final Project

## 📄 License

This project is for educational purposes as part of the CU Boulder Machine Learning course.

---

*Note: This project uses anonymized data from Sena's internal systems for research and educational purposes only.*