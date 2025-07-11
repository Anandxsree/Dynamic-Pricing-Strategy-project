# 💸 Dynamic Pricing Strategy Analysis

Welcome to the **Dynamic Pricing Strategy Analysis** project! This repository showcases a simulation-based pricing engine for an online store. It uses consumer behavior modeling and competitor pricing simulations to optimize pricing for revenue growth.

---

## 🔍 Project Overview

The goal of this project is to develop a **dynamic pricing model** that:

* Simulates competitor price changes
* Models consumer response to pricing strategies
* Optimizes prices to **maximize store revenue** while staying competitive

---

## 📁 Project Structure

```bash
Dynamic-Pricing-Strategy-project/
├── scripts/                     # Python scripts for data, modeling, pricing, visualization
│   ├── generate_consumer_data.py
│   ├── consumer_model.py
│   ├── dynamic_pricing.py
│   ├── test_pricing.py
│   ├── update_store_prices.py
│   └── visualize_results.py
├── data/                        # CSVs: consumer data, store catalog, test results
├── plots/                       # Visualizations (e.g., price comparison chart)
│   └── price_comparison.png
├── reports/                     # Report and presentation files
│   └── dynamic_pricing_report.md
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## 🚀 Setup Instructions

### 📦 Prerequisites

* Python 3.x
* MySQL (for pricing\_db setup)
* Git

### 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/Anandxsree/Dynamic-Pricing-Strategy-project.git
cd Dynamic-Pricing-Strategy-project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 🛠️ Setup MySQL

* Create a database named `pricing_db`
* Update MySQL credentials in script files (if needed)

---

## ▶️ Run the Workflow

Run scripts in the following order:

```bash
python scripts/generate_consumer_data.py
python scripts/consumer_model.py
python scripts/dynamic_pricing.py
python scripts/test_pricing.py
python scripts/update_store_prices.py
python scripts/visualize_results.py
```

---

## 📈 Results

* **Dynamic Pricing**: Updated prices led to a **4.5% increase in projected revenue**
* **Visualization**: See `plots/price_comparison.png` for before/after price comparison
* **Report**: Detailed explanation in `reports/dynamic_pricing_report.md`

---

## 🔮 Future Work

* Deploy in a real-time production environment (e.g., e-commerce store)
* Integrate **seasonality** and **customer demographic segmentation**
