# Sales Analytics and Prediction Project

This project dives deep into customer sales data to uncover valuable insights for business decision-making. It leverages machine learning and time-series forecasting to predict customer churn, forecast product demand, and segment customers based on their purchasing behavior.

## Table of Contents

- [Project Overview](#project-overview)
- [Data](#data)
- [Models and Analyses](#models-and-analyses)
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
* **Other Potential Data (Optional):**
    * Customer demographics
    * Product attributes 
    * Web browsing data
    * Support tickets

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
* **Evaluation:** MAE, MAPE, RMSE, visual comparison to actuals, backtesting.

### Customer Segmentation

* **Model:** K-Means Clustering
* **Features:** Standardized subset of relevant customer features.
* **Evaluation:** Elbow method, Silhouette analysis, interpretability of clusters.

### Customer Lifetime Value (CLV)

* **Model:** BG/NBD (Beta Geometric/Negative Binomial Distribution) model from the `lifetimes` library
* **Features:** Recency, frequency, monetary value of transactions
* **Output:** Predicted CLV for each customer over a 12-month period.

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

[Discuss data limitations, model assumptions, and potential improvements, such as incorporating new features, experimenting with different models, or integrating with other systems.] 
