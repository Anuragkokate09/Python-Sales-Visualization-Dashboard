# 📊 **Python Sales Visualization Dashboard**
### *Automated Retail Data Analysis & Plotting*

---

## 📝 **PROJECT OVERVIEW**
This project demonstrates the use of **Python** to automate business reporting. By processing raw transactional datasets, the script generates a multi-dimensional dashboard that helps stakeholders identify revenue trends, inventory demand, and pricing correlations.

---

## 🛠️ **CORE VISUALIZATION FEATURES**
The script (`Matpotib.py`) performs a comprehensive analysis of the `Sales_100.csv` dataset, producing four critical views:

* 📈 **Trend Analysis (Line Plot):** Tracks the progression of total sales across orders to identify revenue peaks.
* 📊 **Product Insights (Bar Chart):** Ranks product categories based on their total contribution to revenue.
* 🔔 **Quantity Distribution (Histogram):** Analyzes the most frequent order sizes to assist with inventory and logistics planning.
* 📍 **Pricing Correlation (Scatter Plot):** Maps Unit Price against Total Price to validate pricing consistency and detect outliers.



---

## 📊 **DATASET STRUCTURE**
The tool is optimized to work with retail CSV data including:
- **`OrderID`**: Unique transaction reference.
- **`Product`**: Item name or category.
- **`Quantity`**: Items sold per order.
- **`UnitPrice`**: Price per individual unit.
- **`TotalPrice`**: Total revenue generated per line item.

---

## ⚙️ **TECHNICAL STACK**
* **Language:** `Python 3.x`
* **Libraries:** * `Pandas`: For data aggregation and CSV parsing.
    * `Matplotlib`: For generating high-quality static charts.
* **Key Techniques:** Data grouping (`groupby`), frequency distribution (bins), and customized axis labeling.

---

## 📈 **BUSINESS INSIGHTS GENERATED**
| Feature | Business Value |
| :--- | :--- |
| **Line Plot** | Monitors day-to-day revenue health. |
| **Bar Chart** | Identifies "Star Products" for marketing focus. |
| **Histogram** | Optimized stock replenishment based on purchase frequency. |
| **Scatter Plot** | Ensures pricing logic is consistent across the product range. |

---

## 🚀 **HOW TO RUN**
1. Ensure you have Python installed.
2. Install the required libraries:
   ```bash
   pip install pandas matplotlib
3. Place Sales_100.csv in the root directory.
4. Run the script:
   python Matpotib.py

---
