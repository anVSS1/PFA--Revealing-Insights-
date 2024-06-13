# Sales Analytics and Prediction Project

This project dives deep into customer sales data to uncover valuable insights for business decision-making. It leverages machine learning and time-series forecasting to predict customer churn,customer lifetime value (CLV) prediction, forecast product demand, and segment customers based on their purchasing behavior.

## Table of Contents

- [Project Overview](#project-overview)
- [Data](#data)
- [Models and Analyses](#models-and-analyses)
- [Power BI Dashboard](#power-bi-dashboard) 
- [Usage](#usage)
- [Limitations and Future Work](#limitations-and-future-work)

## Project Overview

This repository contains Jupyter Notebooks and Python scripts for comprehensive sales analysis, addressing these key business challenges:

1. **Customer Churn Prediction:**  Identifies customers at risk of leaving, enabling proactive retention strategies.
2. **Demand Forecasting:**  Forecasts future product demand to optimize inventory levels and sales planning.
3. **Customer Segmentation:** Groups customers based on purchase behavior, enabling targeted marketing and personalization.
4. **Customer Lifetime Value (CLV) Prediction:**  Estimates the long-term value of each customer to guide resource allocation and customer relationship management.

## Data

* **`data_cleaned.csv`:**  Cleaned dataset containing transaction-level information (customer ID, order ID, date, quantity, total price, product details).
* **Data Source:** You can download the data file from here: https://drive.google.com/file/d/10JEt8sq1NEhuv5AI7FDAmufsCy0qhVYC/view?usp=drive_link
  
## Models and Analyses

### Churn Prediction

* **Model:** XGBoost Classifier (optimized via GridSearchCV)
* **Features:** 
    * Aggregated metrics: total orders, average order value, recency, frequency, unique products purchased
    * Calculated features: time since first/last purchase, change in purchase frequency, etc.
* **Evaluation:**
    * Metrics: Accuracy, precision, recall, F1-score, ROC-AUC, Precision-Recall Curve.
    * Interpretation: SHAP (SHapley Additive exPlanations) for understanding feature importance.

### Demand Forecasting

* **Model:** Facebook Prophet
* **Data:** Aggregated daily (or other frequency) sales data.
* **Optional:** External regressors (holidays, promotions, etc.).

### Customer Segmentation

* **Model:** K-Means Clustering
* **Features:** Standardized subset of relevant customer features.
* **Evaluation:** Elbow method, Silhouette analysis, interpretability of clusters.

### Customer Lifetime Value (CLV)

* **Model:** BG/NBD (Beta Geometric/Negative Binomial Distribution) model from the `lifetimes` library
* **Features:** Recency, frequency, monetary value of transactions
* **Output:** Predicted CLV for each customer over a 12-month period.

## Power BI Dashboard
**This interactive dashboard provides a user-friendly way to explore and visualize the key insights from your sales data analysis. It's organized into three main sections, offering a holistic view of customer behavior, product performance, and overall sales trends.**

### **Sales Report**
   1. **Revenue Analysis:**
      * **Map:** Geographic distribution of sales figures by city.
      * **Animation:** Evolution of customer segments based on total spending.
      * **Line Chart:** Total sales trend over time, broken down by month and year.
      * **Table:** Detailed sales data for each city, with summaries by family, range, and order counts.

   2. **Product Insights:**
      * **Cards:** Top-selling products, sub-families, and ranges.
      * **Table:** Granular order data, including product counts and order values.
      * **Pie Chart:** Distribution of orders by day of the week.

### **Clients Analysis**
   1. **Customer Overview:**
      * **Card:** Number of customers
      * **Card:** City with the most customers
      * **Histogram:** Customer count by city
      * **Interactive Map:** Exploration of customer locations.
      * **Timeline/Table:** First and last order dates for each customer.
        
  2. **Churn Insights:**
      * **Pie Chart:** Proportion of churned vs. not churned customers.
      * **Table:** Detailed customer data, including churn predictions.
     
### **Products Analysis**
   1. **Product Overview:**
      * **Cards:** Number of products and unique ranges.
      * **Interactive Map:** Sales by city and product.
      * **Table:** Product details with associated range, order counts, and total quantity sold.

## Usage

1. **Install Packages:**  `pip install pandas numpy scikit-learn xgboost prophet lifetimes plotly ipywidgets`
2. **Jupyter Notebooks:**
   * `data_preparation.ipynb`: Load and preprocess your data.
   * `churn_prediction.ipynb`: Train and evaluate the churn prediction model. 
   * `demand_forecasting.ipynb`:  Generate demand forecasts.
   * `customer_segmentation.ipynb`: Perform customer segmentation.
   * `clv_prediction.ipynb`: Calculate Customer Lifetime Value.
3. **Examine Results:** Look at visualizations, evaluation metrics, and SHAP explanations.
4. **Apply Insights:** Translate findings into actionable recommendations for your business.

## Limitations and Future Work
*   **Explore Additional Models:**  Experiment with alternative algorithms for churn prediction and demand forecasting.
*   **Incorporate External Data:**  Enhance demand forecasts by including data on promotions, holidays, and other relevant factors.
*   **Expand Dashboard:** Add more visualizations and interactivity to the Power BI dashboard.
